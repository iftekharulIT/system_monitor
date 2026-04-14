# alerts.py

from config import CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD

def check_alerts(cpu, ram, disk):
    if cpu > CPU_THRESHOLD:
        print(f"⚠️ HIGH CPU USAGE: {cpu}%")

    if ram > RAM_THRESHOLD:
        print(f"⚠️ HIGH RAM USAGE: {ram}%")

    if disk > DISK_THRESHOLD:
        print(f"⚠️ HIGH DISK USAGE: {disk}%")