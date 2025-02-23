from .WindTurbineType3or4IEC import WindTurbineType3or4IEC
from .CGMESProfile import Profile


class WindGenTurbineType3IEC(WindTurbineType3or4IEC):
    """
    Generator model for wind turbines of IEC type 3A and 3B.

    :WindAeroLinearIEC: Wind aerodynamic model associated with this wind generator type 3 model. Default: None
    :WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model. Default: None
    :WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3. Default: None
    :WindMechIEC: Wind mechanical model associated with this wind turbine Type 3 model. Default: None
    :dipmax: Maximum active current ramp rate (di). It is project dependent parameter. Default: 0.0
    :diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindAeroLinearIEC": [Profile.DY.value, ],
        "WindContPType3IEC": [Profile.DY.value, ],
        "WindContPitchAngleIEC": [Profile.DY.value, ],
        "WindMechIEC": [Profile.DY.value, ],
        "dipmax": [Profile.DY.value, ],
        "diqmax": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindTurbineType3or4IEC:\n" + WindTurbineType3or4IEC.__doc__

    def __init__(self, WindAeroLinearIEC = None, WindContPType3IEC = None, WindContPitchAngleIEC = None, WindMechIEC = None, dipmax = 0.0, diqmax = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindAeroLinearIEC = WindAeroLinearIEC
        self.WindContPType3IEC = WindContPType3IEC
        self.WindContPitchAngleIEC = WindContPitchAngleIEC
        self.WindMechIEC = WindMechIEC
        self.dipmax = dipmax
        self.diqmax = diqmax

    def __str__(self):
        str = "class=WindGenTurbineType3IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
