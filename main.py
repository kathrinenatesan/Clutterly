import os
from pathlib import Path
import sys
from scanner import scan_folder

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <folder_path>")
    else:
        files = scan_folder(sys.argv[1])
print(files)