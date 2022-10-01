default_file = "foo.pytouch"

source_tmpl = "\n".join("""
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
