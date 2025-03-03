from .Base import Base
from .CGMESProfile import Profile


class CurveData(Base):
    """
    Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific class  can be used to specify the x and y axis values along with their specific data types.

    :Curve: The point data values that define this curve. Default: None
    :xvalue: The data value of the X-axis variable,  depending on the X-axis units. Default: 0.0
    :y1value: The data value of the  first Y-axis variable, depending on the Y-axis units. Default: 0.0
    :y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Curve": [Profile.EQ.value, ],
        "xvalue": [Profile.EQ.value, ],
        "y1value": [Profile.EQ.value, ],
        "y2value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, Curve = None, xvalue = 0.0, y1value = 0.0, y2value = 0.0):

        self.Curve = Curve
        self.xvalue = xvalue
        self.y1value = y1value
        self.y2value = y2value

    def __str__(self):
        str = "class=CurveData\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
