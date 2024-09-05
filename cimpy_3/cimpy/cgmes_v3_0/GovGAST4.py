from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST4(TurbineGovernorDynamics):
    """
    Generic turbogas.

    :bp: Droop (<i>b</i><i><sub>p</sub></i>).  Typical value = 0,05. Default: 0.0
    :ty: Time constant of fuel valve positioner (<i>Ty</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :ta: Maximum gate opening velocity (<i>TA</i>) (&gt;= 0).  Typical value = 3. Default: 0
    :tc: Maximum gate closing velocity (<i>TC</i>) (&gt;= 0).  Typical value = 0,5. Default: 0
    :tcm: Fuel control time constant (<i>Tcm</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :ktm: Compressor gain (<i>Ktm</i>).  Typical value = 0. Default: 0.0
    :tm: Compressor discharge volume time constant (<i>Tm</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :rymx: Maximum valve opening (<i>RYMX</i>).  Typical value = 1,1. Default: 0.0
    :rymn: Minimum valve opening (<i>RYMN</i>).  Typical value = 0. Default: 0.0
    :mxef: Fuel flow maximum positive error value (<i>MXef</i>).  Typical value = 0,05. Default: 0.0
    :mnef: Fuel flow maximum negative error value (<i>MNef</i>).  Typical value = -0,05. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "bp": [
            cgmesProfile.DY.value,
        ],
        "ty": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "tcm": [
            cgmesProfile.DY.value,
        ],
        "ktm": [
            cgmesProfile.DY.value,
        ],
        "tm": [
            cgmesProfile.DY.value,
        ],
        "rymx": [
            cgmesProfile.DY.value,
        ],
        "rymn": [
            cgmesProfile.DY.value,
        ],
        "mxef": [
            cgmesProfile.DY.value,
        ],
        "mnef": [
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
        bp=0.0,
        ty=0,
        ta=0,
        tc=0,
        tcm=0,
        ktm=0.0,
        tm=0,
        rymx=0.0,
        rymn=0.0,
        mxef=0.0,
        mnef=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.bp = bp
        self.ty = ty
        self.ta = ta
        self.tc = tc
        self.tcm = tcm
        self.ktm = ktm
        self.tm = tm
        self.rymx = rymx
        self.rymn = rymn
        self.mxef = mxef
        self.mnef = mnef

    def __str__(self):
        str = "class=GovGAST4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
