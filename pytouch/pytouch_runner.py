#!/usr/bin/env python3

import sys
import os.path

from pytouch.defaults import source_tmpl

def main():
    global source_tmpl

    # t is target
    with open(sys.argv[1], "w") as t:
        t.write(source_tmpl)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: pytouch [target_filepath]")
