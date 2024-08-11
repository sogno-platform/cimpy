from .WindGenType4IEC import WindGenType4IEC
from .CGMESProfile import Profile


class WindTurbineType4aIEC(WindGenType4IEC):
    """
    Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.2.

    :WindContPType4aIEC: Wind control P type 4A model associated with this wind turbine type 4A model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindContPType4aIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class WindGenType4IEC:\n" + WindGenType4IEC.__doc__

    def __init__(self, WindContPType4aIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindContPType4aIEC = WindContPType4aIEC

    def __str__(self):
        str = "class=WindTurbineType4aIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
