import yaml, os

import pytouch

class ov(object):
    def __init__(self, d): self.__dict__ = d

class TemplateEngine(object):

    # could as well be {{ and }} as in other template engines
    delimiter = ov({
        "start": "__",
        "end": "__"
    })
    

    project_values = {
        "NAME": "",
        "AUTHOR": "",
        "DESCR": "",
        "VERSION": "",
        "LICENSE": ""
    }

    substitute_values = {}

    def __init__(self, name="", author="", descr="", version="", license=""):
        for k in self.project_values.keys():
            self.substitute_values["PROJECT_%s" %k] = eval(k.lower())

    def _read_template_config(self, filepath):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)

    def initialize(self, template="boilerplate"):
        # Load and patch files sequentially, don't keep all files in memory
        # Load and patch to disk, load next
        if os.path.exists(template) and os.path.exists(template) + "/cfg.yaml":
            print("Template exists and is external.")
            config = self._read_template_config(template + "/cfg.yaml")
            self.delimiter.start = config.start_delimiter
            self.delimiter.end = config.end_delimiter

        else:
            absolute_path = pytouch.__file__.replace("__init__.py", template)
            print("Looking for %s" %absolute_path)
            if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
                print("Template exists and is internal.")
                return 0
            else:
                print("Template not found, including internally.")
                return 1
