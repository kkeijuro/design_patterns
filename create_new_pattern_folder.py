#!/usr/bin/python
import os
import sys

def send_message(message):
    print message
    
def folder_pattern_exists(file_path):
    directory = os.path.dirname(file_path)
    try:
        os.stat(directory)
    except:
        return True
    return False       

_PYTHON = "python"
_C = "c++"
_JAVA = "java"

_LANGUAGE_AVAILABLE = [_PYTHON, _C, _JAVA]

def create_pattern_folder(pattern_folder):
    os.mkdir(pattern_folder)
    for language in _LANGUAGE_AVAILABLE:
        f = os.path.join(pattern_folder, language)
        os.mkdir(f)
        
if __name__ == "__main__":
    if len(sys.argv) != 2: raise Exception("Not Valid arguments")
    pattern_name = sys.argv[1]
    f = os.path.join("./", pattern_name)
    if not folder_pattern_exists(f):
        create_pattern_folder(f)
        send_message("Pattern folder: {0} created".format(pattern_name))
    else: raise Exception("Pattern folder almost created")