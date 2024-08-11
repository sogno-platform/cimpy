from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssSB4(PowerSystemStabilizerDynamics):
    """
    Power sensitive stabilizer model.

    :kx: Gain (Kx). Default: 0.0
    :ta: Time constant (Ta). Default: 0.0
    :tb: Time constant (Tb). Default: 0.0
    :tc: Time constant (Tc). Default: 0.0
    :td: Time constant (Td). Default: 0.0
    :te: Time constant (Te). Default: 0.0
    :tt: Time constant (Tt). Default: 0.0
    :tx1: Reset time constant (Tx1). Default: 0.0
    :tx2: Time constant (Tx2). Default: 0.0
    :vsmax: Limiter (Vsmax). Default: 0.0
    :vsmin: Limiter (Vsmin). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kx": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tt": [Profile.DY.value, ],
        "tx1": [Profile.DY.value, ],
        "tx2": [Profile.DY.value, ],
        "vsmax": [Profile.DY.value, ],
        "vsmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, kx = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, td = 0.0, te = 0.0, tt = 0.0, tx1 = 0.0, tx2 = 0.0, vsmax = 0.0, vsmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kx = kx
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.td = td
        self.te = te
        self.tt = tt
        self.tx1 = tx1
        self.tx2 = tx2
        self.vsmax = vsmax
        self.vsmin = vsmin

    def __str__(self):
        str = "class=PssSB4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
