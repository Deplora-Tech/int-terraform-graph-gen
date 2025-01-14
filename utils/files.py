from typing import List, Dict
import os
import requests
from dotenv import load_dotenv


def openfile(filename, mode):
    try:
        return open(filename, mode)
    except IOError as e:
        print("Error: can't open file: %s" % filename)
        print(e)

def readfile(filename):
    try:
        file = openfile(filename, 'r+').readlines()
        return file
    except IOError as e:
        print("Error: can't read file: %s" % filename)
        print(e)

def writefile(filename, text):
    try:
        openfile(filename, 'w').write(text)
    except IOError as e:
        print("Error: can't write file: %s" % filename)
        print(e)

def is_terraform(file: str):
    if file.endswith('.tf') or file.endswith('.tf.json') or file.endswith('.tfvars') or file.endswith('.tfvars.json'):
        return True
    return False

def writefiles(path: str, file_objects: Dict[str, str]):
    try:
        for key in file_objects.keys():
            if is_terraform(key):
                print("key", key)
                file_path = os.path.join(path, key.split('/')[-1])
                print("file_path", file_path)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with openfile(file_path, 'w') as f:
                    f.write(file_objects[key])
    except IOError as e:
        print(f'Error writing files: {e}')

def clear_terraform_files(path: str):
    try:
        for file in os.listdir(path):
            if is_terraform(file):
                os.remove(os.path.join(path, file))
    except IOError as e:
        print(f'Error clearing terraform files: {e}')

def closefile(file):
    try:
        file.close()
    except IOError as e:
        print("Error: can't close file: %s" % file)
        print(e)

def replace_terraform_file(filename):
    try:
        with openfile(filename, 'w') as file:
            file.write('terraform {\n')
            file.write('  required_providers {\n')
            file.write('    google = {\n')
            file.write('      source  = "hashicorp/google"\n')
            file.write('    }\n')
            file.write('    aws = {\n')
            file.write('      source  = "hashicorp/aws"\n')
            file.write('    }\n')
            file.write('    azurerm = {\n')
            file.write('      source  = "hashicorp/azurerm"\n')
            file.write('    }\n')
            file.write('  }\n')
            file.write('}\n')
        file.close()
    except IOError as e:
        print("Error: can't write file: %s" % filename)
        print(e)

def upload_image(path: str, session_id: str):
    load_dotenv()
    with open(path, "rb") as image_file:
        response = requests.post(
            f'{os.getenv('DEPLORA_URL')}/{session_id}',
            files={"file": image_file}
        )
    print(response.json())
    return response.json()