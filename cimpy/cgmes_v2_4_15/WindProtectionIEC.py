from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindProtectionIEC(IdentifiedObject):
    """
    The grid protection model includes protection against over and under voltage, and against over and under frequency.  Reference: IEC Standard 614000-27-1 Section 6.6.6.

    :WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind turbine protection model is associated. Default: None
    :WindTurbineType3or4IEC: Wind generator type 3 or 4 model with which this wind turbine protection model is associated. Default: None
    :fover: Set of wind turbine over frequency protection levels (). It is project dependent parameter. Default: 0.0
    :funder: Set of wind turbine under frequency protection levels (). It is project dependent parameter. Default: 0.0
    :tfover: Set of corresponding wind turbine over frequency protection disconnection times (). It is project dependent parameter. Default: 0.0
    :tfunder: Set of corresponding wind turbine under frequency protection disconnection times (). It is project dependent parameter. Default: 0.0
    :tuover: Set of corresponding wind turbine over voltage protection disconnection times (). It is project dependent parameter. Default: 0.0
    :tuunder: Set of corresponding wind turbine under voltage protection disconnection times (). It is project dependent parameter. Default: 0.0
    :uover: Set of wind turbine over voltage protection levels (). It is project dependent parameter. Default: 0.0
    :uunder: Set of wind turbine under voltage protection levels (). It is project dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindTurbineType1or2IEC": [Profile.DY.value, ],
        "WindTurbineType3or4IEC": [Profile.DY.value, ],
        "fover": [Profile.DY.value, ],
        "funder": [Profile.DY.value, ],
        "tfover": [Profile.DY.value, ],
        "tfunder": [Profile.DY.value, ],
        "tuover": [Profile.DY.value, ],
        "tuunder": [Profile.DY.value, ],
        "uover": [Profile.DY.value, ],
        "uunder": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindTurbineType1or2IEC = None, WindTurbineType3or4IEC = None, fover = 0.0, funder = 0.0, tfover = 0.0, tfunder = 0.0, tuover = 0.0, tuunder = 0.0, uover = 0.0, uunder = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindTurbineType1or2IEC = WindTurbineType1or2IEC
        self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
        self.fover = fover
        self.funder = funder
        self.tfover = tfover
        self.tfunder = tfunder
        self.tuover = tuover
        self.tuunder = tuunder
        self.uover = uover
        self.uunder = uunder

    def __str__(self):
        str = "class=WindProtectionIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
