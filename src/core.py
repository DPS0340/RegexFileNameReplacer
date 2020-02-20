import re
import mimetypes
from os.path import exists, normpath
import os

def matchRegex(filename, regex):
    result = re.search(filename, regex)
    return result != None
    
def rename(filename, directory, newname):
    os.rename(f"{directory}/{filename}", f"{directory}/{newname}")


def run(filename, directory, regex, replaceKeyword):
    if not (filename and directory and regex and replaceKeyword):
        print("invalid arguments")
        return
    
    isMatched = matchRegex(filename, regex)

    if isMatched:
        print(f"match find!\nfilename: {filename}")
        newname = re.sub(regex, replaceKeyword, filename)
        rename(filename, directory, newname)
        return True
    else:
        return False
