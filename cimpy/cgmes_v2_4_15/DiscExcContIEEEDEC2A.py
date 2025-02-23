from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from .CGMESProfile import Profile


class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC2A model for the discontinuous excitation control. This system provides transient excitation boosting via an open-loop control as initiated by a trigger signal generated remotely.  Reference: IEEE Standard 421.5-2005 Section 12.3.

    :td1: Discontinuous controller time constant (). Default: 0.0
    :td2: Discontinuous controller washout time constant (). Default: 0.0
    :vdmax: Limiter (). Default: 0.0
    :vdmin: Limiter (). Default: 0.0
    :vk: Discontinuous controller input reference (). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "td1": [Profile.DY.value, ],
        "td2": [Profile.DY.value, ],
        "vdmax": [Profile.DY.value, ],
        "vdmin": [Profile.DY.value, ],
        "vk": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DiscontinuousExcitationControlDynamics:\n" + DiscontinuousExcitationControlDynamics.__doc__

    def __init__(self, td1 = 0.0, td2 = 0.0, vdmax = 0.0, vdmin = 0.0, vk = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.td1 = td1
        self.td2 = td2
        self.vdmax = vdmax
        self.vdmin = vdmin
        self.vk = vk

    def __str__(self):
        str = "class=DiscExcContIEEEDEC2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
