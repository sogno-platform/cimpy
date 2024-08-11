from .VoltageCompensatorDynamics import VoltageCompensatorDynamics
from .CGMESProfile import Profile


class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    Reference: IEEE Standard 421.5-2005 Section 4.

    :rc:  Default: 0.0
    :tr:  Default: 0.0
    :xc:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "rc": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
        "xc": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class VoltageCompensatorDynamics:\n" + VoltageCompensatorDynamics.__doc__

    def __init__(self, rc = 0.0, tr = 0.0, xc = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.rc = rc
        self.tr = tr
        self.xc = xc

    def __str__(self):
        str = "class=VCompIEEEType1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
