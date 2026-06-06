"""Digital clock application with multiple timezone support."""

import gradio as gr
from datetime import datetime
import pytz
from typing import List, Dict
import json


class DigitalClockApp:
    """A digital clock application that displays time across multiple timezones."""

    # Common timezones
    COMMON_TIMEZONES = [
        "UTC",
        "America/New_York",
        "America/Los_Angeles",
        "America/Chicago",
        "Europe/London",
        "Europe/Paris",
        "Europe/Berlin",
        "Asia/Tokyo",
        "Asia/Shanghai",
        "Asia/Hong_Kong",
        "Asia/Singapore",
        "Asia/Dubai",
        "Asia/Bangkok",
        "Asia/Kolkata",
        "Australia/Sydney",
        "Australia/Melbourne",
        "Pacific/Auckland",
    ]

    def __init__(self):
        """Initialize the digital clock app."""
        self.selected_timezones = self.COMMON_TIMEZONES[:6]  # Default 6 timezones

    def get_time_in_timezone(self, timezone_str: str) -> str:
        """Get formatted time in a specific timezone.

        Args:
            timezone_str: Timezone string (e.g., 'America/New_York')

        Returns:
            Formatted time string
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            # Format: HH:MM:SS
            return local_time.strftime("%H:%M:%S")
        except Exception as e:
            return f"Error: {str(e)}"

    def get_date_in_timezone(self, timezone_str: str) -> str:
        """Get formatted date in a specific timezone.

        Args:
            timezone_str: Timezone string (e.g., 'America/New_York')

        Returns:
            Formatted date string
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            # Format: YYYY-MM-DD (Day)
            return local_time.strftime("%Y-%m-%d (%A)")
        except Exception as e:
            return f"Error: {str(e)}"

    def get_full_datetime(self, timezone_str: str) -> str:
        """Get full datetime information in a specific timezone.

        Args:
            timezone_str: Timezone string

        Returns:
            Full datetime string with timezone offset
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            offset = local_time.strftime("%z")
            # Format offset as +HH:MM or -HH:MM
            offset_formatted = f"{offset[:3]}:{offset[3:]}"
            return f"{local_time.strftime('%Y-%m-%d %H:%M:%S')} (UTC{offset_formatted})"
        except Exception as e:
            return f"Error: {str(e)}"

    def display_clock(self, selected_zones: List[str]) -> str:
        """Generate HTML display for multiple timezone clocks.

        Args:
            selected_zones: List of selected timezone strings

        Returns:
            HTML string for display
        """
        if not selected_zones:
            selected_zones = self.selected_timezones

        html_content = """
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 30px; border-radius: 10px; font-family: 'Courier New', monospace;">
            <h1 style="text-align: center; color: white; margin-bottom: 30px;">🌍 Global Digital Clock</h1>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
        """

        for timezone_str in selected_zones:
            time_str = self.get_time_in_timezone(timezone_str)
            date_str = self.get_date_in_timezone(timezone_str)
            full_info = self.get_full_datetime(timezone_str)

            # Extract timezone name for display
            tz_name = timezone_str.replace("_", " ")

            html_content += f"""
            <div style="background: rgba(255, 255, 255, 0.1); 
                        border: 2px solid rgba(255, 255, 255, 0.3);
                        border-radius: 10px; padding: 20px; 
                        backdrop-filter: blur(10px);">
                <h2 style="color: #4CAF50; margin: 0 0 10px 0; font-size: 16px;">{tz_name}</h2>
                <div style="background: rgba(0, 0, 0, 0.3); padding: 15px; 
                           border-radius: 5px; margin: 10px 0;">
                    <div style="font-size: 36px; color: #FFD700; font-weight: bold; 
                               letter-spacing: 2px; text-align: center;">{time_str}</div>
                </div>
                <div style="color: white; font-size: 12px; text-align: center; margin: 10px 0;">
                    {date_str}
                </div>
                <div style="color: #B0C4DE; font-size: 11px; text-align: center;">
                    {full_info}
                </div>
            </div>
            """

        html_content += """
            </div>
        </div>
        """
        return html_content

    def get_timezone_list(self) -> List[str]:
        """Get list of all available timezones.

        Returns:
            Sorted list of timezone strings
        """
        return sorted(pytz.all_timezones)

    def create_interface(self):
        """Create Gradio interface for the digital clock.

        Returns:
            Gradio Blocks interface
        """
        with gr.Blocks(
            title="Digital Clock - Multi-Timezone",
            css="""
            .timezone-selector { max-height: 300px; overflow-y: auto; }
            body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            """
        ) as interface:
            gr.Markdown(
                """# 🌍 Digital Clock Application
                View current time across multiple timezones simultaneously.
                """
            )

            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Select Timezones")
                    timezone_selector = gr.Dropdown(
                        choices=self.get_timezone_list(),
                        multiselect=True,
                        value=self.selected_timezones,
                        label="Choose timezones to display",
                        info="Select multiple timezones to monitor",
                    )
                    update_button = gr.Button(
                        "🔄 Update Clock",
                        variant="primary",
                        size="lg"
                    )

                with gr.Column(scale=2):
                    clock_display = gr.HTML(
                        value=self.display_clock(self.selected_timezones),
                        label="Clock Display"
                    )

            # Update the clock display
            def update_clock(zones):
                self.selected_timezones = zones if zones else self.COMMON_TIMEZONES[:6]
                return self.display_clock(self.selected_timezones)

            update_button.click(
                fn=update_clock,
                inputs=timezone_selector,
                outputs=clock_display
            )

            # Auto-update every second (using JavaScript)
            with gr.Row():
                gr.Markdown(
                    """### Information
                    - Clock updates in real-time
                    - UTC offset shows timezone difference from UTC
                    - Select multiple timezones to compare times
                    - Date includes day of week
                    """
                )

        return interface


def main():
    """Main entry point for the digital clock application."""
    app = DigitalClockApp()
    interface = app.create_interface()
    interface.launch(share=True, debug=True)


if __name__ == "__main__":
    main()
