from .IdentifiedObject import IdentifiedObject


class WindMechIEC(IdentifiedObject):
    """
    Two mass model. Reference: IEC 61400-27-1:2015, 5.6.2.1.

    :cdrt: Drive train damping (<i>c</i><i><sub>drt</sub></i><i>)</i>. It is a type-dependent parameter. Default: 0.0
    :hgen: Inertia constant of generator (<i>H</i><i><sub>gen</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :hwtr: Inertia constant of wind turbine rotor (<i>H</i><i><sub>WTR</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :kdrt: Drive train stiffness (<i>k</i><i><sub>drt</sub></i>). It is a type-dependent parameter. Default: 0.0
    :WindTurbineType3IEC: Wind turbine type 3 model with which this wind mechanical model is associated. Default: None
    :WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind mechanical model is associated. Default: None
    :WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "cdrt": [
            cgmesProfile.DY.value,
        ],
        "hgen": [
            cgmesProfile.DY.value,
        ],
        "hwtr": [
            cgmesProfile.DY.value,
        ],
        "kdrt": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType3IEC": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType1or2IEC": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType4bIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        cdrt=0.0,
        hgen=0,
        hwtr=0,
        kdrt=0.0,
        WindTurbineType3IEC=None,
        WindTurbineType1or2IEC=None,
        WindTurbineType4bIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.cdrt = cdrt
        self.hgen = hgen
        self.hwtr = hwtr
        self.kdrt = kdrt
        self.WindTurbineType3IEC = WindTurbineType3IEC
        self.WindTurbineType1or2IEC = WindTurbineType1or2IEC
        self.WindTurbineType4bIEC = WindTurbineType4bIEC

    def __str__(self):
        str = "class=WindMechIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
