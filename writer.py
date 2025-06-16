# writer.py
import csv
import os
from datetime import datetime

DATA_FILE = "data/domain_data.csv"

def read_existing_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_to_csv(month_year, count):
    file_exists = os.path.exists(DATA_FILE)

    if not os.path.exists("data"):
        os.makedirs("data")

    with open(DATA_FILE, mode='a', newline='') as csvfile:
        fieldnames = ['month_year', 'count', 'fetched_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'month_year': month_year,
            'count': count,
            'fetched_at': datetime.now().isoformat()
        })
