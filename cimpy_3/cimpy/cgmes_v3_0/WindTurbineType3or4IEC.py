from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 3 and type 4 including their control models.

    :WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or type 4 model. Default: None
    :WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or type 4 model. Default: None
    :WindContQLimIEC: Constant Q limitation model associated with this wind generator type 3 or type 4 model. Default: None
    :WindContQPQULimIEC: QP and QU limitation model associated with this wind generator type 3 or type 4 model. Default: None
    :WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or type 4 model. Default: None
    :WindRefFrameRotIEC: Reference frame rotation model associated with this wind turbine type 3 or type 4 model. Default: None
    """

    cgmesProfile = WindTurbineType3or4Dynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindContCurrLimIEC": [
            cgmesProfile.DY.value,
        ],
        "WIndContQIEC": [
            cgmesProfile.DY.value,
        ],
        "WindContQLimIEC": [
            cgmesProfile.DY.value,
        ],
        "WindContQPQULimIEC": [
            cgmesProfile.DY.value,
        ],
        "WindProtectionIEC": [
            cgmesProfile.DY.value,
        ],
        "WindRefFrameRotIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindTurbineType3or4Dynamics: \n"
        + WindTurbineType3or4Dynamics.__doc__
    )

    def __init__(
        self,
        WindContCurrLimIEC=None,
        WIndContQIEC=None,
        WindContQLimIEC=None,
        WindContQPQULimIEC=None,
        WindProtectionIEC=None,
        WindRefFrameRotIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.WindContCurrLimIEC = WindContCurrLimIEC
        self.WIndContQIEC = WIndContQIEC
        self.WindContQLimIEC = WindContQLimIEC
        self.WindContQPQULimIEC = WindContQPQULimIEC
        self.WindProtectionIEC = WindProtectionIEC
        self.WindRefFrameRotIEC = WindRefFrameRotIEC

    def __str__(self):
        str = "class=WindTurbineType3or4IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
