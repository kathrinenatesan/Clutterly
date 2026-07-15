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

metadata = {
    "scan_day": datetime.today(),
    "folder": None,
    "total_files": 0,
    "total_size": 0,
     
    "files": {

    }

}

def scan_folder(folder_path):
    dir = Path(folder_path).expanduser()
    metadata["folder"] = folder_path

    total_size = 0
    num_files = 0

    # get data about all files in the folder/subfolders
    for file in dir.rglob('*'):
        if file.is_file():
            file_info = file.stat()
            file_data = {
                "id": num_files,
                "name": file.name,
                "path": Path(file.name).resolve(),
                "extension": file.suffix.lower(),
                "size": file_info.st_size,
                "created": file_info.st_ctime,
                "modified": file_info.st_mtime,
                "preview": "",
                "description": "",
                "embedding": None,
                "cluster": None,
                "suggested_folder": None,
                "reason": None,
                "delete_candidate": False,
                "duplicates": []
            }
            total_size += file_info.st_size
            metadata["files"][num_files] = file_data
            num_files += 1
    metadata["total_size"] = total_size
    metadata["total_files"] = num_files
    return metadata