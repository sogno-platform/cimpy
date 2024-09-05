from .IdentifiedObject import IdentifiedObject


class WindContPType4aIEC(IdentifiedObject):
    """
    P control model type 4A. Reference: IEC 61400-27-1:2015, 5.6.5.5.

    :dpmaxp4a: Maximum wind turbine power ramp rate (<i>dp</i><i><sub>maxp4A</sub></i>). It is a project-dependent parameter. Default: 0.0
    :tpordp4a: Time constant in power order lag (<i>T</i><i><sub>pordp4A</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :tufiltp4a: Voltage measurement filter time constant (<i>T</i><i><sub>ufiltp4A</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "dpmaxp4a": [
            cgmesProfile.DY.value,
        ],
        "tpordp4a": [
            cgmesProfile.DY.value,
        ],
        "tufiltp4a": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType4aIEC": [
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
        dpmaxp4a=0.0,
        tpordp4a=0,
        tufiltp4a=0,
        WindTurbineType4aIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.dpmaxp4a = dpmaxp4a
        self.tpordp4a = tpordp4a
        self.tufiltp4a = tufiltp4a
        self.WindTurbineType4aIEC = WindTurbineType4aIEC

    def __str__(self):
        str = "class=WindContPType4aIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
