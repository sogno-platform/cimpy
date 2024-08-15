from .Base import Base
from .CGMESProfile import Profile


class SvTapStep(Base):
    """
    State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.

    :TapChanger: The tap changer associated with the tap step state. Default: None
    :position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined by the related tap changer model and normally is constrained to be within the range of minimum and maximum tap positions. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "TapChanger": [Profile.SV.value, ],
        "position": [Profile.SV.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SV.value


    def __init__(self, TapChanger = None, position = 0.0):

        self.TapChanger = TapChanger
        self.position = position

    def __str__(self):
        str = "class=SvTapStep\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
