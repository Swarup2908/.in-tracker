# utils.py
import re
from datetime import datetime

def get_month_year_from_filename(filename):
    match = re.search(r"(\d{2})-(\d{2})-(\d{4})", filename)
    if match:
        day, month, year = match.groups()
        try:
            date = datetime.strptime(f"{year}-{month}", "%Y-%m")
            return date.strftime("%B %Y")  # Example: "May 2024"
        except:
            pass
    return "Unknown"
