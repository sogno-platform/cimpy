from .ConductingEquipment import ConductingEquipment


class SeriesCompensator(ConductingEquipment):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.

    :r: Positive sequence resistance. Default: 0.0
    :x: Positive sequence reactance. Default: 0.0
    :r0: Zero sequence resistance. Default: 0.0
    :x0: Zero sequence reactance. Default: 0.0
    :varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured in parallel with the series compensator. It is used for short circuit calculations. Default: False
    :varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration. It is used for short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is true. The attribute shall be a positive value. Default: 0.0
    :varistorVoltageThreshold: The dc voltage at which the varistor starts conducting. It is used for short circuit calculations and exchanged only if SeriesCompensator.varistorPresent is true. Default: 0.0
    """

    cgmesProfile = ConductingEquipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "r": [
            cgmesProfile.EQ.value,
        ],
        "x": [
            cgmesProfile.EQ.value,
        ],
        "r0": [
            cgmesProfile.SC.value,
        ],
        "x0": [
            cgmesProfile.SC.value,
        ],
        "varistorPresent": [
            cgmesProfile.SC.value,
        ],
        "varistorRatedCurrent": [
            cgmesProfile.SC.value,
        ],
        "varistorVoltageThreshold": [
            cgmesProfile.SC.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ConductingEquipment: \n"
        + ConductingEquipment.__doc__
    )

    def __init__(
        self,
        r=0.0,
        x=0.0,
        r0=0.0,
        x0=0.0,
        varistorPresent=False,
        varistorRatedCurrent=0.0,
        varistorVoltageThreshold=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.r = r
        self.x = x
        self.r0 = r0
        self.x0 = x0
        self.varistorPresent = varistorPresent
        self.varistorRatedCurrent = varistorRatedCurrent
        self.varistorVoltageThreshold = varistorVoltageThreshold

    def __str__(self):
        str = "class=SeriesCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
