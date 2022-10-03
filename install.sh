#!/bin/bash

./cleanup.sh;
pip3 install .;
nuitka3 pytouch.py;
mv pytouch.bin /usr/bin/pytouch;
cd ..
cp -r pytouch/pytouch/boilerplate $(python3 -c "import pytouch; print(pytouch.__file__)" | sed "s/__init__.py//")

echo "Installed.";
