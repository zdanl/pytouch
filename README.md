PyTouch
=======

Welcome to pytouch.

Description
===========
This is an utterly small but growing tool. It accelerates the process of
starting a project, and managing it, or dealing with Python projects 
without an IDE in general. It creates a minimal python project for you. You
may also compress and encrypt entire projects. The type of sample project
it creates depends on a boilerplate template. There are internal ones that
we support and maintain, but you may also chose an external one.

Dependencies
============
pip3 install nuitka
pip3 install sh

Installation
============
pip3 install . \
    && nuitka3 pytouch/pytouch_runner.py \
    && mv pytouch_runner.bin /usr/bin/pytouch;


