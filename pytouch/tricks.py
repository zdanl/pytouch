# turn a dict() into an object() fullfilling accessibility fetish
class object_view(object):
    def __init__(self, d): self.__dict__ = d
