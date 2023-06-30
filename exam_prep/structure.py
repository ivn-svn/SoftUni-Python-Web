import os


def get_folder_structure(path):
    folder_structure = {}

    for root, dirs, files in os.walk(path):
        # Exclude hidden folders (those starting with a dot)
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Exclude specific folders
        exclude_folders = ['venv', '.idea', 'vendor', '__pycache__']
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        # Exclude hidden files (those starting with a dot)
        files = [f for f in files if not f.startswith('.')]

        current_dir = root.replace(path, '')
        subfolders = current_dir.split(os.sep)[1:]

        parent = folder_structure
        for folder in subfolders:
            parent = parent.setdefault(folder, {})

        parent.update({file: None for file in files})

    return folder_structure


# Provide the path to your Django project's root folder
project_path = r'C:\Users\ivsve\PycharmProjects\SoftUni-Python-Web\exam_prep'

# Get the folder structure
structure = get_folder_structure(project_path)

# Print the folder structure
import json

print(json.dumps(structure, indent=4))
