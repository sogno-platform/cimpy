from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindAeroConstIEC(IdentifiedObject):
    """
    The constant aerodynamic torque model assumes that the aerodynamic torque is constant.  Reference: IEC Standard 61400-27-1 Section 6.6.1.1.

    :WindGenTurbineType1IEC: Wind turbine type 1 model with which this wind aerodynamic model is associated. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindGenTurbineType1IEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindGenTurbineType1IEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindGenTurbineType1IEC = WindGenTurbineType1IEC

    def __str__(self):
        str = "class=WindAeroConstIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
