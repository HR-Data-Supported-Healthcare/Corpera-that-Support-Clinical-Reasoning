import os

def init_source_dest_dirs(src_dir: str, dest_dir: str) -> None:
    """
    Checks whether the source and destination folders exist in the project.
    If not, creates empty folders.

    Args:
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.

    Returns:
        None
    """
    source_dir_exists = os.path.isdir(src_dir)
    if not source_dir_exists:
        os.makedirs(src_dir)
        print("[INIT] Created empty source directory")

    dest_dir_exists = os.path.isdir(dest_dir)
    if not dest_dir_exists:
        os.makedirs(dest_dir)
        print("[INIT] Created empty destination directory")
