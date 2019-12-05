from enum import Enum


class Base():
    """
    Base Class for CIM
    """

    cgmesProfile = Enum("cgmesProfile", {"EQ": 0, "SSH": 1, "TP": 2, "SV": 3, "DY": 4, "GL": 5, "DI": 6})

    def __init__(self, *args, **kw_args):
        pass

    def printxml(self, dict={}):
        return dict
