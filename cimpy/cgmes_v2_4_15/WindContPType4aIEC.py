from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindContPType4aIEC(IdentifiedObject):
    """
    P control model Type 4A.  Reference: IEC Standard 61400-27-1 Section 6.6.5.4.

    :WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated. Default: None
    :dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0
    :tpord: Time constant in power order lag (). It is type dependent parameter. Default: 0.0
    :tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindTurbineType4aIEC": [Profile.DY.value, ],
        "dpmax": [Profile.DY.value, ],
        "tpord": [Profile.DY.value, ],
        "tufilt": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindTurbineType4aIEC = None, dpmax = 0.0, tpord = 0.0, tufilt = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindTurbineType4aIEC = WindTurbineType4aIEC
        self.dpmax = dpmax
        self.tpord = tpord
        self.tufilt = tufilt

    def __str__(self):
        str = "class=WindContPType4aIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
