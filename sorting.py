import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def sort_files_in_directory(directory, target_directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            with ThreadPoolExecutor() as executor:
                executor.submit(sort_files_in_directory, full_path, target_directory)
        else:
            organize_file(full_path, target_directory)


def organize_file(file_path, target_directory):
    _, extension = os.path.splitext(file_path)
    if extension:
        destination_folder = os.path.join(target_directory, extension[1:])
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, destination_folder)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py sorting.py [path to folder]")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = os.path.join(source_directory, "Sorted Files")

    sort_files_in_directory(source_directory, target_directory)
