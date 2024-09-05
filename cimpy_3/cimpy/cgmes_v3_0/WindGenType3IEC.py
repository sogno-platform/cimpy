from .IdentifiedObject import IdentifiedObject


class WindGenType3IEC(IdentifiedObject):
    """
    Parent class supporting relationships to IEC wind turbines type 3 generator models of IEC type 3A and 3B.

    :dipmax: Maximum active current ramp rate (<i>di</i><i><sub>pmax</sub></i>). It is a project-dependent parameter. Default: 0.0
    :diqmax: Maximum reactive current ramp rate (<i>di</i><i><sub>qmax</sub></i>). It is a project-dependent parameter. Default: 0.0
    :xs: Electromagnetic transient reactance (<i>x</i><i><sub>S</sub></i>). It is a type-dependent parameter. Default: 0.0
    :WindTurbineType3IEC: Wind turbine type 3 model with which this wind generator type 3 is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "dipmax": [
            cgmesProfile.DY.value,
        ],
        "diqmax": [
            cgmesProfile.DY.value,
        ],
        "xs": [
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
        self, dipmax=0.0, diqmax=0.0, xs=0.0, WindTurbineType3IEC=None, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.dipmax = dipmax
        self.diqmax = diqmax
        self.xs = xs
        self.WindTurbineType3IEC = WindTurbineType3IEC

    def __str__(self):
        str = "class=WindGenType3IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
