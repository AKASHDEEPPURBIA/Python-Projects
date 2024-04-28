import os
# The os module provides a way to interact with the operating system.
# It offers functions for tasks such as file and directory operations
# , environment variables, process management, and more.

import requests

def get_extension(image_url: str) -> str | None:
    # Create a list of popular extensions
    extension_list: list[str] = ['.jpg', '.png', '.jpeg', '.svg', '.gif']

    #Check the extensions exists in the URL or not
    for ext in extension_list:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder: str = None):
    #Download the image from any URL

    #Attempt to get the correct image extension from URL
    if ext:= get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image Extension could not be located')

    #check if the name already exists:
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')
    # The purpose of this code snippet is to prevent overwriting existing files with the same name.
    # It's a common practice to check if a file already exists before performing operations that
    # could potentially overwrite it, such as creating or saving a new file.
    # If the file already exists, it alerts the user by raising an exception.

    #Download the image

    try:
        # Get the image as bytes and writes it locally to the computer
        image_content: bytes = requests.get(image_url).content
        # getting binary content using content attrubte with http get request

        #open the image_name file in binary write mode as handler and close it
        with open(image_name, 'wb') as handler:
            handler.write(image_content) # copying the binary content to the handler
            print(f'Downloaded: {image_name} Successfully')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_url: str = input('Enter a image URL: ')
    input_name: str = input('Enter a name for your image: ')

    download_image(input_url, input_name, 'Imagess')



