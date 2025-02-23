from .Base import Base
from .CGMESProfile import Profile


class TieFlow(Base):
    """
    A flow specification in terms of location and direction for a control area.

    :ControlArea: The control area of the tie flows. Default: None
    :Terminal: The terminal to which this tie flow belongs. Default: None
    :positiveFlowIn: True if the flow into the terminal (load convention) is also flow into the control area.  For example, this attribute should be true if using the tie line terminal further away from the control area. For example to represent a tie to a shunt component (like a load or generator) in another area, this is the near end of a branch and this attribute would be specified as false. Default: False
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ControlArea": [Profile.EQ.value, ],
        "Terminal": [Profile.EQ.value, ],
        "positiveFlowIn": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, ControlArea = None, Terminal = None, positiveFlowIn = False):

        self.ControlArea = ControlArea
        self.Terminal = Terminal
        self.positiveFlowIn = positiveFlowIn

    def __str__(self):
        str = "class=TieFlow\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
