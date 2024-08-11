from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics
from .CGMESProfile import Profile


class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control models.

    :WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or 4 model. Default: None
    :WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or 4 model. Default: None
    :WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or 4 model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WIndContQIEC": [Profile.DY.value, ],
        "WindContCurrLimIEC": [Profile.DY.value, ],
        "WindProtectionIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class WindTurbineType3or4Dynamics:\n" + WindTurbineType3or4Dynamics.__doc__

    def __init__(self, WIndContQIEC = None, WindContCurrLimIEC = None, WindProtectionIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WIndContQIEC = WIndContQIEC
        self.WindContCurrLimIEC = WindContCurrLimIEC
        self.WindProtectionIEC = WindProtectionIEC

    def __str__(self):
        str = "class=WindTurbineType3or4IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
