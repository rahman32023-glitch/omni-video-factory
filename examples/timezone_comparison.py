"""Example of comparing timezones using timezone utilities."""

import sys
sys.path.insert(0, '../')

from src.timezone_utils import TimezoneUtils


def main():
    """Demonstrate timezone comparison features."""
    print("\n" + "="*60)
    print("Timezone Comparison Examples")
    print("="*60 + "\n")
    
    # Example 1: Get timezone info
    print("1. Timezone Information:")
    print("-" * 40)
    tz_info = TimezoneUtils.get_timezone_info("America/New_York")
    for key, value in tz_info.items():
        print(f"  {key}: {value}")
    
    print("\n2. Compare Two Timezones:")
    print("-" * 40)
    comparison = TimezoneUtils.compare_timezones(
        "America/New_York",
        "Asia/Tokyo"
    )
    for key, value in comparison.items():
        print(f"  {key}: {value}")
    
    print("\n3. Get Timezones by UTC Offset:")
    print("-" * 40)
    zones = TimezoneUtils.get_timezones_by_offset(-5, 0)
    print(f"  Timezones with UTC-5:00 offset (sample):")
    for zone in zones[:5]:
        print(f"    - {zone}")
    if len(zones) > 5:
        print(f"    ... and {len(zones) - 5} more")
    
    print("\n4. Convert Time Between Timezones:")
    print("-" * 40)
    converted = TimezoneUtils.convert_time(
        "14:30:00",
        "America/New_York",
        "Asia/Tokyo"
    )
    print(f"  14:30:00 in New York = {converted} in Tokyo")


if __name__ == "__main__":
    main()
