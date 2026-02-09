import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from jinja2 import Environment, FileSystemLoader
import logging

# ------------------ LOGGER ------------------
logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize EmailSender with SMTP server details and credentials.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

        # Setup Jinja2 environment for templates
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def send_email(self, to_email, subject, body=None, template=None, context=None):
        """
        Send an email.
        - to_email: recipient email address
        - subject: email subject line
        - body: plain text email (optional if template is used)
        - template: name of HTML template file (optional)
        - context: dict of values to fill in the template
        """
        try:
            # Create message container
            msg = MIMEMultipart("alternative")
            msg["From"] = self.sender_email
            msg["To"] = to_email
            msg["Subject"] = subject

            # Render template if provided
            if template:
                tpl = self.env.get_template(template)
                html_content = tpl.render(context or {})
                mime_part = MIMEText(html_content, "html")
            else:
                mime_part = MIMEText(body or "", "plain")

            msg.attach(mime_part)

            # Connect to SMTP server
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, to_email, msg.as_string())

            logging.info(f"Email sent to {to_email}")
            print(f"✅ Email sent to {to_email}")

        except smtplib.SMTPAuthenticationError:
            logging.error("Gmail authentication failed. Use App Password, not your Gmail login password.")
            print("❌ Gmail authentication failed. Use App Password, not your Gmail login password.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            print(f"❌ Failed to send email: {e}")
