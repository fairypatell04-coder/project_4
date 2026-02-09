# gui/scraper_ui.py

import tkinter as tk
from tkinter import messagebox
from web_scraper.scraper import WebScraper

def run_scraper_ui(cfg=None):
    win = tk.Toplevel()
    win.title("🌐 Web Scraper")
    win.geometry("420x250")

    tk.Label(win, text="Web Scraper", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(win, text="Enter URL").pack()
    url_entry = tk.Entry(win, width=45)
    url_entry.pack(pady=5)
    url_entry.insert(0, "https://example.com")

    def start_scrape():
        url = url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "URL required")
            return
        scraper = WebScraper(url)
        scraper.scrape()
        messagebox.showinfo("Success", "Scraping completed")

    tk.Button(win, text="🚀 Start Scraping", command=start_scrape).pack(pady=10)
    tk.Button(win, text="❌ Close", command=win.destroy).pack()
