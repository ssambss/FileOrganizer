from pathlib import Path
import argparse
import sys

argparser = argparse.ArgumentParser(description='Clean a directory by organizing files into folders based on their types')
argparser.add_argument('--root_dir', type=str, help='Path to the directory to clean. Default is the current working directory')
argparser.add_argument('--show_file_types', action='store_true', help='Types of folders and files to organize')
argparser.add_argument('--choose_file_types', type=str, nargs='+', help='Choose specific folders and filetypes to organize. Default is all.')
argparser.add_argument('--delete_shortcuts', action='store_true', help='Delete all shortcuts in the directory.')

def choose_root_dir():

    if args.root_dir:
        root_dir = Path(args.root_dir)
    else:
        root_dir = Path.cwd()

    print(f"\nCleaning directory: {root_dir} \n")

    return root_dir  


def choose_file_types():

    fileTypes = {
    'text': ['.txt', '.doc', '.docx'],
    'pdf': ['.pdf'],
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'video': ['.mp4', '.avi', '.mkv', '.mov'],
    'audio': ['.mp3', '.wav', '.flac'],
    'compressed': ['.zip', '.rar', '.7z'],
    'executable': ['.exe', '.msi', '.bat', '.ps1'],
    'presentation': ['.ppt', '.pptx', '.key'],
    'spreadsheet': ['.ods', '.xls', '.xlsx', '.csv'],
    'database': ['.db', '.sql'],
    'web': ['.html', '.css', '.js'],
    'programming': ['.py', '.java', '.c', '.cpp', '.h', '.hpp', ''],
    'system': ['.dll', '.sys', '.ini', '.json', '.xml', '.log', '.bak', '.tmp']
    }

    if args.show_file_types:
        show_file_types(fileTypes)
        sys.exit()
        

    if args.choose_file_types:
        fileTypes = {key: value for key, value in fileTypes.items() if key in args.choose_file_types}

    print(f'Chosen folders and file types: \n')
    [print(f"{key}: {value}") for key, value in fileTypes.items()]

    return fileTypes

def show_file_types(fileTypes):
    
    print('Types of folders and files to choose from: \n')
    [print(f"{key}: {value}") for key, value in fileTypes.items()]


def create_folders():

    [(root_dir / folder).mkdir() for folder in fileTypes.keys() if not (root_dir / folder).exists()]


def organize_files():

    for file in root_dir.glob('*'):
        if file.is_file():
            for key, value in fileTypes.items():
                if file.suffix in value:
                    file.rename(root_dir / key / file.name)
                    break

        if args.delete_shortcuts:
            if file.suffix == '.lnk':
                file.unlink()

args = argparser.parse_args()
fileTypes = choose_file_types()
root_dir = choose_root_dir()
create_folders()
organize_files()


