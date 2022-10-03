#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import os.path

from pytouch.template_engine import TemplateEngine

def main():
    project_name = sys.argv[1]
    tmpl_eng = TemplateEngine(name=project_name)
    print(tmpl_eng.substitute_values)
   

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: pytouch [target_filepath]")
