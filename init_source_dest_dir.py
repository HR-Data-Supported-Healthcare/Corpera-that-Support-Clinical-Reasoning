import os

def init_source_dest_dirs(src_dir: str, dest_dir: str) -> None:
    """Checks whether the source and destination folders exist in the project. 
    If not, then this function creates empty folders"""
    source_dir_exists = os.path.isdir(src_dir)
    if not source_dir_exists:
        os.makedirs(src_dir)
        print("[INIT] Created empty source directory")

    dest_dir_exists = os.path.isdir(dest_dir)
    if not dest_dir_exists:
        os.makedirs(dest_dir)
        print("[INIT] Created empty destination directory")
