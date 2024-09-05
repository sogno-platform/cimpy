from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


class WindGenTurbineType1aIEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC type 1A. Reference: IEC 61400-27-1:2015, 5.5.2.2.

    :WindAeroConstIEC: Wind aerodynamic model associated with this wind turbine type 1A model. Default: None
    """

    cgmesProfile = WindTurbineType1or2IEC.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindAeroConstIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindTurbineType1or2IEC: \n"
        + WindTurbineType1or2IEC.__doc__
    )

    def __init__(self, WindAeroConstIEC=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindAeroConstIEC = WindAeroConstIEC

    def __str__(self):
        str = "class=WindGenTurbineType1aIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
