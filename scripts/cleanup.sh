#!/bin/bash

find . -name "*.build" -type d -delete;
find . -name "__pycache__" -type d -delete;
find . -name "*.egg" -type d -delete;

rm -rf *.build;
rm -rf *.egg*;
py3clean .;
