"""
@author: David Lei
@since: 11/08/2017

Use to help enforce PEP8 naming standards for files and directories.
"""
import os

files_to_ignore = {
    "LICENSE", ".gitignore", "README.md", "misc", ".", "..", ".DS_Store", ".git", ".idea",
    "standards.py", "__init__.py", "__pycache__"
}


def standardize_dir(current_dir):
    """Recursively traverse a directory to rename all it's files to lower case, then finally rename it as lowercase.
    If a file is a directory will call itself again on that directory.

    :param current_dir: current directory to change to lower case
    """
    for filename in os.listdir(current_dir):
        # Rename all files in directory to lower case.
        if filename in files_to_ignore:
            continue
        file_path = os.path.join(current_dir, filename)
        if os.path.isdir(file_path):
            standardize_dir(file_path)
        else:
            os.rename(file_path, os.path.join(current_dir, filename.lower()))
    # Rename directory.
    os.rename(current_dir, current_dir.lower())

standardize_dir(os.getcwd())


