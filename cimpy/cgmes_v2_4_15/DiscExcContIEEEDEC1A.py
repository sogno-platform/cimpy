from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from .CGMESProfile import Profile


class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.  Reference: IEEE Standard 421.5-2005 Section 12.2.

    :esc: Speed change reference ().  Typical Value = 0.0015. Default: 0.0
    :kan: Discontinuous controller gain ().  Typical Value = 400. Default: 0.0
    :ketl: Terminal voltage limiter gain ().  Typical Value = 47. Default: 0.0
    :tan: Discontinuous controller time constant ().  Typical Value = 0.08. Default: 0.0
    :td: Time constant ().  Typical Value = 0.03. Default: 0.0
    :tl1: Time constant ().  Typical Value = 0.025. Default: 0.0
    :tl2: Time constant ().  Typical Value = 1.25. Default: 0.0
    :tw5: DEC washout time constant ().  Typical Value = 5. Default: 0.0
    :val: Regulator voltage reference ().  Typical Value = 5.5. Default: 0.0
    :vanmax: Limiter for Van (). Default: 0.0
    :vomax: Limiter ().  Typical Value = 0.3. Default: 0.0
    :vomin: Limiter ().  Typical Value = 0.1. Default: 0.0
    :vsmax: Limiter ().  Typical Value = 0.2. Default: 0.0
    :vsmin: Limiter ().  Typical Value = -0.066. Default: 0.0
    :vtc: Terminal voltage level reference ().  Typical Value = 0.95. Default: 0.0
    :vtlmt: Voltage reference ().  Typical Value = 1.1. Default: 0.0
    :vtm: Voltage limits ().  Typical Value = 1.13. Default: 0.0
    :vtn: Voltage limits ().  Typical Value = 1.12. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "esc": [Profile.DY.value, ],
        "kan": [Profile.DY.value, ],
        "ketl": [Profile.DY.value, ],
        "tan": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "tl1": [Profile.DY.value, ],
        "tl2": [Profile.DY.value, ],
        "tw5": [Profile.DY.value, ],
        "val": [Profile.DY.value, ],
        "vanmax": [Profile.DY.value, ],
        "vomax": [Profile.DY.value, ],
        "vomin": [Profile.DY.value, ],
        "vsmax": [Profile.DY.value, ],
        "vsmin": [Profile.DY.value, ],
        "vtc": [Profile.DY.value, ],
        "vtlmt": [Profile.DY.value, ],
        "vtm": [Profile.DY.value, ],
        "vtn": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class DiscontinuousExcitationControlDynamics:\n" + DiscontinuousExcitationControlDynamics.__doc__

    def __init__(self, esc = 0.0, kan = 0.0, ketl = 0.0, tan = 0.0, td = 0.0, tl1 = 0.0, tl2 = 0.0, tw5 = 0.0, val = 0.0, vanmax = 0.0, vomax = 0.0, vomin = 0.0, vsmax = 0.0, vsmin = 0.0, vtc = 0.0, vtlmt = 0.0, vtm = 0.0, vtn = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.esc = esc
        self.kan = kan
        self.ketl = ketl
        self.tan = tan
        self.td = td
        self.tl1 = tl1
        self.tl2 = tl2
        self.tw5 = tw5
        self.val = val
        self.vanmax = vanmax
        self.vomax = vomax
        self.vomin = vomin
        self.vsmax = vsmax
        self.vsmin = vsmin
        self.vtc = vtc
        self.vtlmt = vtlmt
        self.vtm = vtm
        self.vtn = vtn

    def __str__(self):
        str = "class=DiscExcContIEEEDEC1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
