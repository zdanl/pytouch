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
