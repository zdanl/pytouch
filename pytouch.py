#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import os.path
import argparse

from pytouch.template_engine import TemplateEngine

import pytouch

def main():
    
    tmpl_eng = TemplateEngine()
    
    # Calibrate Template Engine
    for k, v in argv.__dict__.items():
        arg = "PROJECT_%s" %k.upper()
        if arg in tmpl_eng.substitute_values.keys():
            tmpl_eng.substitute_values[arg] = v

    # Initialize Boilerplate or Custom Template
    tmpl_eng.initialize(template=argv.template)

if __name__ == "__main__":
    prse = argparse.ArgumentParser(description="Manage Python3 projects")
    prse.add_argument("name", help="This is the name of everything")
    
    prse.add_argument("--license", help="Something like GPL or MIT")
    prse.add_argument("--author", help="Author of the project")
    prse.add_argument("--version", help="Version number or string")
    prse.add_argument("--descr", help="Describe the project")

    prse.add_argument("-template", default="boilerplate", help="Proj tmplate")

    argv = prse.parse_args()
    main()
