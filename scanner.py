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

def scan_folder(folder_path):
    dir = Path(folder_path).expanduser()

    total_size = 0
    num_files = 0

    # images_size = 0
    # documents_size = 0
    # archives_size = 0
    # installers_size = 0
    # videos_size = 0
    # audio_size = 0
    # code_size = 0
    # libin_size = 0
    # sysfiles_size = 0
    # others_size = 0

    # for testing
    # others_size = 0

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

    categorized_size = sum(category_sizes.values())

    # # printing the results
    # print(f"Number of files: {num_files}")
    # print(f"Total size: {total_size / (1024**3):.2f} GB")
    # print(f"Categorized: {categorized_size / (1024**3):.2f} GB")
    # print(f"Difference: {(total_size - categorized_size) / (1024**3):.2f} GB")

    # print(f"Images size: {category_sizes['Images'] / (1024**3):.2f}GB")
    # print(f"Documents size: {category_sizes['Documents'] / (1024**3):.2f}GB")
    # print(f"Archives size: {category_sizes['Archives'] / (1024**3):.2f}GB")
    # print(f"Installers size: {category_sizes['Installers'] / (1024**3):.2f}GB")
    # print(f"Videos size: {category_sizes['Videos'] / (1024**3):.2f}GB")
    # print(f"Audio size: {category_sizes['Audio'] / (1024**3):.2f}GB")
    # print(f"Code size: {category_sizes['Code'] / (1024**3):.2f}GB")
    # print(f"Libraries/Binaries size: {category_sizes['Libraries/Binaries'] / (1024**3):.2f}GB")
    # print(f"System Files size: {category_sizes['System Files'] / (1024**3):.2f}GB")
    # print(f"Others size: {category_sizes['Others'] / (1024**3):.2f}GB")

    print("\nClutterly Scan Report")
    print("=" * 40)

    print(f"Folder      : {dir}")
    print(f"Total files : {num_files:,}")
    print(f"Total size  : {total_size / (1024**3):.2f} GB")

    print("\nLargest Categories")
    print("-" * 40)

    for name, size in sorted(
        category_sizes.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{name:<22} {size / (1024**3):>7.2f} GB")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <folder_path>")
    else:
        scan_folder(sys.argv[1])
