from .Switch import Switch


class Cut(Switch):
    """
    A cut separates a line segment into two parts. The cut appears as a switch inserted between these two parts and connects them together. As the cut is normally open there is no galvanic connection between the two line segment parts. But it is possible to close the cut to get galvanic connection. The cut terminals are oriented towards the line segment terminals with the same sequence number. Hence the cut terminal with sequence number equal to 1 is oriented to the line segment's terminal with sequence number equal to 1. The cut terminals also act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this, connectivity nodes are placed at the cut terminals. Once the connectivity nodes are in place any conducting equipment can be connected at them.

    :ACLineSegment: The line segment to which the cut is applied. Default: None
    :lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line segment, i.e. the line segment Terminal with sequenceNumber equal to 1. Default: 0.0
    """

    cgmesProfile = Switch.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "ACLineSegment": [
            cgmesProfile.EQ.value,
        ],
        "lengthFromTerminal1": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Switch: \n" + Switch.__doc__

    def __init__(self, ACLineSegment=None, lengthFromTerminal1=0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ACLineSegment = ACLineSegment
        self.lengthFromTerminal1 = lengthFromTerminal1

    def __str__(self):
        str = "class=Cut\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
