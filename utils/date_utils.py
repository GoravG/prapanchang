
from datetime import datetime as Date

from datetime import datetime

def get_date_from_string(date_str: str):
    """Convert a date string in dd-mm-yyyy format to a datetime.date object."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Expected format is dd-mm-yyyy.")