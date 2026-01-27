import time
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,  # Controls how much detail you see (DEBUG < INFO < WARNING < ERROR)
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

# False its REAL True its a dry run!
DRY_RUN = False

BASE_DIR: Path  = Path("D:/Digital Art/2025")    

FOLDERS = [
    "Character-design/jpg",
    "Finished-painting/jpg/Progress",
    "Finished-painting/Boards",
    "Finished-painting/Back-ups",
    "Finished-painting/Values",
    "Timelaps"
]


def setup_directories(base: Path, folders: list[str]) -> None:
    for folder in folders:
        full_path = base / folder
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {full_path}")
        else:
            logging.debug(f"Directory already exists: {full_path}")


def detect_files(folder: Path) -> None: 
    for file in folder.iterdir():
        if file.is_file():
            mod_time = datetime.fromtimestamp(file.stat().st_mtime)
            logging.info(f"file Name: {file.name}") 
            logging.info(f"Extension: {file.suffix}") 
            logging.info(f"Last modified: {mod_time}") 
            logging.info(f"Full path: {file}")
            logging.info(f"------------------------------") 


def decide_destination(file: Path, base: Path) -> Path:
    """
    Decide where this file should go based on type, name, and age.
    Returns the destination folder Path.
    """
    # check file type
    # check name rules
    # return full destination path
    if file.suffix == ".jpg" or file.suffix == ".png":
        if "finale" in file.name.lower() or "final" in file.name.lower():
             return base / "Finished-painting/jpg"
        elif "character" in file.name.lower() or "design" in file.name.lower():
            return base / "Character-design/jpg"
        else:
            return base / "Finished-painting/jpg/Progress"
    elif file.suffix == ".clip":
        mod_time = file.stat().st_mtime
        thresh_time = time.time() - 7*86400
        if "finale" in file.name.lower() or "final" in file.name.lower():
            return base / "Finished-painting"
        elif "character" in file.name.lower() or "design" in file.name.lower():
            return base / "Character-design"
        elif "board" in file.name.lower():
            return base / "Finished-painting/Boards"
        elif mod_time < thresh_time:
            return base / "Finished-painting/Back-ups"
        else:
            return base / "Finished-painting"
    elif file.suffix == ".mp4":
        return base / "Timelaps"
    return base


def move_file_safely(file: Path, base: Path, dry_run: bool = DRY_RUN):
    if not file.is_file():
        return
    
    destination = decide_destination(file, base)  

    if not destination.exists():
        if dry_run:
            logging.info(f"[DRY RUN] Would create directory: {destination}")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {destination}")

    full_path = destination / file.name
    counter = 1
    while full_path.exists():
        new_name = file.stem + "_" + str(counter) + file.suffix
        full_path = destination / new_name
        counter += 1
        
    if dry_run:
        logging.info(f"[DRY RUN] Would move {file} -> {full_path}")
    else:
        file.rename(full_path)
        logging.info(f"file:{file.name} moved as {full_path.name} to {destination}")    


if __name__ == "__main__":
    if BASE_DIR.exists():
        logging.info(f"Base directory found: {BASE_DIR}")
        setup_directories(BASE_DIR, FOLDERS)
    else:
        logging.error(f"Base directory does not exist: {BASE_DIR}")

    for file in BASE_DIR.iterdir():
        if file.is_file():
            move_file_safely(file, BASE_DIR, dry_run=DRY_RUN)