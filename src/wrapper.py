import sys
from os import listdir
from os.path import dirname, basename, exists, isdir, abspath
import re
import core
import argparse


def search(paths, regex, replace_keyword, appendMode):
    for fp in paths:
        fp = abspath(fp)
        print(f'found {basename(fp)}')
        if isdir(fp):
            print("it's directory, doing recursive search\n\n")
            search([abspath(fp+"/"+e) for e in listdir(fp)], regex, replace_keyword, appendMode)
            continue
        parent = dirname(fp)
        filename = basename(fp)
        print("\n\n", end="")
        res = core.run(filename, parent, regex, replace_keyword, appendMode)
        if res is False:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str)
    parser.add_argument('regex', type=str)
    parser.add_argument('replace_keyword', type=str)
    parser.add_argument('--append', type=bool, default=False)
    args = parser.parse_args()
    file_path = args.file_path
    regex = args.regex
    replace_keyword = args.replace_keyword
    print(file_path)
    search([file_path], regex, replace_keyword, args.append)


if __name__ == "__main__":
    main()
