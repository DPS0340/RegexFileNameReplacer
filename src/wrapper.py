import sys
from os import listdir
from os.path import dirname, basename, exists, isdir, abspath, normpath
import re
import core
import argparse


def search(paths, regex, replaceKeyword):
    for fp in paths:
        fp = abspath(fp)
        print(f'found {basename(fp)}')
        if isdir(fp):
            print("it's directory, doing recursive search\n\n")
            search([abspath(fp+"/"+e) for e in listdir(fp)], regex, replaceKeyword)
            continue
        parent = dirname(fp)
        filename = basename(fp)
        print("\n\n", end="")
        res = core.run(filename, parent, regex, replaceKeyword)
        if res is False:
            pass

def main():
    file_path = sys.argv[1]
    regex = re.compile(sys.argv[2])
    replaceKeyword = sys.argv[3]
    print(file_path)
    search([file_path], regex, replaceKeyword)


if __name__ == "__main__":
    main()
