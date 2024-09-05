from .LoadDynamics import LoadDynamics


class LoadComposite(LoadDynamics):
    """
    Combined static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

    :epvs: Active load-voltage dependence index (static) (<i>Epvs</i>).  Typical value = 0,7. Default: 0.0
    :epfs: Active load-frequency dependence index (static) (<i>Epfs</i>).  Typical value = 1,5. Default: 0.0
    :eqvs: Reactive load-voltage dependence index (static) (<i>Eqvs</i>).  Typical value = 2. Default: 0.0
    :eqfs: Reactive load-frequency dependence index (static) (<i>Eqfs</i>).  Typical value = 0. Default: 0.0
    :epvd: Active load-voltage dependence index (dynamic) (<i>Epvd</i>).  Typical value = 0,7. Default: 0.0
    :epfd: Active load-frequency dependence index (dynamic) (<i>Epfd</i>).  Typical value = 1,5. Default: 0.0
    :eqvd: Reactive load-voltage dependence index (dynamic) (<i>Eqvd</i>).  Typical value = 2. Default: 0.0
    :eqfd: Reactive load-frequency dependence index (dynamic) (<i>Eqfd</i>).  Typical value = 0. Default: 0.0
    :lfac: Loading factor (<i>L</i><i><sub>fac</sub></i>). The ratio of initial <i>P</i> to motor MVA base.  Typical value = 0,8. Default: 0.0
    :h: Inertia constant (<i>H</i>) (&gt;= 0).  Typical value = 2,5. Default: 0
    :pfrac: Fraction of constant-power load to be represented by this motor model (<i>P</i><i><sub>FRAC</sub></i>) (&gt;= 0,0 and &lt;= 1,0).  Typical value = 0,5. Default: 0.0
    """

    cgmesProfile = LoadDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "epvs": [
            cgmesProfile.DY.value,
        ],
        "epfs": [
            cgmesProfile.DY.value,
        ],
        "eqvs": [
            cgmesProfile.DY.value,
        ],
        "eqfs": [
            cgmesProfile.DY.value,
        ],
        "epvd": [
            cgmesProfile.DY.value,
        ],
        "epfd": [
            cgmesProfile.DY.value,
        ],
        "eqvd": [
            cgmesProfile.DY.value,
        ],
        "eqfd": [
            cgmesProfile.DY.value,
        ],
        "lfac": [
            cgmesProfile.DY.value,
        ],
        "h": [
            cgmesProfile.DY.value,
        ],
        "pfrac": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class LoadDynamics: \n" + LoadDynamics.__doc__
    )

    def __init__(
        self,
        epvs=0.0,
        epfs=0.0,
        eqvs=0.0,
        eqfs=0.0,
        epvd=0.0,
        epfd=0.0,
        eqvd=0.0,
        eqfd=0.0,
        lfac=0.0,
        h=0,
        pfrac=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.epvs = epvs
        self.epfs = epfs
        self.eqvs = eqvs
        self.eqfs = eqfs
        self.epvd = epvd
        self.epfd = epfd
        self.eqvd = eqvd
        self.eqfd = eqfd
        self.lfac = lfac
        self.h = h
        self.pfrac = pfrac

    def __str__(self):
        str = "class=LoadComposite\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
