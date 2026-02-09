# gui/email_ui.py

import tkinter as tk
from tkinter import messagebox
from email_automation.emailer import EmailSender

# ------------------ EMAIL TEMPLATES ------------------
EMAIL_TEMPLATES = {
    "Welcome": "Hello {name},\n\nWelcome to our Automation Suite!\n\nBest regards,\nAutomation Team",
    "Reminder": "Hello {name},\n\nThis is a friendly reminder from Automation Suite.\n\nThank you!",
    "Custom": ""
}

# ------------------ MAIN EMAIL UI ------------------
def run_email_ui(cfg):
    win = tk.Toplevel()
    win.title("✉️ Email Automation")
    win.geometry("520x540")
    win.resizable(False, False)

    # ------------------ TITLE ------------------
    tk.Label(
        win,
        text="Send Personalized Email",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=15)

    # ------------------ FORM FRAME ------------------
    frame = tk.Frame(win)
    frame.pack(padx=20, pady=5, fill="x")

    def field(label):
        tk.Label(frame, text=label, anchor="w").pack(fill="x", pady=(10, 2))

    # Recipient Email
    field("Recipient Email")
    recipient_entry = tk.Entry(frame)
    recipient_entry.pack(fill="x")
    recipient_entry.insert(0, cfg["email"]["sender_email"])

    # Recipient Name
    field("Recipient Name")
    name_entry = tk.Entry(frame)
    name_entry.pack(fill="x")
    name_entry.insert(0, "Friend")

    # Subject
    field("Subject")
    subject_entry = tk.Entry(frame)
    subject_entry.pack(fill="x")
    subject_entry.insert(0, "Automation Suite Email")

    # Template
    field("Template")
    template_var = tk.StringVar(value="Welcome")
    template_menu = tk.OptionMenu(frame, template_var, *EMAIL_TEMPLATES.keys())
    template_menu.pack(fill="x")

    # Message
    field("Message")
    message_box = tk.Text(frame, height=8)
    message_box.pack(fill="both")

    # ------------------ STATUS LABEL ------------------
    status_label = tk.Label(win, text="", font=("Segoe UI", 10, "bold"))
    status_label.pack(pady=10)

    # ------------------ TEMPLATE HANDLER ------------------
    def update_message(*args):
        template = EMAIL_TEMPLATES.get(template_var.get(), "")
        name = name_entry.get() or "Friend"
        message_box.delete("1.0", tk.END)
        message_box.insert(tk.END, template.format(name=name))

    template_var.trace_add("write", update_message)
    name_entry.bind("<KeyRelease>", update_message)
    update_message()

    # ------------------ SEND EMAIL ------------------
    def send_email():
        to_email = recipient_entry.get().strip()
        subject = subject_entry.get().strip()
        body = message_box.get("1.0", tk.END).strip()

        if not to_email or not subject or not body:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            email_cfg = cfg["email"]
            sender = EmailSender(
                smtp_server=email_cfg["smtp_server"],
                smtp_port=email_cfg["smtp_port"],
                sender_email=email_cfg["sender_email"],
                sender_password=email_cfg["sender_password"]
            )

            sender.send_email(to_email, subject, body)
            status_label.config(
                text=f"✅ Email sent successfully to {to_email}",
                fg="green"
            )

        except Exception as e:
            status_label.config(
                text=f"❌ Failed to send email: {e}",
                fg="red"
            )

    # ------------------ BUTTONS ------------------
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=2)

    tk.Button(
        btn_frame,
        text="📨 Send Email",
        width=18,
        height=3,
        bg="#2563eb",
        fg="white",
        command=send_email
    ).pack(side="left", padx=10)

    tk.Button(
        btn_frame,
        text="❌ Close",
        width=18,
        height=2,
        bg="#dc2626",
        fg="white",
        command=win.destroy
    ).pack(side="right", padx=10)
