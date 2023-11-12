import os
import re
import shutil

def move_dj_mixes(source_folder, destination_folder, size_threshold=100 * 1024 * 1024, delete_after_move=False):
    """
    Search and move DJ mixes from a source folder to a destination folder.
    Optionally delete the source file after a successful move.

    :param source_folder: Path to the source folder.
    :param destination_folder: Path to the destination folder where mixes will be moved.
    :param size_threshold: File size threshold in bytes to consider as a mix.
    :param delete_after_move: Flag to delete the source file after a successful move.
    :return: List of files that were moved.
    """
    dj_mix_patterns = re.compile(r'(full\s+mix|cd[-\s]?\d+|disc[-\s]?\d+|continuous\s+mix|live\s+set)', re.IGNORECASE)
    moved_mixes = []

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.mp3'):
                source_path = os.path.join(root, file)
                file_size = os.path.getsize(source_path)

                # Check if the file size is above the threshold and the name matches the patterns
                if file_size > size_threshold and dj_mix_patterns.search(file):
                    destination_path = os.path.join(destination_folder, file)
                    shutil.move(source_path, destination_path)

                    # If delete flag is on, check if the move was successful before deleting
                    if delete_after_move and os.path.exists(source_path) and os.path.exists(destination_path) and os.path.getsize(destination_path) == file_size:
                        os.remove(source_path)
                    moved_mixes.append(destination_path)

    return moved_mixes

# Example usage:
# source_folder = '/path/to/your/music/library'
# destination_folder = '/path/to/destination/folder'
# moved_files = move_dj_mixes(source_folder, destination_folder, delete_after_move=True)
# for file in moved_files:
#     print(f"Moved: {file}")
