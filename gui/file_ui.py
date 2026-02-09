# gui/file_ui.py

import tkinter as tk
from tkinter import messagebox
from file_organizer.organizer import FileOrganizer

def run_file_organizer_ui(cfg=None):
    win = tk.Toplevel()
    win.title("📂 File Organizer")
    win.geometry("400x220")

    tk.Label(win, text="File Organizer", font=("Arial", 16, "bold")).pack(pady=10)

    def organize_files():
        organizer = FileOrganizer(
            cfg["watch_folder"],
            cfg["organized_folder"]
        )
        organizer.organize()
        messagebox.showinfo("Success", "Files organized successfully")

    tk.Button(win, text="📂 Organize Files", command=organize_files).pack(pady=10)
    tk.Button(win, text="❌ Close", command=win.destroy).pack()
