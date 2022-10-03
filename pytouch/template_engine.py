import yaml, os

import pytouch

import random

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

    _tmp_build = "/tmp"

    def __init__(self, name="", author="", descr="", version="", license=""):
        for k in self.project_values.keys():
            self.substitute_values["PROJECT_%s" %k] = eval(k.lower())

    # just shortening so everything fits into 80 screen bytes per line
    def _exst(self, path): return os.path.exists(path)

    def _read_template_config(self, filepath):
        with open(filepath, 'r') as file:
            return ov(yaml.safe_load(file))

    def _configure_template(self):
        config = self._read_template_config(self.template_path + "/cfg.yaml")

        # Set delimiters
        self.delimiter.start = config.start_delimiter
        self.delimiter.end = config.end_delimiter

    def _prepare_build(self):
        # make build directory
        self._tmp_build += "/_build_%d" %(int(random.random() * 1024))
        os.mkdir(self._tmp_build)
        os.system("cp -r %s/* %s/" %(self.template_path, self._tmp_build))
        print("Building in %s" %self._tmp_build)

    def _move_build(self):
        # TODO make this better without os.system
        target = self.substitute_values["PROJECT_NAME"]
        os.system("mkdir %s" %target)
        os.system("mv %s/* %s" %(self._tmp_build, target))

    def _compile_files_and_directories(self):
        pass

    def _compile_template_data(self):
        pass

    def _cleanup_build(self):
        os.system("rm -rf %s" %self._tmp_build)

    def _run(self):
        self._configure_template()
        self._prepare_build()
        self._compile_files_and_directories()
        self._compile_template_data()
        self._move_build()
        self._cleanup_build()

    def initialize(self, template="boilerplate"):
        # Load and patch files sequentially, don't keep all files in memory
        # Load and patch to disk, load next
        if self._exst(template) is True and self._exst(template + "/cfg.yaml"):
            print("Template exists and is external.")
            self.template_path = template
            self._run()
        else:
            absolute_path = pytouch.__file__.replace("__init__.py", template)
            print("Looking for %s" %absolute_path)
            if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
                self.template_path = absolute_path
                print("Template exists and is internal.")
                self._run()
                return 0
            else:
                print("Template not found, including internally.")
                return 1
