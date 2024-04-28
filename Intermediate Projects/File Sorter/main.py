import os
#provides a portable way of using operating system-dependent functionality.
import shutil
# offers a higher-level interface for file operations such as
# copying and removing files and directories.
import tkinter as tk
from tkinter import filedialog #provides dialogs for opening and saving files and directories.

def select_folder():
    """Open a file dialog to select a folder"""
    root = tk.Tk() #It creates a Tkinter Tk object, which represents the main window of the application.
    root.withdraw()  # Hide the main window
    #as we don't actually need to show it since we're only using the file dialog.

    #This line uses the askdirectory method from the filedialog
    # module to open a dialog window for selecting a directory.
    folder_path = filedialog.askdirectory(title="Select Folder to Sort")

    if folder_path:
        sort_files(folder_path)
        remove_empty_folders(folder_path)
        print('Files sorted successfully!')
    else:
        print('No folder selected.')
def create_folder(path: str, extension: str) -> str:
    """Creates a folder that names after the extension of the folder"""
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)
    # It constructs a new pathname by concatenating path
    # and folder_name with the appropriate separator based on the operating system.

    #if the folder_path doesn't exists then create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #return the folder_path
    return folder_path

def sort_files(source_path: str):
    """Sort file based on a given path"""

    #Recursively walkthrough the all directories and files in the source path
    for root_dir, sub_dir, filenames in os.walk(source_path):
        # The os.walk() function generates the file names in a directory tree
        # by walking the tree either top-down or bottom-up.
        # It returns a tuple (root, dirs, files) where root is the current directory being looked at,
        # dirs is a list of subdirectories in root, and files is a list of files in root.
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                targer_folder: str = create_folder(source_path, extension)

                #create a path that leads to a target folder
                target_path: str = os.path.join(targer_folder, filename)

                #move the file from its current location to its target location
                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str):
    """Removes all empty folders"""
    # We will walk through all folders again but this time in bottom-up(files->subdir->root) approach
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        #create a folder_path for each dir
        for current_dir in sub_dir:
            folder_path = create_folder(root_dir, current_dir)

            #check if the folder is empty, if yes then remove the folder
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    user_choice = input('Do you want to sort a folder using GUI? (yes/no): ')

    if user_choice.lower() == 'yes':
        select_folder()
    else:
        user_input = input('Please provide a file path to sort: ')

        if os.path.exists(user_input):
            sort_files(user_input)
            remove_empty_folders(user_input)
            print('Files sorted successfully!')
        else:
            print('Invalid path, please provide a valid file path.')


if __name__ == '__main__':
    main()


