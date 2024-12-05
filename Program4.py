import os

def ensure_directory_exists(directory_path):
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)

print(ensure_directory_exists("Я родился"))
