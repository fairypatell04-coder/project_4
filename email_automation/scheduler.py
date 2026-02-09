import time
import schedule
import logging


class EmailScheduler:
    def __init__(self):
        self.jobs = []

    def schedule_once(self, delay_seconds, task):
        logging.info(f"Scheduling email in {delay_seconds} seconds")
        time.sleep(delay_seconds)
        task()

    def schedule_daily(self, time_str, task):
        schedule.every().day.at(time_str).do(task)

        while True:
            schedule.run_pending()
            time.sleep(1)
