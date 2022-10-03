import pytouch

import yaml, os, random

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
            compile_string = self.delimiter.start + "PROJECT_%s" %k.upper()
            compile_string += self.delimiter.end
            self.substitute_values[compile_string] = eval(k.lower())

    # just shortening so everything fits into 80 screen bytes per line
    def _exst(self, path): return os.path.exists(path)

    def _read_template_config(self, filepath):
        with open(filepath, 'r') as file:
            return ov(yaml.safe_load(file))

    def _configure_template(self):
        config = self._read_template_config(self.template_path + "/.cfg.yaml")

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
        target = self.substitute_values["__PROJECT_NAME__"]
        os.system("mkdir %s" %target)
        os.system("mv %s/* %s" %(self._tmp_build, target))

    def _compile_files_and_directories(self):
        # TODO implement your own recursion for educational purposes
        for root, dirs, files in os.walk(self._tmp_build):
            for dir in dirs:
                path = root + "/" + dir
                if "__pycache__" in dir:
                    os.system("rm -rf %s" %path)
                for k, v in self.substitute_values.items():
                    if k in dir:
                        os.system("mv %s %s" %(path, path.replace(k, v)))
                        break
           
            last_changed = False
            for file in files:
                data = ""
                path = root + "/" + file
                if file.endswith(".pyc"):
                    os.system("rm %s" %path)
                with open(path, "r") as f:
                    data = f.read()
                    for k, v in self.substitute_values.items():
                        if k in data:
                            data = data.replace(k, v)
                            last_changed = True

                if last_changed is True:
                    with open(path, "w") as f2:
                        f2.write(data)
                    print("Processed %s" %file)
                    last_changed = False

                for k, v in self.substitute_values.items():
                    if k in file:
                        os.system("mv %s %s" %(path, path.replace(k, v)))
                        break

    def _compile_template_data(self):
        pass

    def _cleanup_build(self):
        os.system("rm -rf %s" %self._tmp_build)

    def run(self):
        self._configure_template()
        self._prepare_build()
        self._compile_files_and_directories()
        self._compile_files_and_directories()
        self._compile_template_data()
        self._move_build()
        self._cleanup_build()

    def initialize(self, template="boilerplate"):
        # Load and patch files sequentially, don't keep all files in memory
        # Load and patch to disk, load next
        if self._exst(template) is True and self._exst(template + "/.cfg.yaml"):
            self.template_path = template
            return 0
        else:
            absolute_path = pytouch.__file__.replace("__init__.py", template)
            print("Absolute path: %s" %absolute_path)
            if os.path.exists(absolute_path) and os.path.isdir(absolute_path):
                self.template_path = absolute_path
                return 0
            else:
                return 1
