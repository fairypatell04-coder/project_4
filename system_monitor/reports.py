import csv
from pathlib import Path
from datetime import datetime


class ReportGenerator:
    def export_csv(self, metrics):
        Path("exports").mkdir(exist_ok=True)

        filename = f"exports/system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=metrics.keys())
            writer.writeheader()
            writer.writerow(metrics)

        return filename
