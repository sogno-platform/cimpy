from .DiscontinuousExcitationControlDynamics import (
    DiscontinuousExcitationControlDynamics,
)


class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault. Reference: IEEE 421.5-2005, 12.2.

    :vtlmt: Voltage reference (<i>V</i><i><sub>TLMT</sub></i>).  Typical value = 1,1. Default: 0.0
    :vomax: Limiter (<i>V</i><i><sub>OMAX</sub></i>) (&gt; DiscExcContIEEEDEC1A.vomin).  Typical value = 0,3. Default: 0.0
    :vomin: Limiter (<i>V</i><i><sub>OMIN</sub></i>) (&lt; DiscExcContIEEEDEC1A.vomax).  Typical value = 0,1. Default: 0.0
    :ketl: Terminal voltage limiter gain (<i>K</i><i><sub>ETL</sub></i>).  Typical value = 47. Default: 0.0
    :vtc: Terminal voltage level reference (<i>V</i><i><sub>TC</sub></i>).  Typical value = 0,95. Default: 0.0
    :val: Regulator voltage reference (<i>V</i><i><sub>AL</sub></i>).  Typical value = 5,5. Default: 0.0
    :esc: Speed change reference (<i>E</i><i><sub>SC</sub></i>).  Typical value = 0,0015. Default: 0.0
    :kan: Discontinuous controller gain (<i>K</i><i><sub>AN</sub></i>).  Typical value = 400. Default: 0.0
    :tan: Discontinuous controller time constant (<i>T</i><i><sub>AN</sub></i>) (&gt;= 0).  Typical value = 0,08. Default: 0
    :tw5: DEC washout time constant (<i>T</i><i><sub>W</sub></i><sub>5</sub>) (&gt;= 0).  Typical value = 5. Default: 0
    :vsmax: Limiter (<i>V</i><i><sub>SMAX</sub></i>)(&gt; DiscExcContIEEEDEC1A.vsmin).  Typical value = 0,2. Default: 0.0
    :vsmin: Limiter (<i>V</i><i><sub>SMIN</sub></i>) (&lt; DiscExcContIEEEDEC1A.vsmax).  Typical value = -0,066. Default: 0.0
    :td: Time constant (<i>T</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 0,03. Default: 0
    :tl1: Time constant (<i>T</i><i><sub>L</sub></i><sub>1</sub>) (&gt;= 0).  Typical value = 0,025. Default: 0
    :tl2: Time constant (<i>T</i><i><sub>L</sub></i><sub>2</sub>) (&gt;= 0).  Typical value = 1,25. Default: 0
    :vtm: Voltage limits (<i>V</i><i><sub>TM</sub></i>).  Typical value = 1,13. Default: 0.0
    :vtn: Voltage limits (<i>V</i><i><sub>TN</sub></i>).  Typical value = 1,12. Default: 0.0
    :vanmax: Limiter for Van (<i>V</i><i><sub>ANMAX</sub></i>). Default: 0.0
    """

    cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "vtlmt": [
            cgmesProfile.DY.value,
        ],
        "vomax": [
            cgmesProfile.DY.value,
        ],
        "vomin": [
            cgmesProfile.DY.value,
        ],
        "ketl": [
            cgmesProfile.DY.value,
        ],
        "vtc": [
            cgmesProfile.DY.value,
        ],
        "val": [
            cgmesProfile.DY.value,
        ],
        "esc": [
            cgmesProfile.DY.value,
        ],
        "kan": [
            cgmesProfile.DY.value,
        ],
        "tan": [
            cgmesProfile.DY.value,
        ],
        "tw5": [
            cgmesProfile.DY.value,
        ],
        "vsmax": [
            cgmesProfile.DY.value,
        ],
        "vsmin": [
            cgmesProfile.DY.value,
        ],
        "td": [
            cgmesProfile.DY.value,
        ],
        "tl1": [
            cgmesProfile.DY.value,
        ],
        "tl2": [
            cgmesProfile.DY.value,
        ],
        "vtm": [
            cgmesProfile.DY.value,
        ],
        "vtn": [
            cgmesProfile.DY.value,
        ],
        "vanmax": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n"
        + DiscontinuousExcitationControlDynamics.__doc__
    )

    def __init__(
        self,
        vtlmt=0.0,
        vomax=0.0,
        vomin=0.0,
        ketl=0.0,
        vtc=0.0,
        val=0.0,
        esc=0.0,
        kan=0.0,
        tan=0,
        tw5=0,
        vsmax=0.0,
        vsmin=0.0,
        td=0,
        tl1=0,
        tl2=0,
        vtm=0.0,
        vtn=0.0,
        vanmax=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.vtlmt = vtlmt
        self.vomax = vomax
        self.vomin = vomin
        self.ketl = ketl
        self.vtc = vtc
        self.val = val
        self.esc = esc
        self.kan = kan
        self.tan = tan
        self.tw5 = tw5
        self.vsmax = vsmax
        self.vsmin = vsmin
        self.td = td
        self.tl1 = tl1
        self.tl2 = tl2
        self.vtm = vtm
        self.vtn = vtn
        self.vanmax = vanmax

    def __str__(self):
        str = "class=DiscExcContIEEEDEC1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
