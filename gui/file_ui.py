# gui/file_ui.py

import tkinter as tk
from tkinter import messagebox, filedialog
from file_organizer.organizer import FileOrganizer


def run_file_organizer_ui(cfg=None):
    win = tk.Toplevel()
    win.title("📂 File Organizer")
    win.geometry("520x320")
    win.resizable(False, False)

    tk.Label(
        win,
        text="File Organizer",
        font=("Arial", 16, "bold")
    ).pack(pady=12)

    # ---------------- WATCH FOLDER ----------------
    tk.Label(win, text="Watch Folder:").pack(anchor="w", padx=20)

    watch_var = tk.StringVar(
        value=cfg.get("watch_folder", "") if cfg else ""
    )

    watch_entry = tk.Entry(win, textvariable=watch_var, width=60)
    watch_entry.pack(padx=20)

    def choose_watch():
        path = filedialog.askdirectory(initialdir="D:/")

        if path:
            watch_var.set(path)

    tk.Button(win, text="Browse", command=choose_watch).pack(pady=5)

    # ---------------- ORGANIZED FOLDER ----------------
    tk.Label(win, text="Organized Folder:").pack(anchor="w", padx=20)

    org_var = tk.StringVar(
        value=cfg.get("organized_folder", "") if cfg else ""
    )

    org_entry = tk.Entry(win, textvariable=org_var, width=60)
    org_entry.pack(padx=20)

    def choose_org():
        path = filedialog.askdirectory(initialdir="D:/")

        if path:
            org_var.set(path)

    tk.Button(win, text="Browse", command=choose_org).pack(pady=5)

    # ---------------- STATUS ----------------
    status_label = tk.Label(win, text="", font=("Arial", 10, "bold"))
    status_label.pack(pady=8)

    # ---------------- ORGANIZE ACTION ----------------
    def organize_files():
        watch = watch_var.get().strip()
        org = org_var.get().strip()

        if not watch or not org:
            messagebox.showerror(
                "Error",
                "Please select both folders"
            )
            return

        try:
            organizer = FileOrganizer(watch, org)
            organizer.organize()

            status_label.config(
                text="✅ Files organized successfully",
                fg="green"
            )

        except Exception as e:
            status_label.config(
                text=f"❌ Failed: {e}",
                fg="red"
            )

    # ---------------- BUTTONS ----------------
    tk.Button(
        win,
        text="🚀 Organize Files",
        command=organize_files,
        width=25
    ).pack(pady=10)

    tk.Button(
        win,
        text="❌ Close",
        command=win.destroy,
        width=25
    ).pack()

    win.mainloop()
