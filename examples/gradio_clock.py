"""Example of running the Gradio-based digital clock."""

import sys
sys.path.insert(0, '../')

from src.clock_app import DigitalClockApp


def main():
    """Run the Gradio digital clock interface."""
    print("Starting Digital Clock Application...")
    print("Opening in browser...\n")
    
    app = DigitalClockApp()
    interface = app.create_interface()
    interface.launch(
        share=True,
        debug=False,
        show_error=True
    )


if __name__ == "__main__":
    main()
