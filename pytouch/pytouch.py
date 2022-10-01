#!/usr/bin/env python3

import sys
import os.path

from pytouch.defaults import source_tmpl, default_file

def main():
    global source_tmpl, default_file

    # f is file
    if (os.path.exists(default_file)):
        f = open(default_file, "r")
        source_tmpl = f.read()
        f.close()

    # t is target
    with open(sys.argv[1], "w") as t:
        t.write(source_tmpl)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: pytouch [target_filepath]")
