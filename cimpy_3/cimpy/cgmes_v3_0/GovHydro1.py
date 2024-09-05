from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro1(TurbineGovernorDynamics):
    """
    Basic hydro turbine governor.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :rperm: Permanent droop (<i>R</i>) (&gt; 0).  Typical value = 0,04. Default: 0.0
    :rtemp: Temporary droop (<i>r</i>) (&gt; GovHydro1.rperm).  Typical value = 0,3. Default: 0.0
    :tr: Washout time constant (<i>Tr</i>) (&gt; 0).  Typical value = 5. Default: 0
    :tf: Filter time constant (<i>Tf</i>) (&gt; 0).  Typical value = 0,05. Default: 0
    :tg: Gate servo time constant (<i>Tg</i>) (&gt; 0).  Typical value = 0,5. Default: 0
    :velm: Maximum gate velocity (<i>Vlem</i>) (&gt; 0).  Typical value = 0,2. Default: 0.0
    :gmax: Maximum gate opening (<i>Gmax</i>) (&gt; 0 and &gt; GovHydro.gmin).  Typical value = 1. Default: 0.0
    :gmin: Minimum gate opening (<i>Gmin</i>) (&gt;= 0 and &lt; GovHydro1.gmax).  Typical value = 0. Default: 0.0
    :tw: Water inertia time constant (<i>Tw</i>) (&gt; 0).  Typical value = 1. Default: 0
    :at: Turbine gain (<i>At</i>) (&gt; 0).  Typical value = 1,2. Default: 0.0
    :dturb: Turbine damping factor (<i>Dturb</i>) (&gt;= 0).  Typical value = 0,5. Default: 0.0
    :qnl: No-load flow at nominal head (<i>qnl</i>) (&gt;= 0).  Typical value = 0,08. Default: 0.0
    :hdam: Turbine nominal head (<i>hdam</i>).  Typical value = 1. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "rperm": [
            cgmesProfile.DY.value,
        ],
        "rtemp": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tg": [
            cgmesProfile.DY.value,
        ],
        "velm": [
            cgmesProfile.DY.value,
        ],
        "gmax": [
            cgmesProfile.DY.value,
        ],
        "gmin": [
            cgmesProfile.DY.value,
        ],
        "tw": [
            cgmesProfile.DY.value,
        ],
        "at": [
            cgmesProfile.DY.value,
        ],
        "dturb": [
            cgmesProfile.DY.value,
        ],
        "qnl": [
            cgmesProfile.DY.value,
        ],
        "hdam": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class TurbineGovernorDynamics: \n"
        + TurbineGovernorDynamics.__doc__
    )

    def __init__(
        self,
        mwbase=0.0,
        rperm=0.0,
        rtemp=0.0,
        tr=0,
        tf=0,
        tg=0,
        velm=0.0,
        gmax=0.0,
        gmin=0.0,
        tw=0,
        at=0.0,
        dturb=0.0,
        qnl=0.0,
        hdam=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.rperm = rperm
        self.rtemp = rtemp
        self.tr = tr
        self.tf = tf
        self.tg = tg
        self.velm = velm
        self.gmax = gmax
        self.gmin = gmin
        self.tw = tw
        self.at = at
        self.dturb = dturb
        self.qnl = qnl
        self.hdam = hdam

    def __str__(self):
        str = "class=GovHydro1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
