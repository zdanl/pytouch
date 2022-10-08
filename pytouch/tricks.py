# turn a dict() into an object() fullfilling accessibility fetish
class ov(object):
    def __init__(self, d): self.__dict__ = d
