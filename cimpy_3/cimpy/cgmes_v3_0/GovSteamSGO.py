from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamSGO(TurbineGovernorDynamics):
    """
    Simplified steam turbine governor.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :t1: Controller lag (<i>T1</i>) (&gt;= 0). Default: 0
    :t2: Controller lead compensation (<i>T2</i>) (&gt;= 0). Default: 0
    :t3: Governor lag (<i>T3</i>) (&gt; 0). Default: 0
    :t4: Delay due to steam inlet volumes associated with steam chest and inlet piping (<i>T4</i>) (&gt;= 0). Default: 0
    :t5: Reheater delay including hot and cold leads (<i>T5</i>) (&gt;= 0). Default: 0
    :t6: Delay due to IP-LP turbine, crossover pipes and LP end hoods (<i>T6</i>) (&gt;= 0). Default: 0
    :k1: One / PU regulation (<i>K1</i>). Default: 0.0
    :k2: Fraction (<i>K2</i>). Default: 0.0
    :k3: Fraction (<i>K3</i>). Default: 0.0
    :pmax: Upper power limit (<i>Pmax</i>) (&gt; GovSteamSGO.pmin). Default: 0.0
    :pmin: Lower power limit (<i>Pmin</i>) (&gt;= 0 and &lt; GovSteamSGO.pmax). Default: 0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "k1": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "pmax": [
            cgmesProfile.DY.value,
        ],
        "pmin": [
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
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        t5=0,
        t6=0,
        k1=0.0,
        k2=0.0,
        k3=0.0,
        pmax=0.0,
        pmin=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.pmax = pmax
        self.pmin = pmin

    def __str__(self):
        str = "class=GovSteamSGO\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
