from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC type 2.  Reference: IEC 61400-27-1:2015, 5.5.3.

    :WindContRotorRIEC: Wind control rotor resistance model associated with wind turbine type 2 model. Default: None
    :WindPitchContPowerIEC: Pitch control power model associated with this wind turbine type 2 model. Default: None
    """

    cgmesProfile = WindTurbineType1or2IEC.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindContRotorRIEC": [
            cgmesProfile.DY.value,
        ],
        "WindPitchContPowerIEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindTurbineType1or2IEC: \n"
        + WindTurbineType1or2IEC.__doc__
    )

    def __init__(
        self, WindContRotorRIEC=None, WindPitchContPowerIEC=None, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.WindContRotorRIEC = WindContRotorRIEC
        self.WindPitchContPowerIEC = WindPitchContPowerIEC

    def __str__(self):
        str = "class=WindGenTurbineType2IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
