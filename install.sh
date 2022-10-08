#!/bin/bash

clear;

python3 -c "from pytouch import ascii; print(ascii.banner)";

# Cleanup developer taint
find . -name __pycache__ -type d;

# Install Python3 Module
pip3 install .;

# Compile Python3 module
nuitka3 pytouch.py;
mv pytouch.bin /usr/bin/pytouch;
rm -rf pytouch.build;

cd ..

# Compute Target Path
target_path=$(python3 -c "import pytouch; print(pytouch.__file__)" | sed "s/__init__.py//");
echo "Target path $target_path";

# Create directory not installed by pip3
target_path="$target_path/static_templates";

# Move 
cp -r pytouch/pytouch/static_templates/fraimwork $target_path;
cp -r pytouch/pytouch/static_templates/appy $target_path;

echo "Installed.";
