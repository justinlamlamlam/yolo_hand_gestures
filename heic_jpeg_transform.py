import os
from PIL import Image
import pyheif

def convert_heic_to_jpeg(heic_path, jpeg_path):
    """Convert a single HEIC file to JPEG format."""
    heif_file = pyheif.read(heic_path)
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
    image.save(jpeg_path, "JPEG")
    print(f"Converted: {heic_path} -> {jpeg_path}")

def process_directory(directory):
    """Recursively find and convert all HEIC files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".heic"):
                heic_path = os.path.join(root, file)
                jpeg_path = os.path.splitext(heic_path)[0] + ".jpg"
                convert_heic_to_jpeg(heic_path, jpeg_path)

                import os

def remove_whitespaces_in_path(directory):
    """Recursively renames files and directories by removing whitespaces."""
    for root, dirs, files in os.walk(directory, topdown=False):  # Bottom-up to avoid path conflicts
        # Rename files
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = filename.replace(" ", "").replace("\t", "").replace("\n", "")
            new_path = os.path.join(root, new_filename)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f'Renamed File: "{old_path}" -> "{new_path}"')
                except Exception as e:
                    print(f'Error renaming file "{old_path}": {e}')

        # Rename directories
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            new_dirname = dirname.replace(" ", "").replace("\t", "").replace("\n", "")
            new_dir_path = os.path.join(root, new_dirname)

            if old_dir_path != new_dir_path:
                try:
                    os.rename(old_dir_path, new_dir_path)
                    print(f'Renamed Directory: "{old_dir_path}" -> "{new_dir_path}"')
                except Exception as e:
                    print(f'Error renaming directory "{old_dir_path}": {e}')

def remove_parentheses_in_path(directory):
    """Recursively renames files and directories by removing '(' and ')' from their names."""
    for root, dirs, files in os.walk(directory, topdown=False):  # Bottom-up to avoid path conflicts
        # Rename files
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = filename.replace("(", "").replace(")", "")
            new_path = os.path.join(root, new_filename)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f'Renamed File: "{old_path}" -> "{new_path}"')
                except Exception as e:
                    print(f'Error renaming file "{old_path}": {e}')

        # Rename directories
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            new_dirname = dirname.replace("(", "").replace(")", "")
            new_dir_path = os.path.join(root, new_dirname)

            if old_dir_path != new_dir_path:
                try:
                    os.rename(old_dir_path, new_dir_path)
                    print(f'Renamed Directory: "{old_dir_path}" -> "{new_dir_path}"')
                except Exception as e:
                    print(f'Error renaming directory "{old_dir_path}": {e}')
def remove_heic_files(directory):
    """Recursively removes all .heic files in the given directory."""
    for root, _, files in os.walk(directory, topdown=False):  # Bottom-up to avoid issues while deleting
        for filename in files:
            if filename.lower().endswith(".heic"):  # Check for .heic extension (case-insensitive)
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def remove_non_jpg(directory: str):
    """
    Recursively removes all files that are not JPG from the specified directory.
    :param directory: Path to the directory to clean up.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.lower().endswith(".jpg"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")


if __name__ == "__main__":
    current_directory = os.getcwd()  # Get current working directory
    remove_non_jpg("./azuran")
    # remove_heic_files(current_directory)
    # print("HEIC file removal completed!")
    # remove_parentheses_in_path(current_directory)
    # print("Renaming completed!")
    # remove_whitespaces_in_path(current_directory)
    # print("Renaming completed!")
    """
    input_directory = "./leon/"
    process_directory(input_directory)
    print("Conversion completed!")
    """