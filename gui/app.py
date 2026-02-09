# gui/app.py

import tkinter as tk
import os

from core.config import load_config
from core.logger import setup_logger

from gui.theme import *
from gui.file_ui import run_file_organizer_ui
from gui.scraper_ui import run_scraper_ui
from gui.email_ui import run_email_ui
from gui.monitor_ui import run_monitor_ui

# ------------------ SETUP ------------------
setup_logger()
cfg = load_config()

# ------------------ FADE IN EFFECT ------------------
def fade_in(win):
    win.attributes("-alpha", 0.0)
    for i in range(0, 11):
        win.attributes("-alpha", i / 10)
        win.update()
        win.after(20)

# ------------------ MAIN GUI ------------------
def run_main_gui():
    root = tk.Tk()
    root.title("Automation Suite")
    root.geometry("450x420")
    root.configure(bg=BG_COLOR)
    root.resizable(False, False)

    # ------------------ APP ICON ------------------
    icon_path = os.path.join("assets", "app.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    fade_in(root)

    # ------------------ TITLE ------------------
    tk.Label(
        root,
        text="🛠️ Automation Suite",
        font=FONT_TITLE,
        bg=BG_COLOR,
        fg=TITLE_COLOR
    ).pack(pady=25)

    # ------------------ BUTTON FACTORY ------------------
    def make_btn(text, cmd, bg=BTN_COLOR, hover="#1d4ed8"):
        btn = tk.Button(
            root,
            text=text,
            width=30,
            height=2,
            command=cmd,
            bg=bg,
            fg=BTN_TEXT,
            font=FONT_BTN,
            bd=0,
            cursor="hand2",
            activebackground=hover
        )

        btn.bind("<Enter>", lambda e: btn.config(bg=hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    # ------------------ MODULE BUTTONS ------------------
    make_btn("📂 File Organizer", lambda: run_file_organizer_ui(cfg)).pack(pady=6)
    make_btn("🌐 Web Scraper", lambda: run_scraper_ui(cfg)).pack(pady=6)
    make_btn("✉️ Email Automation", lambda: run_email_ui(cfg)).pack(pady=6)
    make_btn("📊 System Monitor", run_monitor_ui).pack(pady=6)

    # ------------------ EXIT BUTTON ------------------
    make_btn("❌ Exit", root.destroy, bg="#dc2626", hover="#b91c1c").pack(pady=20)

    # ------------------ FOOTER ------------------
    tk.Label(
        root,
        text="© 2026 Automation Suite",
        bg=BG_COLOR,
        fg="#6b7280",
        font=FONT_TEXT
    ).pack(side="bottom", pady=10)

    root.mainloop()

# ------------------ ENTRY POINT ------------------
if __name__ == "__main__":
    run_main_gui()
