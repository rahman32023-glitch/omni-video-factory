"""Utility functions for timezone operations."""

import pytz
from datetime import datetime, timedelta
from typing import List, Dict, Tuple


class TimezoneUtils:
    """Utility class for timezone-related operations."""

    @staticmethod
    def get_timezone_offset(timezone_str: str) -> Tuple[int, int]:
        """Get UTC offset for a timezone in hours and minutes.

        Args:
            timezone_str: Timezone string (e.g., 'America/New_York')

        Returns:
            Tuple of (hours, minutes) offset from UTC
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            offset = local_time.utcoffset()
            total_seconds = int(offset.total_seconds())
            hours, remainder = divmod(abs(total_seconds), 3600)
            minutes = remainder // 60
            if total_seconds < 0:
                hours = -hours
            return (hours, minutes)
        except Exception:
            return (0, 0)

    @staticmethod
    def get_timezone_info(timezone_str: str) -> Dict:
        """Get detailed information about a timezone.

        Args:
            timezone_str: Timezone string

        Returns:
            Dictionary with timezone information
        """
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            hours, minutes = TimezoneUtils.get_timezone_offset(timezone_str)
            offset_str = f"UTC{hours:+03d}:{minutes:02d}"

            return {
                "timezone": timezone_str,
                "display_name": timezone_str.replace("_", " "),
                "current_time": local_time.strftime("%H:%M:%S"),
                "current_date": local_time.strftime("%Y-%m-%d"),
                "day_of_week": local_time.strftime("%A"),
                "utc_offset": offset_str,
                "is_dst": bool(local_time.dst()),
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def compare_timezones(tz1: str, tz2: str) -> Dict:
        """Compare two timezones.

        Args:
            tz1: First timezone string
            tz2: Second timezone string

        Returns:
            Dictionary with comparison results
        """
        try:
            tz1_obj = pytz.timezone(tz1)
            tz2_obj = pytz.timezone(tz2)

            time1 = datetime.now(tz1_obj)
            time2 = datetime.now(tz2_obj)

            diff = time2.utcoffset() - time1.utcoffset()
            hours, remainder = divmod(int(diff.total_seconds()), 3600)
            minutes = remainder // 60

            return {
                "tz1": tz1,
                "tz2": tz2,
                "time_difference": f"{hours:+03d}:{minutes:02d}",
                "tz1_time": time1.strftime("%H:%M:%S"),
                "tz2_time": time2.strftime("%H:%M:%S"),
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_timezones_by_offset(offset_hours: int, offset_minutes: int = 0) -> List[str]:
        """Get all timezones with a specific UTC offset.

        Args:
            offset_hours: Hours offset from UTC
            offset_minutes: Minutes offset from UTC (default: 0)

        Returns:
            List of timezone strings
        """
        matching_timezones = []
        target_offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        for tz_name in pytz.all_timezones:
            try:
                tz = pytz.timezone(tz_name)
                local_time = datetime.now(tz)
                if local_time.utcoffset() == target_offset:
                    matching_timezones.append(tz_name)
            except Exception:
                pass

        return sorted(matching_timezones)

    @staticmethod
    def get_utc_time() -> datetime:
        """Get current UTC time.

        Returns:
            UTC datetime object
        """
        return datetime.now(pytz.UTC)

    @staticmethod
    def convert_time(time_str: str, from_tz: str, to_tz: str, time_format: str = "%H:%M:%S") -> str:
        """Convert time from one timezone to another.

        Args:
            time_str: Time string to convert
            from_tz: Source timezone string
            to_tz: Target timezone string
            time_format: Time format string (default: "%H:%M:%S")

        Returns:
            Converted time string
        """
        try:
            # Parse the time in source timezone (assuming today's date)
            from_tz_obj = pytz.timezone(from_tz)
            to_tz_obj = pytz.timezone(to_tz)

            # Create datetime with today's date
            today = datetime.today().date()
            time_obj = datetime.strptime(time_str, time_format).time()
            local_time = from_tz_obj.localize(datetime.combine(today, time_obj))

            # Convert to target timezone
            converted_time = local_time.astimezone(to_tz_obj)
            return converted_time.strftime(time_format)
        except Exception as e:
            return f"Error: {str(e)}"
