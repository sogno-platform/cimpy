from .IdentifiedObject import IdentifiedObject


class WindAeroConstIEC(IdentifiedObject):
    """
    Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC 61400-27-1:2015, 5.6.1.1.

    :WindGenTurbineType1aIEC: Wind turbine type 1A model with which this wind aerodynamic model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindGenTurbineType1aIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(self, WindGenTurbineType1aIEC=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindGenTurbineType1aIEC = WindGenTurbineType1aIEC

    def __str__(self):
        str = "class=WindAeroConstIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
