from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class SeriesCompensator(ConductingEquipment):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.

    :r: Positive sequence resistance. Default: 0.0
    :r0: Zero sequence resistance. Default: 0.0
    :varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured at the series compensator. Default: False
    :varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration. Default: 0.0
    :varistorVoltageThreshold: The dc voltage at which the varistor start conducting. Default: 0.0
    :x: Positive sequence reactance. Default: 0.0
    :x0: Zero sequence reactance. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
        "r0": [Profile.EQ.value, ],
        "varistorPresent": [Profile.EQ.value, ],
        "varistorRatedCurrent": [Profile.EQ.value, ],
        "varistorVoltageThreshold": [Profile.EQ.value, ],
        "x": [Profile.EQ.value, ],
        "x0": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, r = 0.0, r0 = 0.0, varistorPresent = False, varistorRatedCurrent = 0.0, varistorVoltageThreshold = 0.0, x = 0.0, x0 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.r = r
        self.r0 = r0
        self.varistorPresent = varistorPresent
        self.varistorRatedCurrent = varistorRatedCurrent
        self.varistorVoltageThreshold = varistorVoltageThreshold
        self.x = x
        self.x0 = x0

    def __str__(self):
        str = "class=SeriesCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
