import logging


class AlertEngine:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def check(self, metrics):
        alerts = []

        if metrics["cpu_percent"] > self.thresholds["cpu"]:
            alerts.append(f"CPU usage high: {metrics['cpu_percent']}%")

        if metrics["memory_percent"] > self.thresholds["memory"]:
            alerts.append(f"Memory usage high: {metrics['memory_percent']}%")

        if metrics["disk_percent"] > self.thresholds["disk"]:
            alerts.append(f"Disk usage high: {metrics['disk_percent']}%")

        for alert in alerts:
            logging.warning(alert)

        return alerts
