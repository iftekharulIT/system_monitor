import csv
import os
from datetime import datetime

LOG_FILE = "logs/system_log.csv"

def log_data(cpu, ram, disk):
    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header ONLY if file is new
        if not file_exists:
            writer.writerow(["Timestamp", "CPU (%)", "RAM (%)", "Disk (%)"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            round(cpu, 1),
            round(ram, 1),
            round(disk, 1)
        ])