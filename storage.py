# storage.py
import csv
import os
from datetime import datetime

CSV_PATH = "data/domain_data.csv"

def init_csv():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["month_year", "count", "fetched_at"])

def read_data():
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, newline='') as f:
        return list(csv.DictReader(f))

def entry_exists(month_year):
    for row in read_data():
        if row["month_year"] == month_year:
            return True
    return False

def insert_data(month_year, count):
    if entry_exists(month_year):
        print(f"ℹ️ Entry for {month_year} already exists. Skipping.")
        return False

    with open(CSV_PATH, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([month_year, count, datetime.now().isoformat()])
    return True

def get_total_count():
    data = read_data()
    return sum(int(row["count"]) for row in data)

def get_latest_entry():
    data = read_data()
    return data[-1] if data else None
