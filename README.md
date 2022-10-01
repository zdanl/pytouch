README
======

Welcome to pytouch.

Description
===========
This is an utterly small but growing tool. It accelerates the process of
starting a project over and over again, or dealing with Python projects 
without an IDE in general. It creates a minimal python file for you. You
may also compress and encrypt entire projects.

Dependencies
============
(as root)
pip3 install sh nuitka

Installation
============
pip3 install . \
    && nuitka3 pytouch/pytouch_runner.py \
    && mv pytouch_runner.bin /usr/bin/pytouch;


