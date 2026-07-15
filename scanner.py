import os
from pathlib import Path
from datetime import datetime
import sys

category = {
    "Images": [
        ".png",
        ".jpg",
        ".jpeg",
        ".heic",
        ".gif",
        ".svg",
        ".webp",
        ".bmp",
        ".tiff",
        ".ico"
    ],
    "Documents": [
        ".pdf",
        ".docx",
        ".txt",
        ".rtf",
        ".pptx",
        ".xlsx",
        ".csv",
        ".md"
    ],
    "Archives": [
        ".zip",
        ".tar"
    ],
    "Installers": [
        ".dmg",
        ".pkg"
    ],
    "Videos": [
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".webm"
    ],
    "Audio": [
        '.mp3', 
        '.wav', 
        '.m4a', 
        '.flac', 
        '.aac'    
    ],
    "Code": [
        ".py",
        ".js",
        ".html",
        ".css",
        ".java",
        ".c",
        ".cpp",
        ".cs",
        ".rb",
        ".php",
        ".go",
        ".rs",
        ".ts",
        ".swift",
        ".kt",
        ".m",
        ".sh",
        ".bat",
        ".pl",
        ".r",
        ".lua",
        ".sql",
        ".xml",
        ".json",
        ".yaml",
        ".yml",
        ".ini",
        ".md",
    ],
    "Libraries/Binaries": [
        ".jar", 
        ".node", 
        ".dylib", 
        ".dll", 
        ".so", 
        ".a", 
        ".lib", 
        ".wasm"
    ],
    "System Files": [
        ".sys",
        ".plist",
        ".log",
        ".nib",
        ".DS_Store",
        ".localized",
        ".map"
    ]
}

category_sizes = {
    "Images": 0,
    "Documents": 0,
    "Archives": 0,
    "Installers": 0,
    "Videos": 0,
    "Audio": 0,
    "Code": 0,
    "Libraries/Binaries": 0,
    "System Files": 0,
    "Others": 0
}

ind_sizes = []

def scan_folder(folder_path):
    dir = Path(folder_path).expanduser()

    total_size = 0
    num_files = 0

    # get data about all files in the folder/subfolders
    for file in dir.rglob('*'):
        if file.is_file():
            info = file.stat()
            size = info.st_size
            created_time = datetime.fromtimestamp(info.st_ctime)
            modified_time = datetime.fromtimestamp(info.st_mtime)

            file_category = [key for key, val in category.items() if file.suffix.lower() in val]
            total_size += size
            num_files += 1
            if file_category:
                category_sizes[file_category[0]] += size
            else:
                category_sizes["Others"] += size
            ind_sizes.append((size, file.name))

    # print("\nClutterly Scan Report")
    # print("=" * 40)

    # print(f"Folder      : {dir}")
    # print(f"Total files : {num_files:,}")
    # print(f"Total size  : {total_size / (1024**3):.2f} GB")

    # print("\nLargest Categories")
    # print("-" * 40)

    # for name, size in sorted(
    #     category_sizes.items(),
    #     key=lambda item: item[1],
    #     reverse=True
    # ):
    #     print(f"{name:<22} {size / (1024**3):>7.2f} GB")
    
    # print("\nLargest Files")
    # print("-" * 40)

    # ind_sizes.sort(reverse=True)
    # five_largest = ind_sizes[:5]

    # for file in five_largest:
    #     print(f"{file[1]:<30} {file[0] / (1024**3):>7.2f} GB")