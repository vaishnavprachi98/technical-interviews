"""
@author: David Lei
@since: 11/08/2017

Use to help enforce PEP8 naming standards for files and directories.
"""
import os
import subprocess

files_to_ignore = {
    "LICENSE", ".gitignore", "README.md", "misc", ".", "..", ".DS_Store", ".git", ".idea",
    "standards.py", "__init__.py", "__pycache__"
}


def standardize_dir(current_dir, is_tracked_by_git):
    """Recursively traverse a directory to rename all it's files to lower case, then finally rename it as lowercase.
    If a file is a directory will call itself again on that directory.

    Uses subprocess.check_call to wait for the git mv to complete to make sure only one path is being affected at a time.

    :param current_dir: current directory to change to lower case
    """
    for filename in os.listdir(current_dir):
        # Rename all files in directory to lower case.
        if filename in files_to_ignore:
            continue
        file_path = os.path.join(current_dir, filename)
        if os.path.isdir(file_path):
            standardize_dir(file_path, is_tracked_by_git)
        else:
            if is_tracked_by_git:
                subprocess.check_call('git mv {0} {1}'.format(file_path, os.path.join(current_dir, filename.lower())))
            else:
                os.rename(file_path, os.path.join(current_dir, filename.lower()))

    # Rename directory.
    if is_tracked_by_git:
        subprocess.check_call('git mv {0} {1}'.format(current_dir, current_dir.lower()))
    else:
        os.rename(current_dir, current_dir.lower())

standardize_dir(os.getcwd(), is_tracked_by_git=True)


