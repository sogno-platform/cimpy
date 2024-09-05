from .Base import Base


class Boolean(Base):
    """
    A type with the value space "true" and "false".

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.GL.value,
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
    ):

        pass

    def __str__(self):
        str = "class=Boolean\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
