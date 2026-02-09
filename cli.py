# cli.py

import argparse
from core.config import load_config
from core.logger import setup_logger
from core.workflow import WorkflowEngine
from file_organizer.organizer import FileOrganizer

def main():
    # ------------------ LOGGER ------------------
    setup_logger()

    # ------------------ CLI PARSER ------------------
    parser = argparse.ArgumentParser(description="Automation Suite CLI")
    parser.add_argument(
        "tool",
        choices=["organize", "scrape", "email", "workflow", "gui", "monitor"],
        help="Tool to run"
    )
    args = parser.parse_args()
    print(f"🚀 Running tool: {args.tool}")

    # ------------------ LOAD CONFIG ------------------
    cfg = load_config()

    # ------------------ FILE ORGANIZER (WEEK 1) ------------------
    if args.tool == "organize":
        organizer = FileOrganizer(
            watch_folder=cfg["watch_folder"],
            organized_folder=cfg["organized_folder"]
        )
        organizer.organize()
        print("✅ File organization completed")

    # ------------------ WEB SCRAPER (WEEK 2) ------------------
    elif args.tool == "scrape":
        from web_scraper.scraper import WebScraper

        url = "https://example.com"
        scraper = WebScraper(url)
        data = scraper.scrape()
        print(f"✅ Web scraping completed: {len(data)} items found")

    # ------------------ EMAIL AUTOMATION (WEEK 3) ------------------
    elif args.tool == "email":
        from email_automation.emailer import EmailSender

        email_cfg = cfg.get("email")
        if not email_cfg:
            print("❌ Email configuration missing in config.json")
            return

        try:
            sender = EmailSender(
                smtp_server=email_cfg["smtp_server"],
                smtp_port=email_cfg["smtp_port"],
                sender_email=email_cfg["sender_email"],
                sender_password=email_cfg["sender_password"],  # Use App Password
            )
            sender.send_email(
                to_email=email_cfg["sender_email"],
                subject="🎉 Automation Suite Test Email",
                body="This is a test email from the Automation Suite CLI."
            )
            print("✅ Email sent successfully")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

    # ------------------ WORKFLOW ENGINE (Week 1+2) ------------------
    elif args.tool == "workflow":
        from web_scraper.scraper import WebScraper

        wf = WorkflowEngine("Week 1 + Week 2 Workflow")

        # Task 1: File Organizer
        organizer = FileOrganizer(
            watch_folder=cfg["watch_folder"],
            organized_folder=cfg["organized_folder"]
        )
        wf.add_task(organizer.organize)

        # Task 2: Web Scraper
        scraper = WebScraper("https://example.com")
        wf.add_task(scraper.scrape)

        wf.run()
        print("✅ Workflow completed successfully")

    # ------------------ PLACEHOLDERS ------------------
    elif args.tool == "gui":
        print("⚠️ GUI will be implemented in Week 5")

    elif args.tool == "monitor":
        from system_monitor.monitor import run_monitor
        report_file, alerts = run_monitor()
        print(f"📄 Report generated: {report_file}")
        if alerts:
            print(f"⚠️ Alerts detected: {len(alerts)} issues")
        else:
            print("✅ All system metrics within thresholds")

# ------------------ ENTRY POINT ------------------
if __name__ == "__main__":
    main()


from email_automation.emailer import EmailSender

cfg = load_config()
email_cfg = cfg["email"]

sender = EmailSender(
    smtp_server=email_cfg["smtp_server"],
    smtp_port=email_cfg["smtp_port"],
    sender_email=email_cfg["sender_email"],
    sender_password=email_cfg["sender_password"]  # Use App Password for Gmail
)

sender.send_email(
    to_email=email_cfg["sender_email"],
    subject="🎉 Automation Suite Test",
    template="welcome.html",
    context={"name": "Fairy"}
)
print("✅ Test email sent successfully")