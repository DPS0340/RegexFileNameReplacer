import re
import mimetypes
from os.path import exists, normpath
import os

def matchRegex(filename, regex):
    result = re.search(filename, regex)
    return result
    
def rename(filename, directory, newname):
    os.rename(f"{directory}/{filename}", f"{directory}/{newname}")


def run(filename, directory, regex, replace_keyword, appendMode):
    if not (filename and directory and regex and replace_keyword):
        print("invalid arguments")
        return
    
    result = matchRegex(filename, regex)

    if result:
        print(f"match find!\nfilename: {filename}")
        if appendMode == False:
            newname = re.sub(regex, replace_keyword, filename)
        else:
            newname = re.sub(regex, replace_keyword, filename) % result.group(0)
        rename(filename, directory, newname)
        return True
    else:
        return False
