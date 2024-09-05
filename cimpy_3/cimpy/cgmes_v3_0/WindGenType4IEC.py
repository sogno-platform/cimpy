from .IdentifiedObject import IdentifiedObject


class WindGenType4IEC(IdentifiedObject):
    """
    IEC type 4 generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.4.

    :dipmax: Maximum active current ramp rate (<i>di</i><i><sub>pmax</sub></i>). It is a project-dependent parameter. Default: 0.0
    :diqmin: Minimum reactive current ramp rate (<i>di</i><i><sub>qmin</sub></i>). It is a project-dependent parameter. Default: 0.0
    :diqmax: Maximum reactive current ramp rate (<i>di</i><i><sub>qmax</sub></i>). It is a project-dependent parameter. Default: 0.0
    :tg: Time constant (<i>T</i><i><sub>g</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :WindTurbineType4aIEC: Wind turbine type 4A model with which this wind generator type 4 model is associated. Default: None
    :WindTurbineType4bIEC: Wind turbine type 4B model with which this wind generator type 4 model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "dipmax": [
            cgmesProfile.DY.value,
        ],
        "diqmin": [
            cgmesProfile.DY.value,
        ],
        "diqmax": [
            cgmesProfile.DY.value,
        ],
        "tg": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType4aIEC": [
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
        dipmax=0.0,
        diqmin=0.0,
        diqmax=0.0,
        tg=0,
        WindTurbineType4aIEC=None,
        WindTurbineType4bIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.dipmax = dipmax
        self.diqmin = diqmin
        self.diqmax = diqmax
        self.tg = tg
        self.WindTurbineType4aIEC = WindTurbineType4aIEC
        self.WindTurbineType4bIEC = WindTurbineType4bIEC

    def __str__(self):
        str = "class=WindGenType4IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
