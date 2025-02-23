from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from .CGMESProfile import Profile


class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

    :tdr: Reset time delay (). Default: 0.0
    :vtmin: Terminal undervoltage comparison level (). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "tdr": [Profile.DY.value, ],
        "vtmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DiscontinuousExcitationControlDynamics:\n" + DiscontinuousExcitationControlDynamics.__doc__

    def __init__(self, tdr = 0.0, vtmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.tdr = tdr
        self.vtmin = vtmin

    def __str__(self):
        str = "class=DiscExcContIEEEDEC3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
