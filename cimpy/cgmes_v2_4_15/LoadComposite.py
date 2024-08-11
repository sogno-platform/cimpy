from .LoadDynamics import LoadDynamics
from .CGMESProfile import Profile


class LoadComposite(LoadDynamics):
    """
    This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

    :epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5. Default: 0.0
    :epfs: Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5. Default: 0.0
    :epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7. Default: 0.0
    :epvs: Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7. Default: 0.0
    :eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0. Default: 0.0
    :eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0. Default: 0.0
    :eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2. Default: 0.0
    :eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2. Default: 0.0
    :h: Inertia constant (H).  Typical Value = 2.5. Default: 0.0
    :lfrac: Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8. Default: 0.0
    :pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.5. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "epfd": [Profile.DY.value, ],
        "epfs": [Profile.DY.value, ],
        "epvd": [Profile.DY.value, ],
        "epvs": [Profile.DY.value, ],
        "eqfd": [Profile.DY.value, ],
        "eqfs": [Profile.DY.value, ],
        "eqvd": [Profile.DY.value, ],
        "eqvs": [Profile.DY.value, ],
        "h": [Profile.DY.value, ],
        "lfrac": [Profile.DY.value, ],
        "pfrac": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class LoadDynamics:\n" + LoadDynamics.__doc__

    def __init__(self, epfd = 0.0, epfs = 0.0, epvd = 0.0, epvs = 0.0, eqfd = 0.0, eqfs = 0.0, eqvd = 0.0, eqvs = 0.0, h = 0.0, lfrac = 0.0, pfrac = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.epfd = epfd
        self.epfs = epfs
        self.epvd = epvd
        self.epvs = epvs
        self.eqfd = eqfd
        self.eqfs = eqfs
        self.eqvd = eqvd
        self.eqvs = eqvs
        self.h = h
        self.lfrac = lfrac
        self.pfrac = pfrac

    def __str__(self):
        str = "class=LoadComposite\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
