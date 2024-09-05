from .WindTurbineType4IEC import WindTurbineType4IEC


class WindTurbineType4bIEC(WindTurbineType4IEC):
    """
    Wind turbine IEC type 4B. Reference: IEC 61400-27-1:2015, 5.5.5.3.

    :WindContPType4bIEC: Wind control P type 4B model associated with this wind turbine type 4B model. Default: None
    :WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4B model. Default: None
    :WindMechIEC: Wind mechanical model associated with this wind turbine type 4B model. Default: None
    """

    cgmesProfile = WindTurbineType4IEC.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindContPType4bIEC": [
            cgmesProfile.DY.value,
        ],
        "WindGenType4IEC": [
            cgmesProfile.DY.value,
        ],
        "WindMechIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindTurbineType4IEC: \n"
        + WindTurbineType4IEC.__doc__
    )

    def __init__(
        self,
        WindContPType4bIEC=None,
        WindGenType4IEC=None,
        WindMechIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.WindContPType4bIEC = WindContPType4bIEC
        self.WindGenType4IEC = WindGenType4IEC
        self.WindMechIEC = WindMechIEC

    def __str__(self):
        str = "class=WindTurbineType4bIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
