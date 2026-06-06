"""Web-based digital clock with enhanced styling and real-time updates."""

import gradio as gr
from datetime import datetime
import pytz
from typing import List
import json


class EnhancedDigitalClock:
    """Enhanced digital clock with web interface."""

    PRESET_ZONES = {
        "Business Hours": [
            "America/New_York",
            "Europe/London",
            "Asia/Tokyo",
        ],
        "Americas": [
            "America/New_York",
            "America/Los_Angeles",
            "America/Toronto",
            "America/Sao_Paulo",
        ],
        "Europe & Africa": [
            "Europe/London",
            "Europe/Paris",
            "Europe/Moscow",
            "Africa/Cairo",
            "Africa/Johannesburg",
        ],
        "Asia Pacific": [
            "Asia/Tokyo",
            "Asia/Shanghai",
            "Asia/Singapore",
            "Australia/Sydney",
            "Pacific/Auckland",
        ],
    }

    def __init__(self):
        """Initialize enhanced clock."""
        self.all_timezones = sorted(pytz.all_timezones)

    def get_clock_card_html(self, timezone_str: str) -> str:
        """Generate HTML for a single clock card.

        Args:
            timezone_str: Timezone string

        Returns:
            HTML string for clock card
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)

            time_str = local_time.strftime("%H:%M:%S")
            date_str = local_time.strftime("%Y-%m-%d")
            day_str = local_time.strftime("%A")
            tz_name = timezone_str.replace("_", " ")

            # Get UTC offset
            offset = local_time.strftime("%z")
            offset_formatted = f"UTC{offset[:3]}:{offset[3:]}"

            # Determine card color based on time of day
            hour = local_time.hour
            if 6 <= hour < 12:
                bg_color = "#FFB6C1"  # Morning - light pink
                time_color = "#FF6347"
            elif 12 <= hour < 18:
                bg_color = "#87CEEB"  # Afternoon - sky blue
                time_color = "#1E90FF"
            elif 18 <= hour < 21:
                bg_color = "#FFA500"  # Evening - orange
                time_color = "#FF4500"
            else:
                bg_color = "#191970"  # Night - midnight blue
                time_color = "#FFD700"

            return f"""
            <div style="background: linear-gradient(135deg, {bg_color}40, {bg_color}80);
                        border: 2px solid {bg_color};
                        border-radius: 15px; padding: 25px; margin: 10px;
                        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
                        text-align: center; min-width: 280px;">
                <h3 style="color: #333; margin: 0 0 15px 0; font-size: 18px; font-weight: bold;">{tz_name}</h3>
                <div style="background: rgba(255, 255, 255, 0.9); border-radius: 10px; padding: 20px; margin: 10px 0;">
                    <div style="font-size: 48px; color: {time_color}; font-weight: bold;
                               font-family: 'Courier New', monospace; letter-spacing: 3px;">{time_str}</div>
                    <div style="font-size: 14px; color: #666; margin-top: 10px;">{date_str}</div>
                    <div style="font-size: 12px; color: #999; margin-top: 5px;">{day_str}</div>
                </div>
                <div style="color: #555; font-size: 12px; margin-top: 10px;">{offset_formatted}</div>
            </div>
            """
        except Exception as e:
            return f'<div style="color: red; padding: 20px;">Error: {str(e)}</div>'

    def display_multiple_clocks(self, timezone_list: List[str]) -> str:
        """Generate HTML display for multiple clocks.

        Args:
            timezone_list: List of timezone strings

        Returns:
            HTML string with all clocks
        """
        if not timezone_list:
            timezone_list = list(self.PRESET_ZONES["Business Hours"])

        html = '<div style="display: flex; flex-wrap: wrap; justify-content: center; background: linear-gradient(135deg, #667eea, #764ba2); padding: 20px; border-radius: 10px;">'

        for tz in timezone_list:
            html += self.get_clock_card_html(tz)

        html += '</div>'
        return html

    def create_gradio_app(self):
        """Create Gradio application.

        Returns:
            Gradio Blocks interface
        """
        with gr.Blocks(title="Digital Clock - Web", theme=gr.themes.Soft()) as app:
            gr.Markdown(
                """# ⏰ Global Digital Clock
                Real-time clock display across multiple timezones
                """,
                elem_id="title"
            )

            with gr.Row():
                with gr.Column(scale=1, min_width=250):
                    gr.Markdown("### ⚙️ Configuration")

                    preset_selector = gr.Radio(
                        choices=list(self.PRESET_ZONES.keys()),
                        value="Business Hours",
                        label="Quick Presets",
                        info="Select a preset timezone group"
                    )

                    custom_zones = gr.Dropdown(
                        choices=self.all_timezones,
                        multiselect=True,
                        label="Custom Timezones",
                        info="Or select specific timezones"
                    )

                    update_btn = gr.Button(
                        "🔄 Update Display",
                        variant="primary",
                        size="lg"
                    )

                    refresh_info = gr.Markdown(
                        "*Click 'Update Display' to refresh the clock*"
                    )

                with gr.Column(scale=3):
                    clock_display = gr.HTML(
                        value=self.display_multiple_clocks(
                            self.PRESET_ZONES["Business Hours"]
                        )
                    )

            def update_display(preset, custom):
                if custom:
                    zones = custom
                else:
                    zones = self.PRESET_ZONES.get(preset, self.PRESET_ZONES["Business Hours"])
                return self.display_multiple_clocks(zones)

            update_btn.click(
                fn=update_display,
                inputs=[preset_selector, custom_zones],
                outputs=clock_display
            )

            preset_selector.change(
                fn=update_display,
                inputs=[preset_selector, custom_zones],
                outputs=clock_display
            )

            with gr.Row():
                gr.Markdown(
                    """### 📋 Features
                    - **Real-time Updates**: Clock shows current time in each timezone
                    - **Color Coded**: Cards change color based on time of day
                    - **UTC Offset**: Shows timezone difference from UTC
                    - **Date & Day**: Displays full date and day of week
                    - **Presets**: Quick selection for common timezone groups
                    - **Custom Selection**: Choose any timezone combination
                    """
                )

        return app


def run_web_clock():
    """Run the web-based digital clock."""
    clock = EnhancedDigitalClock()
    app = clock.create_gradio_app()
    app.launch(share=True)


if __name__ == "__main__":
    run_web_clock()
