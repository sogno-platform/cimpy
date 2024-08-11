from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches.

    :SwitchSchedules: A SwitchSchedule is associated with a Switch. Default: "list"
    :normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen. Default: False
    :open: The attribute tells if the switch is considered open when used as input to topology processing. Default: False
    :ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and construction. Default: 0.0
    :retained: Branch is retained in a bus branch model.  The flow through retained switches will normally be calculated in power flow. Default: False
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "SwitchSchedules": [Profile.EQ.value, ],
        "normalOpen": [Profile.EQ.value, ],
        "open": [Profile.SSH.value, ],
        "ratedCurrent": [Profile.EQ.value, ],
        "retained": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, SwitchSchedules = "list", normalOpen = False, open = False, ratedCurrent = 0.0, retained = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SwitchSchedules = SwitchSchedules
        self.normalOpen = normalOpen
        self.open = open
        self.ratedCurrent = ratedCurrent
        self.retained = retained

    def __str__(self):
        str = "class=Switch\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
