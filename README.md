# File organizer

This Python script organizes files in a specified directory into folders based on their file types. It helps users clean up and organize directories by categorizing files into predefined folders (e.g., text, images, videos, etc.). The script also allows users to customize the file types they want to organize and delete shortcut files (`.lnk`).

## Features

- Organizes files into folders based on their types (e.g., text, images, videos, etc.).
- Option to display all available file types for organizing.
- Option to choose specific file types and folders for organization.
- Deletes all shortcuts (`.lnk` files) from the directory if specified.

## Requirements

- Python 3.10 or newer

## How to Use

### Installation

- Make sure you have Python installed by checking the version:
  ```bash
  python --version

- Clone this repository and navigate to the directory:
  ```bash
  git clone https://github.com/ssambss/FileOrganizer.git
  cd <repo_folder>

- The script can be run from the command line with several options for customization:
  ```bash
  python cleaner.py [OPTIONS]

## Options
- --root_dir: Path to the directory to clean. If not specified, the current working directory is used.
- --show_file_types: Displays all available file types and their corresponding folder categories.
- --choose_file_types: Choose specific folders and file types to organize. Provide space-separated values (e.g., text pdf image).
- --delete_shortcuts: Deletes all .lnk files (Windows shortcuts) from the directory.

### Examples

- Clean the current working directory:
  ```bash
  python cleaner.py

- Clean a specific directory:
  ```bash
  python cleaner.py --root_dir /path/to/directory

- Display all available file types:
  ```bash
  python cleaner.py --show_file_types

- Organize only specific file types (e.g., text, pdf, image):
  ```bash
  python cleaner.py --choose_file_types text pdf image

- Clean the directory and delete all shortcuts:
  ```bash
  python cleaner.py --delete_shortcuts

## File Types

Below are the default file types the script categorizes into folders:

- **text**: `.txt`, `.doc`, `.docx`
- **pdf**: `.pdf`
- **image**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **video**: `.mp4`, `.avi`, `.mkv`, `.mov`
- **audio**: `.mp3`, `.wav`, `.flac`
- **compressed**: `.zip`, `.rar`, `.7z`
- **executable**: `.exe`, `.msi`, `.bat`, `.ps1`
- **presentation**: `.ppt`, `.pptx`, `.key`
- **spreadsheet**: `.ods`, `.xls`, `.xlsx`, `.csv`
- **programming**: `.py`
