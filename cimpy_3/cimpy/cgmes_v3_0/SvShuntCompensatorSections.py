from .Base import Base


class SvShuntCompensatorSections(Base):
    """
    State variable for the number of sections in service for a shunt compensator.

    :ShuntCompensator: The shunt compensator for which the state applies. Default: None
    :sections: The number of sections in service as a continuous variable. The attribute shall be a positive value or zero. To get integer value scale with ShuntCompensator.bPerSection. Default: 0.0
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SV.value,
        ],
        "ShuntCompensator": [
            cgmesProfile.SV.value,
        ],
        "sections": [
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        ShuntCompensator=None,
        sections=0.0,
    ):

        self.ShuntCompensator = ShuntCompensator
        self.sections = sections

    def __str__(self):
        str = "class=SvShuntCompensatorSections\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
