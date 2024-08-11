from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcSCRX(ExcitationSystemDynamics):
    """
    Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem.

    :cswitch: Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage. Default: False
    :emax: Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
    :emin: Minimum field voltage output (Emin).  Typical Value = 0. Default: 0.0
    :k: Gain (K) (>0).  Typical Value = 200. Default: 0.0
    :rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance (RcRfd).  Typical Value = 0. Default: 0.0
    :tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is not defined explicitly.  Typical Value = 0.1. Default: 0.0
    :tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 0.0
    :te: Time constant of gain block (Te) (>0).  Typical Value = 0.02. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "cswitch": [Profile.DY.value, ],
        "emax": [Profile.DY.value, ],
        "emin": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "rcrfd": [Profile.DY.value, ],
        "tatb": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, cswitch = False, emax = 0.0, emin = 0.0, k = 0.0, rcrfd = 0.0, tatb = 0.0, tb = 0.0, te = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.cswitch = cswitch
        self.emax = emax
        self.emin = emin
        self.k = k
        self.rcrfd = rcrfd
        self.tatb = tatb
        self.tb = tb
        self.te = te

    def __str__(self):
        str = "class=ExcSCRX\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
