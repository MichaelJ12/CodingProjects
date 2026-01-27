import os, shutil
import time
import psutil

current_dir = "D:Digital Art/2025/"
files_in_dir = os.listdir(current_dir)

folder_names = [
    'Character-design/jpg',
    'Finished-painting/jpg/Progress',
    'Finished-painting/Boards',
    'Finished-painting/Back-ups',
    'Finished-painting/Values',
    'Timelaps'
]

if not os.path.exists(current_dir):
    print(f"Directory does not exist: {current_dir}")
else:
    print(f"Directory exists: {current_dir}")
print("Script started!")

#create folder if not exist
for folder in folder_names:
    full_path =  os.path.join(current_dir, folder)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

def move_file(src, dest):
    if not os.path.exists(dest):
        shutil.move(src, dest)

def is_file_in_use(file_path):
    try:
        with open(file_path, 'r'):
            return False
    except IOError:
        print(f"Skipping '{file_path}' because it is currently in use or locked.")
        return True

week = 7 * 86400 # 7 days in seconds
current_time = time.time() # Current time in seconds since epoch
threshold_time = current_time - week # Files older than one week

file_rules = {
    "clip": {
        "Finale": "Finished-painting",
        "character": "Character-design",
        "Board": "Finished-painting/Boards",
        "Backup": "Finished-painting/Back-ups"
    },
    "jpg": {
        "Finale": "Finished-painting/jpg",
        "character": "Character-design/jpg",
        "default": "Finished-painting/jpg/Progress"
    },
    "mp4": "Timelaps"
}

path = "D:/Digital Art/2025/Finished-painting/"
files_in_path = os.listdir(path)

for file in files_in_path:
    print(f"Checking file: {file}")
    file_path = os.path.join(path, file)
    last_modified = os.path.getmtime(file_path)

    if os.path.isdir(file_path):
        print(f"Skipping directory: {file_path}")
        continue

    print(f"Checking file: {file}")

    if is_file_in_use(file_path):  # Skip files in use
        continue

    if file.endswith(".clip"):
        if "Finale" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting", file))
        elif "Board" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Boards", file))
        elif "Character" in file:
            move_file(file_path, os.path.join(current_dir, "Character-design", file))
        elif last_modified < threshold_time:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Back-ups", file))

    elif file.endswith(".jpg"):
        if "Finale" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/jpg", file))
        elif "Board" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Boards", file))
        elif "Character" in file:
            move_file(file_path, os.path.join(current_dir, "Character-design/jpg", file))
        else:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/jpg/Progress", file))

# Process files in current_dir
for file in files_in_dir:
    file_path = os.path.join(current_dir, file)
    last_modified = os.path.getmtime(file_path)

    if is_file_in_use(file_path):  # Skip files in use
        continue

    # Handle .clip files
    if file.endswith(".clip"):
        if "Finale" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting", file))
        elif "Board" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Boards", file))
        elif "Character" in file:
            move_file(file_path, os.path.join(current_dir, "Character-design", file))
        elif last_modified < threshold_time:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Back-ups", file))
        else:
            move_file(file_path, os.path.join(current_dir, "Finished-painting", file))

    # Handle .jpg files
    elif file.endswith(".jpg"):
        if "Finale" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/jpg", file))
        elif "Board" in file:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/Boards", file))
        elif "Character" in file:
            move_file(file_path, os.path.join(current_dir, "Character-design/jpg", file))
        else:
            move_file(file_path, os.path.join(current_dir, "Finished-painting/jpg/Progress", file))

    # Handle "Board" files


    # Handle .mp4 files
    elif file.endswith(".mp4"):
        move_file(file_path, os.path.join(current_dir, "Timelaps", file))










