import re
import mimetypes
from os.path import exists, normpath
import os

def matchRegex(filename, regex):
    result = re.search(regex, filename)
    return result
    
def rename(filename, directory, newname):
    print(f"{directory}/{filename}")
    print(f"{directory}/{newname}")
    if exists(f"{directory}/{filename}") and not exists(f"{directory}/{newname}"):
        print(f"rename {filename} to {newname}")
        os.rename(f"{directory}/{filename}", f"{directory}/{newname}")
    else:
        print("newname exists!")


def run(filename, directory, regex, replace_keyword, appendMode):
    if not (filename and directory and regex and replace_keyword):
        print("invalid arguments")
        return
    
    result = matchRegex(filename, regex)

    if result:
        print(f"match find!\nfilename: {filename}")
        print(f"{result.group(0)}")
        if appendMode == False:
            newname = replace_keyword
        else:
            newname = replace_keyword % result.group(0)
        rename(filename, directory, newname)
        return True
    else:
        return False
