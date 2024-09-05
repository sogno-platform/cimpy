from .IdentifiedObject import IdentifiedObject


class WindAeroOneDimIEC(IdentifiedObject):
    """
    One-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.2.

    :ka: Aerodynamic gain (<i>k</i><i><sub>a</sub></i>). It is a type-dependent parameter. Default: 0.0
    :thetaomega: Initial pitch angle (<i>theta</i><i><sub>omega0</sub></i>). It is a case-dependent parameter. Default: 0.0
    :WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "thetaomega": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType3IEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self, ka=0.0, thetaomega=0.0, WindTurbineType3IEC=None, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.thetaomega = thetaomega
        self.WindTurbineType3IEC = WindTurbineType3IEC

    def __str__(self):
        str = "class=WindAeroOneDimIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
