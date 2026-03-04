# Walks through directories and gathers raw data.
#
# What id does:
#
# - Walks through the directories and gathers raw data.
# - Applies ignore rules.
# - Collect file sizes and paths.
# - Detect duplicate files (optional).
# - Count extensions.

from pathlib import Path
from collections import Counter


# Directories and files to ignore by default.
DEFAULT_IGNORE_PATTERNS = {
    ".git", ".hg", ".svn",              # Version control directories
    "node_modules", "venv", "env",      # Dependencies and virtual environments
    "__pycache__",  ".pytest_cache",    # Python cache directories
    "build", "dist",                    # Build and distribution directories
    ".DS_Store", "Thumbs.db",           # OS metadata files
}


def scan_directory(path, ignore_pattern):

    '''
    Walks the folder and filters ignored paths.
    Gathers file info and returns the collected data.
    '''

    root_directory = Path(path)


def should_ignore(path, ignore_patterns):

    '''
    Checks if a path matches ignore rules.
    It supports built-in ignores + user patterns.
    '''

    pass


def collect_file_info(file_path):

    '''
    Collects file information such as size and extension.
    Returns a dictionary with the collected data.
    '''

    pass


def summarize_extensions(files):

    '''
    Summarizes file extensions and their counts.
    Returns the most common extensions.
    '''

    pass


def find_largest_files(files, limit=10):

    '''
    Finds the largest files in the collected data.
    Returns a list of the largest files up to the specified limit.
    '''

    pass


def calculate_total_size(files):

    '''
    Calculates the total size of all collected files.
    Returns the total size.
    '''

    pass
