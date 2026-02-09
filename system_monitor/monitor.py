# system_monitor/monitor.py

import psutil
import os
from datetime import datetime
import csv
import platform

def run_monitor():
    """
    Collect system metrics: CPU, RAM, Disk
    Save a CSV report in exports/
    Returns: (report_file_path, alerts_list)
    """
    alerts = []

    # Ensure export directory exists
    report_dir = "exports"
    os.makedirs(report_dir, exist_ok=True)

    # Timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_dir, f"system_report_{timestamp}.csv")

    # Determine root path for disk usage (Windows vs Unix)
    if platform.system() == "Windows":
        root_path = "C:\\"
    else:
        root_path = "/"

    # Collect system metrics
    cpu = psutil.cpu_percent(interval=1)  # interval=1 for accurate measurement
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage(root_path).percent

    metrics = [
        ("CPU Usage (%)", cpu),
        ("RAM Usage (%)", ram),
        ("Disk Usage (%)", disk)
    ]

    # Thresholds
    if cpu > 90:
        alerts.append("High CPU usage")
    if ram > 90:
        alerts.append("High RAM usage")
    if disk > 90:
        alerts.append("High Disk usage")

    # Save CSV report
    try:
        with open(report_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            writer.writerows(metrics)
    except Exception as e:
        alerts.append(f"Failed to write CSV: {e}")

    return report_file, alerts
