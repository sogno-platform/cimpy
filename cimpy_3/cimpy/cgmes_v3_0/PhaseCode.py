from .Base import Base


class PhaseCode(Base):
    """
    An unordered enumeration of phase identifiers.  Allows designation of phases for both transmission and distribution equipment, circuits and loads.   The enumeration, by itself, does not describe how the phases are connected together or connected to ground.  Ground is not explicitly denoted as a phase. Residential and small commercial loads are often served from single-phase, or split-phase, secondary circuits. For the example of s12N, phases 1 and 2 refer to hot wires that are 180 degrees out of phase, while N refers to the neutral wire. Through single-phase transformer connections, these secondary circuits may be served from one or two of the primary phases A, B, and C. For three-phase loads, use the A, B, C phase codes instead of s12N. The integer values are from IEC 61968-9 to support revenue metering applications.

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
    ):

        pass

    def __str__(self):
        str = "class=PhaseCode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
