from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 1 and type 2 including their control models. Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous generator model. Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3.

    :WindMechIEC: Wind mechanical model associated with this wind generator type 1 or type 2 model. Default: None
    :WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or type 2 model. Default: None
    """

    cgmesProfile = WindTurbineType1or2Dynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindMechIEC": [
            cgmesProfile.DY.value,
        ],
        "WindProtectionIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindTurbineType1or2Dynamics: \n"
        + WindTurbineType1or2Dynamics.__doc__
    )

    def __init__(self, WindMechIEC=None, WindProtectionIEC=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindMechIEC = WindMechIEC
        self.WindProtectionIEC = WindProtectionIEC

    def __str__(self):
        str = "class=WindTurbineType1or2IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
