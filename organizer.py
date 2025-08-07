import os
import shutil
import sys

def organize(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            ext = file.split('.')[-1]
            new_dir = os.path.join(folder_path, ext.upper())
            os.makedirs(new_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(new_dir, file))
    print("Files organized successfully!")

if __name__ == "__main__":
    folder = sys.argv[1]
    organize(folder)
