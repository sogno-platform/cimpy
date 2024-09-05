from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcBBC(ExcitationSystemDynamics):
    """
    Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main generator directly.

    :t1: Controller time constant (<i>T1</i>) (&gt;= 0).  Typical value = 6. Default: 0
    :t2: Controller time constant (<i>T2</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :t3: Lead/lag time constant (<i>T3</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0,05. Default: 0
    :t4: Lead/lag time constant (<i>T4</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0,01. Default: 0
    :k: Steady state gain (<i>K</i>) (not = 0).  Typical value = 300. Default: 0.0
    :vrmin: Minimum control element output (<i>Vrmin</i>) (&lt; ExcBBC.vrmax).  Typical value = -5. Default: 0.0
    :vrmax: Maximum control element output (<i>Vrmax</i>) (&gt; ExcBBC.vrmin).  Typical value = 5. Default: 0.0
    :efdmin: Minimum open circuit exciter voltage (<i>Efdmin</i>) (&lt; ExcBBC.efdmax).  Typical value = -5. Default: 0.0
    :efdmax: Maximum open circuit exciter voltage (<i>Efdmax</i>) (&gt; ExcBBC.efdmin).  Typical value = 5. Default: 0.0
    :xe: Effective excitation transformer reactance (<i>Xe</i>) (&gt;= 0).  <i>Xe</i> models the regulation of the transformer/rectifier unit.  Typical value = 0,05. Default: 0.0
    :switch: Supplementary signal routing selector (<i>switch</i>). true = <i>Vs</i> connected to 3rd summing point false =  <i>Vs</i> connected to 1st summing point (see diagram). Typical value = false. Default: False
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
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
        "k": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "efdmin": [
            cgmesProfile.DY.value,
        ],
        "efdmax": [
            cgmesProfile.DY.value,
        ],
        "xe": [
            cgmesProfile.DY.value,
        ],
        "switch": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ExcitationSystemDynamics: \n"
        + ExcitationSystemDynamics.__doc__
    )

    def __init__(
        self,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        k=0.0,
        vrmin=0.0,
        vrmax=0.0,
        efdmin=0.0,
        efdmax=0.0,
        xe=0.0,
        switch=False,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.vrmin = vrmin
        self.vrmax = vrmax
        self.efdmin = efdmin
        self.efdmax = efdmax
        self.xe = xe
        self.switch = switch

    def __str__(self):
        str = "class=ExcBBC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
