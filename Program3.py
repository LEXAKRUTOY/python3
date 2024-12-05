import os

def list_files_in_directory(directory_path):
    directory_path = os.listdir()
    return directory_path

print(list_files_in_directory('.'))