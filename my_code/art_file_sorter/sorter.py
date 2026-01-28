import time
import logging
from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------
# Sets up logging so the script prints readable status messages
logging.basicConfig(
    level=logging.INFO,  # Minimum level to show (DEBUG < INFO < WARNING < ERROR)
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

# --------------------------------------------------
# GLOBAL SETTINGS
# --------------------------------------------------
# False = real file moves
# True  = dry run (no files are actually moved)
DRY_RUN = False

# Base directory where all files and folders live
BASE_DIR: Path = Path("D:/Digital Art/2026")

# Folder structure that should always exist
FOLDERS = [
    "Character-design/jpg",
    "Finished-painting/jpg/Progress",
    "Finished-painting/Boards",
    "Finished-painting/Back-ups",
    "Finished-painting/Values",
    "Timelaps"
]

# --------------------------------------------------
# DIRECTORY SETUP
# --------------------------------------------------
def setup_directories(base: Path, folders: list[str]) -> None:
    """
    Create required directory structure if it does not exist.
    """
    for folder in folders:
        full_path = base / folder

        # Create directory (including parents) if missing
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {full_path}")
        else:
            logging.debug(f"Directory already exists: {full_path}")

# --------------------------------------------------
# FILE INSPECTION (DEBUG / INFO TOOL)
# --------------------------------------------------
def detect_files(folder: Path) -> None:
    """
    Logs information about each file in a folder.
    Useful for debugging and understanding file metadata.
    """
    for file in folder.iterdir():
        if file.is_file():
            mod_time = datetime.fromtimestamp(file.stat().st_mtime)

            logging.info(f"file Name: {file.name}")
            logging.info(f"Extension: {file.suffix}")
            logging.info(f"Last modified: {mod_time}")
            logging.info(f"Full path: {file}")
            logging.info(f"------------------------------")

# --------------------------------------------------
# DESTINATION DECISION LOGIC
# --------------------------------------------------
def decide_destination(file: Path, base: Path) -> Path:
    """
    Decide where a file should go based on:
    - File extension
    - Keywords in filename
    - File age (for backups)
    
    Returns the destination folder path.
    """

    # --------------------------
    # IMAGE FILES
    # --------------------------
    if file.suffix == ".jpg" or file.suffix == ".png":
        if "finale" in file.name.lower() or "final" in file.name.lower():
            return base / "Finished-painting/jpg"
        elif "character" in file.name.lower() or "design" in file.name.lower():
            return base / "Character-design/jpg"
        else:
            # Default location for WIP images
            return base / "Finished-painting/jpg/Progress"

    # --------------------------
    # CLIP STUDIO FILES
    # --------------------------
    elif file.suffix == ".clip" or file.suffix == '.pur':
        mod_time = file.stat().st_mtime
        thresh_time = time.time() - 7 * 86400  # 7 days ago

        if "finale" in file.name.lower() or "final" in file.name.lower():
            return base / "Finished-painting"
        elif "character" in file.name.lower() or "design" in file.name.lower():
            return base / "Character-design"
        elif "board" in file.name.lower():
            return base / "Finished-painting/Boards"
        elif mod_time < thresh_time:
            # Old files go to backups
            return base / "Finished-painting/Back-ups"
        else:
            return base / "Finished-painting"

    # --------------------------
    # VIDEO FILES (TIMELAPSES)
    # --------------------------
    elif file.suffix == ".mp4":
        return base / "Timelaps"

    # Fallback (should rarely happen)
    return base

# --------------------------------------------------
# SAFE FILE MOVE FUNCTION
# --------------------------------------------------
def move_file_safely(file: Path, base: Path, dry_run: bool = DRY_RUN):
    """
    Moves a file to its decided destination.
    - Creates folders if needed
    - Prevents overwriting by auto-renaming
    - Supports dry run mode
    """

    # Ignore anything that is not a file
    if not file.is_file():
        return

    # Determine destination folder
    destination = decide_destination(file, base)

    # Create destination folder if missing
    if not destination.exists():
        if dry_run:
            logging.info(f"[DRY RUN] Would create directory: {destination}")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {destination}")

    # Full destination path
    full_path = destination / file.name

    # Prevent overwriting by adding _1, _2, etc.
    counter = 1
    while full_path.exists():
        new_name = file.stem + "_" + str(counter) + file.suffix
        full_path = destination / new_name
        counter += 1

    # Perform or simulate move
    if dry_run:
        logging.info(f"[DRY RUN] Would move {file} -> {full_path}")
    else:
        file.rename(full_path)
        logging.info(f"file:{file.name} moved as {full_path.name} to {destination}")

# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":

    # Check base directory
    if BASE_DIR.exists():
        logging.info(f"Base directory found: {BASE_DIR}")
        setup_directories(BASE_DIR, FOLDERS)
    else:
        logging.error(f"Base directory does not exist: {BASE_DIR}")

    # Process only files directly inside BASE_DIR
    for file in BASE_DIR.iterdir():
        if file.is_file():
            move_file_safely(file, BASE_DIR, dry_run=DRY_RUN)
