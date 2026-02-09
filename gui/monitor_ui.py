# gui/monitor_ui.py

import tkinter as tk
from tkinter import ttk
from system_monitor.monitor import run_monitor
from core.logger import setup_logger

setup_logger()

def run_monitor_ui(cfg=None):
    # Create top-level window
    win = tk.Toplevel()
    win.title("📊 System Monitor Dashboard")
    win.geometry("450x350")
    win.resizable(False, False)

    ttk.Label(win, text="System Monitor Dashboard", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Frame for metrics
    metrics_frame = ttk.Frame(win)
    metrics_frame.pack(pady=10, padx=20, fill="x")

    # Labels for CPU, RAM, Disk
    cpu_label = ttk.Label(metrics_frame, text="CPU Usage: --%", font=("Helvetica", 12))
    cpu_label.pack(anchor="w", pady=5)
    ram_label = ttk.Label(metrics_frame, text="RAM Usage: --%", font=("Helvetica", 12))
    ram_label.pack(anchor="w", pady=5)
    disk_label = ttk.Label(metrics_frame, text="Disk Usage: --%", font=("Helvetica", 12))
    disk_label.pack(anchor="w", pady=5)

    # Status / Alerts
    status_label = ttk.Label(win, text="Checking system metrics...", font=("Helvetica", 12, "bold"))
    status_label.pack(pady=15)

    # CSV report label
    report_label = ttk.Label(win, text="", font=("Helvetica", 10))
    report_label.pack(pady=5)

    # Function to refresh metrics
    def refresh_metrics():
        report_file, alerts = run_monitor()
        # Read the latest metrics from CSV
        with open(report_file, "r") as f:
            lines = f.readlines()[1:]  # skip header
            cpu_val = lines[0].split(",")[1].strip()
            ram_val = lines[1].split(",")[1].strip()
            disk_val = lines[2].split(",")[1].strip()

        cpu_label.config(text=f"CPU Usage: {cpu_val}%", foreground="red" if float(cpu_val) > 90 else "green")
        ram_label.config(text=f"RAM Usage: {ram_val}%", foreground="red" if float(ram_val) > 90 else "green")
        disk_label.config(text=f"Disk Usage: {disk_val}%", foreground="red" if float(disk_val) > 90 else "green")

        if alerts:
            status_label.config(text=f"⚠️ Alerts: {len(alerts)} issue(s) detected", foreground="red")
        else:
            status_label.config(text="✅ All system metrics within thresholds", foreground="green")

        report_label.config(text=f"📄 Report generated: {report_file}")

    # Buttons frame
    btn_frame = ttk.Frame(win)
    btn_frame.pack(pady=10)

    ttk.Button(btn_frame, text="🔄 Refresh Metrics", command=refresh_metrics, width=20).pack(side="left", padx=10)
    ttk.Button(btn_frame, text="❌ Close", command=win.destroy, width=20).pack(side="right", padx=10)

    # Initial metrics refresh
    refresh_metrics()

    win.mainloop()
