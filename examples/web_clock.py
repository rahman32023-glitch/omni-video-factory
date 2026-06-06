"""Example of running the enhanced web-based digital clock."""

import sys
sys.path.insert(0, '../')

from src.clock_web import EnhancedDigitalClock


def main():
    """Run the enhanced web-based clock."""
    print("Starting Enhanced Digital Clock...")
    print("Opening in browser...\n")
    
    clock = EnhancedDigitalClock()
    app = clock.create_gradio_app()
    app.launch(
        share=True,
        debug=False,
        show_error=True
    )


if __name__ == "__main__":
    main()
