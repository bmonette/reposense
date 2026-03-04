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


def scan_directory(path, ignore_pattern=None):

    '''
    Walks the folder and filters ignored paths.
    Gathers file info and returns the collected data.

    Returns a list of file-info dicts (see collect_file_info).
    '''

    root_directory = Path(path)

    if not root_directory.exists():
        raise FileNotFoundError(f"Path '{path}' does not exist.")

    if not root_directory.is_dir():
        raise NotADirectoryError(f"Path '{path}' is not a directory.")

    files = []

    for item in root_directory.rglob("*"):
        if not item.is_file():
            continue

        if should_ignore(item, ignore_patterns):
            continue

        files.append(collect_file_info(item))

    return files


def should_ignore(path, ignore_patterns):

    '''
    Checks if a path matches ignore rules.
    It supports built-in ignores + user-supplied patterns.

    A path is ignored if any part of it matches an ignore pattern
    in the combined set of default and user-supplied patterns.
    '''

    combined = set(DEFAULT_IGNORE_PATTERNS)

    if ignore_patterns:
        # Normalise: accept Path object or plain strings.
        combined.update(str(p) for p in ignore_patterns)

    path = Path(path)

    # Check every component of the path (handles nested ignored dirs)
    for part in path.parts:
        if part in combined:
            return True

    # Also check by suffix so callers can pass (e.g. "*.log, ".pyc")
    if path.suffix in combined:
        return True


def collect_file_info(file_path):
    """
    Collects file information such as size and extension.
    Returns a dictionary with the collected data.

    Keys:
        path      - absolute Path object
        name      - filename string
        extension - lowercase extension including dot, e.g. '.py'
        size      - size in bytes (int)
    """

    file_path = Path(file_path)

    return {
        "path": file_path.resolve(),
        "name": file_path.name,
        "extension": file_path.suffix.lower(),
        "size": file_path.stat().st_size,
    }


def summarize_extensions(files):

    '''
    Summarizes file extensions and their counts.
    Returns the most common extensions.
    '''

    counter = Counter(f["extension"] or "" for f in files)
    return counter.most_common


def find_largest_files(files, limit=10):

    '''
    Finds the largest files in the collected data.
    Returns a list of the largest files up to the specified limit.
    '''

    return sorted(files, key=lambda f: f["size"], reverse=True)[:limit]


def calculate_total_size(files):

    '''
    Calculates the total size of all collected files.
    Returns the total size.
    '''

    pass
