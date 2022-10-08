#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __________         ___________                     .__      
# \______   \ ___.__.\__    ___/____   __ __   ____  |  |__   
# |     ___/<   |  |  |    |  /  _ \ |  |  \_/ ___\ |  |  \  
# |    |     \___  |  |    | (  <_> )|  |  /\  \___ |   Y  \ 
# |____|     / ____|  |____|  \____/ |____/  \___  >|___|  / 
#       .    \/ Twitter @dzethoxy, Github: @zdanl\/ v0.1 \/
#

# system & standard library imports
import sys, os
import yaml
import os.path
import platform
import argparse

# import the framework
import pytouch

def main():
    parse = argparse.ArgumentParser(description="Manage Python3 projects")

    sub_parse = parse.add_subparsers(help='commands', dest="command")

    ### -Create- subparser ###
    create_parse = sub_parse.add_parser("create", help="Create a Project")
    create_parse.add_argument("name", help="This is the project name")
    create_parse.add_argument("--license", default="GPL", help="Something like GPL or MIT")
    create_parse.add_argument("--author", default="John Snow", help="Author of the project")
    create_parse.add_argument("--version", default="0.1", help="Version number or string")
    create_parse.add_argument("--descr", default="Sample Description", help="Describe the project")
    create_parse.add_argument("--email", default="email@email.me", help="Author Email Address")
    create_parse.add_argument("-template", "-tmpl", "-t", default="appy",
                              help="Proj tmplate")


    ### -Identity- subparser ###
    identity_parse = sub_parse.add_parser("identity", help="Manage identity")
    identity_parse.add_argument("-name", default="John Snow", help="Your name")
    identity_parse.add_argument("-email", default="email@email.me", help="Email")
    identity_parse.add_argument("-company", default="Corp.", help="Company")
    identity_parse.add_argument("-pgp", default="1:2", help="PGP Fingerprint")
    
    ### -Destroy- subparser ###
    identity_parse = sub_parse.add_parser("destroy", help="Manage identity")
    identity_parse.add_argument("name", help="Your project name")

    ### -Crypt- subparser ###
    crypt_parse = sub_parse.add_parser("crypt", help="En-/Decrypt a project")
    crypt_parse.add_argument("name", default="Project name", help="Project name")

    ### -Zip- subparser ###
    crypt_parse = sub_parse.add_parser("zip", help="De-/Compress a project")
    crypt_parse.add_argument("name", default="Project name", help="Project name")
    
    ### -Build- subparser ###
    crypt_parse = sub_parse.add_parser("build", help="Build a project")
    crypt_parse.add_argument("name", help="Project name")

    # resolved Windows 11 compatability
    command = "clear"
    if platform.system() == "Windows":
        command = "cls"
    os.system(command)
    print(pytouch.ascii.banner)

    PyTouch.Argv = parse.parse_args()
    PyTouch.RunMode = PyTouch.Argv.command

    if PyTouch.RunMode == "create":
        main_create()
    elif PyTouch.RunMode == "destroy":
        main_destroy()
    elif PyTouch.RunMode == "build":
        main_build()
    elif PyTouch.RunMode == "crypt":
        main_crypt()
    elif PyTouch.RunMode == "zip":
        main_zip()
    elif PyTouch.RunMode == "identity":
        main_identity()
    else:
        parse.print_help()

def main_identity():
    # TODO find a better way to do this.
    print(PyTouch.Config)
    if PyTouch.Argv.name:
        PyTouch.Config["identity"]["name"] = PyTouch.Argv.name
    elif PyTouch.Argv.email:
        PyTouch.Config.identity["email"] = PyTouch.Argv.email
    elif PyTouch.Argv.company:
        PyTouch.Config.identity["company"] = PyTouch.Argv.company
    elif PyTouch.Argv.pgp:
        PyTouch.Config.identity["pgp"] = PyTouch.Argv.pgp
    write_config()


def main_destroy():
    p = PyTouch.Argv.name
    if os.path.exists(p) and os.path.exists(p + "/.pytouch.yaml"):
        os.system("rm -rf %s" %p)
        print("Deleted project.")
    else:
        print("Project does not exist or is not a PyTouch project.")
        sys.exit(1)

def main_zip():
    pass

def main_crypt():
    pass

def main_build():
    pass

def main_create():
    argv = PyTouch.Argv

    if os.path.exists(PyTouch.Argv.name):
        print("It seems like %s exists. May I delete?" %argv.name)
        a = input("Delete %s [y/n] >> " %argv.name)
        if (a.lower().startswith("y")):
            os.system("rm -rf %s" %argv.name)
        else:
            print("Not deleting. Choose a different name.")
            sys.exit(1)
    
    tmpl_eng = pytouch.engine.template()
    
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
    code = tmpl_eng.run()

    # Check if it worked.
    if code != 0:
        print("Something went wrong. Project probably not created.")
    else:
        print("Your project [%s] was created." %argv.name)

    return code

def write_config():
    with open(PyTouch.Home + "/.pytouch.yaml", 'w') as f:
        yaml.dump(PyTouch.Config, f)
    print("Config written.")
        
def load_config():
    # reads yaml file and returns object()  not dict()
    path = PyTouch.Home + "/.pytouch.yaml"
    if not os.path.exists(path):
        print("No PyTouch config file found.")
        with open(path, 'w') as file:
            file.write("---")
    else:
        with open(path, 'r') as file:
            PyTouch.Config = yaml.safe_load(file)
            print("Config:")
            print(PyTouch.Config)

if __name__ == "__main__":
    PyTouch = pytouch.tricks.ov({
        "RunMode": None,
        "Argv": None,
        "Config": None,
        "Home": os.path.expanduser("~")
    })

    load_config()
    main()
