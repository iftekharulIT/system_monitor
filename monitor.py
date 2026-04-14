# monitor.py

import psutil
import time
from logger import log_data
from alerts import check_alerts

def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return cpu, ram, disk

def run_monitor():
    print("🚀 Starting System Monitor...")

    while True:
        cpu, ram, disk = get_system_usage()

        print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

        log_data(cpu, ram, disk)
        check_alerts(cpu, ram, disk)

        time.sleep(5)  # run every 5 seconds

if __name__ == "__main__":
    run_monitor()