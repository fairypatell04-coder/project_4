import os
import shutil
import logging
from datetime import datetime

class FileOrganizer:
    """Organizes files from watch_folder into categorized folders"""

    def __init__(self, watch_folder, organized_folder):
        self.watch_folder = watch_folder
        self.organized_folder = organized_folder

        self.categories = {
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
            "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv"],
            "Music": [".mp3", ".wav", ".aac", ".flac"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"]
        }

    def organize(self):
        """Move files into categorized folders"""
        for filename in os.listdir(self.watch_folder):
            src_path = os.path.join(self.watch_folder, filename)
            if not os.path.isfile(src_path):
                continue

            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, exts in self.categories.items():
                if ext in exts:
                    self._move_file(filename, category)
                    moved = True
                    break

            if not moved:
                self._move_file(filename, "Others")

    def _move_file(self, filename, category):
        dest_dir = os.path.join(self.organized_folder, category)
        os.makedirs(dest_dir, exist_ok=True)

        src_path = os.path.join(self.watch_folder, filename)
        dest_path = os.path.join(dest_dir, filename)

        # Handle duplicate files
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{base}_{timestamp}{ext}"
            dest_path = os.path.join(dest_dir, filename)

        shutil.move(src_path, dest_path)
        logging.info(f"Moved {filename} → {category}")
