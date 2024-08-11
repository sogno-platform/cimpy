from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class Curve(IdentifiedObject):
    """
    A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.

    :CurveDatas: The curve of  this curve data point. Default: "list"
    :curveStyle: The style or shape of the curve. Default: None
    :xUnit: The X-axis units of measure. Default: None
    :y1Unit: The Y1-axis units of measure. Default: None
    :y2Unit: The Y2-axis units of measure. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "CurveDatas": [Profile.EQ.value, ],
        "curveStyle": [Profile.EQ.value, ],
        "xUnit": [Profile.EQ.value, ],
        "y1Unit": [Profile.EQ.value, ],
        "y2Unit": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, CurveDatas = "list", curveStyle = None, xUnit = None, y1Unit = None, y2Unit = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.CurveDatas = CurveDatas
        self.curveStyle = curveStyle
        self.xUnit = xUnit
        self.y1Unit = y1Unit
        self.y2Unit = y2Unit

    def __str__(self):
        str = "class=Curve\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
