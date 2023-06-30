import os

def generate_folder_structure(path, indent=''):
    tree = ''
    files = os.listdir(path)
    for file in files:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            tree += f"{indent}- {file}\n"
            tree += generate_folder_structure(filepath, indent + '  ')
        else:
            tree += f"{indent}- {file}\n"
    return tree

if __name__ == '__main__':
    root_path = os.getcwd()
    folder_structure = generate_folder_structure(root_path)
    with open('folder_structure.md', 'w') as file:
        file.write(folder_structure)
