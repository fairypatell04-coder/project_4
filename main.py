# main.py

import sys
from cli import main as run_cli
from gui.app import run_main_gui

if __name__ == "__main__":
    # If any arguments are passed, run CLI
    if len(sys.argv) > 1:
        run_cli()
    else:
        # No arguments, launch GUI
        run_main_gui()
