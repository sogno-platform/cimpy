from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssPTIST3(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 3.

    :m: (<i>M</i>).  <i>M</i> = 2 x <i>H</i>.  Typical value = 5. Default: 0.0
    :tf: Time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :tp: Time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :t1: Time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
    :t2: Time constant (<i>T2</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :t3: Time constant (<i>T3</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :t4: Time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0,05. Default: 0
    :k: Gain (<i>K</i>).  Typical value = 9. Default: 0.0
    :dtf: Time step frequency calculation (<i>deltatf</i>) (&gt;= 0).  Typical value = 0,025 (0,03 for 50 Hz). Default: 0
    :dtc: Time step related to activation of controls (<i>deltatc</i>) (&gt;= 0).  Typical value = 0,025 (0,03 for 50 Hz). Default: 0
    :dtp: Time step active power calculation (<i>deltatp</i>) (&gt;= 0).  Typical value = 0,0125  (0,015 for 50 Hz). Default: 0
    :t5: Time constant (<i>T5</i>) (&gt;= 0). Default: 0
    :t6: Time constant (<i>T6</i>) (&gt;= 0). Default: 0
    :a0: Filter coefficient (<i>A0</i>). Default: 0.0
    :a1: Limiter (<i>Al</i>). Default: 0.0
    :a2: Filter coefficient (<i>A2</i>). Default: 0.0
    :b0: Filter coefficient (<i>B0</i>). Default: 0.0
    :b1: Filter coefficient (<i>B1</i>). Default: 0.0
    :b2: Filter coefficient (<i>B2</i>). Default: 0.0
    :a3: Filter coefficient (<i>A3</i>). Default: 0.0
    :a4: Filter coefficient (<i>A4</i>). Default: 0.0
    :a5: Filter coefficient (<i>A5</i>). Default: 0.0
    :b3: Filter coefficient (<i>B3</i>). Default: 0.0
    :b4: Filter coefficient (<i>B4</i>). Default: 0.0
    :b5: Filter coefficient (<i>B5</i>). Default: 0.0
    :athres: Threshold value above which output averaging will be bypassed (<i>Athres</i>).  Typical value = 0,005. Default: 0.0
    :dl: Limiter (<i>Dl</i>). Default: 0.0
    :al: Limiter (<i>Al</i>). Default: 0.0
    :lthres: Threshold value (<i>Lthres</i>). Default: 0.0
    :pmin: (<i>Pmin</i>). Default: 0.0
    :isw: Digital/analogue output switch (<i>Isw</i>). true = produce analogue output false = convert to digital output, using tap selection table. Default: False
    :nav: Number of control outputs to average (<i>NAV</i>) (1 &lt;=  <i>NAV</i> &lt;= 16).  Typical value = 4. Default: 0.0
    :ncl: Number of counts at limit to active limit function (<i>NCL</i>) (&gt; 0). Default: 0.0
    :ncr: Number of counts until reset after limit function is triggered (<i>NCR</i>). Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "m": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tp": [
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
        "dtf": [
            cgmesProfile.DY.value,
        ],
        "dtc": [
            cgmesProfile.DY.value,
        ],
        "dtp": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "a0": [
            cgmesProfile.DY.value,
        ],
        "a1": [
            cgmesProfile.DY.value,
        ],
        "a2": [
            cgmesProfile.DY.value,
        ],
        "b0": [
            cgmesProfile.DY.value,
        ],
        "b1": [
            cgmesProfile.DY.value,
        ],
        "b2": [
            cgmesProfile.DY.value,
        ],
        "a3": [
            cgmesProfile.DY.value,
        ],
        "a4": [
            cgmesProfile.DY.value,
        ],
        "a5": [
            cgmesProfile.DY.value,
        ],
        "b3": [
            cgmesProfile.DY.value,
        ],
        "b4": [
            cgmesProfile.DY.value,
        ],
        "b5": [
            cgmesProfile.DY.value,
        ],
        "athres": [
            cgmesProfile.DY.value,
        ],
        "dl": [
            cgmesProfile.DY.value,
        ],
        "al": [
            cgmesProfile.DY.value,
        ],
        "lthres": [
            cgmesProfile.DY.value,
        ],
        "pmin": [
            cgmesProfile.DY.value,
        ],
        "isw": [
            cgmesProfile.DY.value,
        ],
        "nav": [
            cgmesProfile.DY.value,
        ],
        "ncl": [
            cgmesProfile.DY.value,
        ],
        "ncr": [
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
        m=0.0,
        tf=0,
        tp=0,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        k=0.0,
        dtf=0,
        dtc=0,
        dtp=0,
        t5=0,
        t6=0,
        a0=0.0,
        a1=0.0,
        a2=0.0,
        b0=0.0,
        b1=0.0,
        b2=0.0,
        a3=0.0,
        a4=0.0,
        a5=0.0,
        b3=0.0,
        b4=0.0,
        b5=0.0,
        athres=0.0,
        dl=0.0,
        al=0.0,
        lthres=0.0,
        pmin=0.0,
        isw=False,
        nav=0.0,
        ncl=0.0,
        ncr=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.m = m
        self.tf = tf
        self.tp = tp
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.dtf = dtf
        self.dtc = dtc
        self.dtp = dtp
        self.t5 = t5
        self.t6 = t6
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.athres = athres
        self.dl = dl
        self.al = al
        self.lthres = lthres
        self.pmin = pmin
        self.isw = isw
        self.nav = nav
        self.ncl = ncl
        self.ncr = ncr

    def __str__(self):
        str = "class=PssPTIST3\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
