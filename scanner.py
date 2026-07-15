import os
from pathlib import Path
from datetime import datetime
from pypdf import PdfReader
from docx import Document
import sys

metadata = {
    "scan_day": datetime.today(),
    "folder": None,
    "total_files": 0,
    "total_size": 0,
     
    "files": {

    }

}

def extract_pdf(path):
    try:
        reader= PdfReader(path)
        if reader.is_encrypted:
            return "(Encrypted pdf)"
        text = ""

        for page in reader.pages:
            remaining = 200 - len(text)
            
            text += page.extract_text() or ""

            if len(text) >= 200:
                break
        return text[:200]
    except Exception as e:
        print(f"Couldn't read {path}: {e}")
        return ""

def extract_docx(path):
    reader= Document(path)
    text = []
    for para in reader.paragraphs:
        char_count = 0
        if char_count + len(para.text) >= 200:
            remaining = 200 - char_count
            text.append(para.text[:remaining])
            break
        else:
            text.append(para.text)
            char_count += len(para.text)
            # Account for the newline character between paragraphs
            text.append("\n")
            char_count += 1
            
    return "".join(text)

def extract_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return(file.read(200))

def get_preview(file):
    if (file.suffix.lower() == ".pdf"):
        return extract_pdf(file)
    elif (file.suffix.lower() == ".docx"):
        return extract_docx(file)
    elif file.suffix.lower() in [".txt", ".md", ".py"]:
        return extract_text(file)
    return ""



def scan_folder(folder_path):
    dir = Path(folder_path).expanduser()
    metadata["folder"] = folder_path

    total_size = 0
    num_files = 0

    # get data about all files in the folder/subfolders
    for file in dir.rglob('*'):
        if file.is_file():
            file_info = file.stat()

            try:
                text_chunk = get_preview(file)
            except Exception as e:
                print(f"Skipping {file.name}: {e}")
                text_chunk = ""

            file_data = {
                "id": num_files,
                "name": file.name,
                "path": file.resolve(),
                "extension": file.suffix.lower(),
                "size": file_info.st_size,
                "created": file_info.st_ctime,
                "modified": file_info.st_mtime,
                "preview": text_chunk,
                "description": f"{file.suffix} file named {file.name} with the first 200 chars being '{text_chunk}'.",
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
    return metadata["files"]