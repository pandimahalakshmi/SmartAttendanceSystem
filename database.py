import csv
from datetime import datetime

def mark_attendance(name):
    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([name, dt_string])

def create_csv():
    with open("attendance.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Time"])
