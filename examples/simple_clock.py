"""Simple example of using the digital clock."""

import sys
sys.path.insert(0, '../')

from src.clock_app import DigitalClockApp


def main():
    """Run a simple digital clock example."""
    app = DigitalClockApp()
    
    # Display time in different timezones
    zones = [
        "America/New_York",
        "Europe/London",
        "Asia/Tokyo",
        "Australia/Sydney",
    ]
    
    print("\n" + "="*60)
    print("Global Digital Clock - Simple Example")
    print("="*60 + "\n")
    
    for timezone in zones:
        time_str = app.get_time_in_timezone(timezone)
        date_str = app.get_date_in_timezone(timezone)
        full_info = app.get_full_datetime(timezone)
        
        print(f"Timezone: {timezone}")
        print(f"  Time:   {time_str}")
        print(f"  Date:   {date_str}")
        print(f"  Full:   {full_info}")
        print()


if __name__ == "__main__":
    main()
