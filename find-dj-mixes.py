import os
import re
import shutil

def move_dj_mixes(source_folder, destination_folder, size_threshold=100 * 1024 * 1024):
    """
    Search and move DJ mixes from a source folder to a destination folder.

    :param source_folder: Path to the source folder.
    :param destination_folder: Path to the destination folder where mixes will be moved.
    :param size_threshold: File size threshold in bytes to consider as a mix.
    :return: List of files that were moved.
    """
    dj_mix_patterns = re.compile(r'(full\s+mix|cd[-\s]?\d+|disc[-\s]?\d+|continuous\s+mix|live\s+set)', re.IGNORECASE)
    moved_mixes = []

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                # Check if the file size is above the threshold and the name matches the patterns
                if file_size > size_threshold and dj_mix_patterns.search(file):
                    destination_path = os.path.join(destination_folder, file)
                    shutil.move(file_path, destination_path)
                    moved_mixes.append(destination_path)

    return moved_mixes

# Example usage:
# source_folder = '/path/to/your/music/library'
# destination_folder = '/path/to/destination/folder'
# moved_files = move_dj_mixes(source_folder, destination_folder)
# for file in moved_files:
#     print(f"Moved: {file}")
