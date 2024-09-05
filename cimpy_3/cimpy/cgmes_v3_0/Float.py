from .Base import Base


class Float(Base):
    """
    A floating point number. The range is unspecified and not limited.

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
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
        str = "class=Float\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
