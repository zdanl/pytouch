#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import os.path
import argparse
import pytouch

# make this pytouch.engine.crypto, etc.
from pytouch.engine import TemplateEngine, CryptoEngine
from pytouch.engine import CompressionEngine

def main():
    
    tmpl_eng = TemplateEngine()
    
    print("Chosen template engine: %s" %argv.template)

    # Calibrate Template Engine with Argparse
    for k, v in argv.__dict__.items():
        arg = tmpl_eng.delimiter.start + "PROJECT_%s" %k.upper()
        arg += tmpl_eng.delimiter.end
        if arg in tmpl_eng.substitute_values.keys():
            tmpl_eng.substitute_values[arg] = v

    # Initialize Boilerplate or Custom Template
    code = tmpl_eng.initialize(template=argv.template)
    if code == 1:
        print("Something went wrong with the Template Engine.")
        sys.exit(1)

    # Template engine will do everything for us.
    tmpl_eng.run()
    print("Your project was created.")

if __name__ == "__main__":
    prse = argparse.ArgumentParser(description="Manage Python3 projects")
    prse.add_argument("name", help="This is the name of everything")
    
    prse.add_argument("--license", help="Something like GPL or MIT")
    prse.add_argument("--author", help="Author of the project")
    prse.add_argument("--version", help="Version number or string")
    prse.add_argument("--descr", help="Describe the project")

    prse.add_argument("-template", default="boilerplate", help="Proj tmplate")

    argv = prse.parse_args()
    if os.path.exists(argv.name):
        print("It seems like %s exists. May I delete?" %argv.name)
        a = input("Delete %s [y/n] >> " %argv.name)
        if (a.lower().startswith("y")):
            os.system("rm -rf %s" %argv.name)
        else:
            print("Not deleting. Choose a different name.")
            sys.exit(1)
    main()
