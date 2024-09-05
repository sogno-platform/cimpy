from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSB4(PowerSystemStabilizerDynamics):
    """
    Power sensitive stabilizer model.

    :tt: Time constant (<i>Tt</i>) (&gt;= 0).  Typical value = 0,18. Default: 0
    :kx: Gain (<i>Kx</i>).  Typical value = 2,7. Default: 0.0
    :tx2: Time constant (<i>Tx2</i>) (&gt;= 0).  Typical value = 5,0. Default: 0
    :ta: Time constant (<i>Ta</i>) (&gt;= 0).  Typical value = 0,37. Default: 0
    :tx1: Reset time constant (<i>Tx1</i>) (&gt;= 0).  Typical value = 0,035. Default: 0
    :tb: Time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0,37. Default: 0
    :tc: Time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0,035. Default: 0
    :td: Time constant (<i>Td</i>) (&gt;= 0).  Typical value = 0,0. Default: 0
    :te: Time constant (<i>Te</i>) (&gt;= 0).  Typical value = 0,0169. Default: 0
    :vsmax: Limiter (<i>Vsmax</i>) (&gt; PssSB4.vsmin).  Typical value = 0,062. Default: 0.0
    :vsmin: Limiter (<i>Vsmin</i>) (&lt; PssSB4.vsmax).  Typical value = -0,062. Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "tt": [
            cgmesProfile.DY.value,
        ],
        "kx": [
            cgmesProfile.DY.value,
        ],
        "tx2": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "tx1": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "td": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "vsmax": [
            cgmesProfile.DY.value,
        ],
        "vsmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemStabilizerDynamics: \n"
        + PowerSystemStabilizerDynamics.__doc__
    )

    def __init__(
        self,
        tt=0,
        kx=0.0,
        tx2=0,
        ta=0,
        tx1=0,
        tb=0,
        tc=0,
        td=0,
        te=0,
        vsmax=0.0,
        vsmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.tt = tt
        self.kx = kx
        self.tx2 = tx2
        self.ta = ta
        self.tx1 = tx1
        self.tb = tb
        self.tc = tc
        self.td = td
        self.te = te
        self.vsmax = vsmax
        self.vsmin = vsmin

    def __str__(self):
        str = "class=PssSB4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
