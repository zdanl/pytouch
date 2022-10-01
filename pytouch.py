#!/usr/bin/env python3

import sys
import os.path

tmpl_data = "\n".join("""
#!/usr/bin/env python3

# This is your project description.

# Author: Your Name <your@name.me>
# 2022 (c) some rights reversed.

def main():
    your_function()
    pass

def your_function():
    return 1

if __name__ == "__main__":
    main()
""".split("\n")[1:-1])

def main():
    global tmpl_data

    # f is file
    if (os.path.exists("template.pytouch")):
        f = open("template.pytouch", "r")
        tmpl_data = f.read()
        f.close()

    # t is target
    with open(sys.argv[1], "w") as t:
        t.write(tmpl_data)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: pytouch [target_filepath]")
