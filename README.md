# 🛠️ Automation Suite (Python)

A complete Python-based Automation Suite that provides multiple automation tools
through both **CLI** and **GUI** interfaces.

---

## 🚀 Features

### 📂 File Organizer
- Automatically organizes files based on extension
- Supports custom folder rules

### 🌐 Web Scraper
- Scrapes webpage title and content
- Simple and beginner-friendly UI

### ✉️ Email Automation
- Sends emails using Gmail SMTP (App Password)
- Supports templates and custom messages

### 📊 System Monitor
- Monitors CPU, RAM, and Disk usage
- Generates CSV reports
- Alerts when thresholds exceed limits

---

## 🧠 Architecture

Project 4/
│
├── core/
│ ├── config.py
│ ├── logger.py
│
├── gui/
│ ├── app.py
│ ├── file_ui.py
│ ├── scraper_ui.py
│ ├── email_ui.py
│ ├── monitor_ui.py
│ └── theme.py
│
├── system_monitor/
│ └── monitor.py
│
├── email_automation/
│ └── emailer.py
│
├── tests/
│ └── test_email.py
│
├── exports/
├── logs/
├── cli.py
├── requirements.txt
└── README.md



---

## ▶️ How to Run

### 🔹 1. Install Dependencies
```bash
pip install -r requirements.txt


Run CLI
python cli.py


Run GUI



Testing
python -m unittest discover tests