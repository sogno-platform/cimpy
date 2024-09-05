from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSK(ExcitationSystemDynamics):
    """
    Slovakian excitation system.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.

    :efdmax: Field voltage clipping upper level limit (<i>Efdmax</i>) (&gt; ExcSK.efdmin). Default: 0.0
    :efdmin: Field voltage clipping lower level limit (<i>Efdmin</i>) (&lt; ExcSK.efdmax). Default: 0.0
    :emax: Maximum field voltage output (<i>Emax</i>) (&gt; ExcSK.emin).  Typical value = 20. Default: 0.0
    :emin: Minimum field voltage output (<i>Emin</i>) (&lt; ExcSK.emax).  Typical value = -20. Default: 0.0
    :k: Gain (<i>K</i>).  Typical value = 1. Default: 0.0
    :k1: Parameter of underexcitation limit (<i>K1</i>).  Typical value = 0,1364. Default: 0.0
    :k2: Parameter of underexcitation limit (<i>K2</i>).  Typical value = -0,3861. Default: 0.0
    :kc: PI controller gain (<i>Kc</i>).  Typical value = 70. Default: 0.0
    :kce: Rectifier regulation factor (<i>Kce</i>).  Typical value = 0. Default: 0.0
    :kd: Exciter internal reactance (<i>Kd</i>).  Typical value = 0. Default: 0.0
    :kgob: P controller gain (<i>Kgob</i>).  Typical value = 10. Default: 0.0
    :kp: PI controller gain (<i>Kp</i>).  Typical value = 1. Default: 0.0
    :kqi: PI controller gain of integral component (<i>Kqi</i>).  Typical value = 0. Default: 0.0
    :kqob: Rate of rise of the reactive power (<i>Kqob</i>). Default: 0.0
    :kqp: PI controller gain (<i>Kqp</i>).  Typical value = 0. Default: 0.0
    :nq: Deadband of reactive power (<i>nq</i>).  Determines the range of sensitivity.  Typical value = 0,001. Default: 0.0
    :qconoff: Secondary voltage control state (<i>Qc_on_off</i>). true = secondary voltage control is on false = secondary voltage control is off. Typical value = false. Default: False
    :qz: Desired value (setpoint) of reactive power, manual setting (<i>Qz</i>). Default: 0.0
    :remote: Selector to apply automatic calculation in secondary controller model (<i>remote</i>). true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (<i>Qz</i>) is required. Typical value = true. Default: False
    :sbase: Apparent power of the unit (<i>Sbase</i>) (&gt; 0).  Unit = MVA.  Typical value = 259. Default: 0.0
    :tc: PI controller phase lead time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 8. Default: 0
    :te: Time constant of gain block (<i>Te</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :ti: PI controller phase lead time constant (<i>Ti</i>) (&gt;= 0).  Typical value = 2. Default: 0
    :tp: Time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :tr: Voltage transducer time constant (<i>Tr</i>) (&gt;= 0).  Typical value = 0,01. Default: 0
    :uimax: Maximum error (<i>UImax</i>) (&gt; ExcSK.uimin).  Typical value = 10. Default: 0.0
    :uimin: Minimum error (<i>UImin</i>) (&lt; ExcSK.uimax).  Typical value = -10. Default: 0.0
    :urmax: Maximum controller output (<i>URmax</i>) (&gt; ExcSK.urmin).  Typical value = 10. Default: 0.0
    :urmin: Minimum controller output (<i>URmin</i>) (&lt; ExcSK.urmax).  Typical value = -10. Default: 0.0
    :vtmax: Maximum terminal voltage input (<i>Vtmax</i>) (&gt; ExcSK.vtmin).  Determines the range of voltage deadband.  Typical value = 1,05. Default: 0.0
    :vtmin: Minimum terminal voltage input (<i>Vtmin</i>) (&lt; ExcSK.vtmax).  Determines the range of voltage deadband.  Typical value = 0,95. Default: 0.0
    :yp: Maximum output (<i>Yp</i>).  Typical value = 1. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "efdmax": [
            cgmesProfile.DY.value,
        ],
        "efdmin": [
            cgmesProfile.DY.value,
        ],
        "emax": [
            cgmesProfile.DY.value,
        ],
        "emin": [
            cgmesProfile.DY.value,
        ],
        "k": [
            cgmesProfile.DY.value,
        ],
        "k1": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "kc": [
            cgmesProfile.DY.value,
        ],
        "kce": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "kgob": [
            cgmesProfile.DY.value,
        ],
        "kp": [
            cgmesProfile.DY.value,
        ],
        "kqi": [
            cgmesProfile.DY.value,
        ],
        "kqob": [
            cgmesProfile.DY.value,
        ],
        "kqp": [
            cgmesProfile.DY.value,
        ],
        "nq": [
            cgmesProfile.DY.value,
        ],
        "qconoff": [
            cgmesProfile.DY.value,
        ],
        "qz": [
            cgmesProfile.DY.value,
        ],
        "remote": [
            cgmesProfile.DY.value,
        ],
        "sbase": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "ti": [
            cgmesProfile.DY.value,
        ],
        "tp": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "uimax": [
            cgmesProfile.DY.value,
        ],
        "uimin": [
            cgmesProfile.DY.value,
        ],
        "urmax": [
            cgmesProfile.DY.value,
        ],
        "urmin": [
            cgmesProfile.DY.value,
        ],
        "vtmax": [
            cgmesProfile.DY.value,
        ],
        "vtmin": [
            cgmesProfile.DY.value,
        ],
        "yp": [
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
        efdmax=0.0,
        efdmin=0.0,
        emax=0.0,
        emin=0.0,
        k=0.0,
        k1=0.0,
        k2=0.0,
        kc=0.0,
        kce=0.0,
        kd=0.0,
        kgob=0.0,
        kp=0.0,
        kqi=0.0,
        kqob=0.0,
        kqp=0.0,
        nq=0.0,
        qconoff=False,
        qz=0.0,
        remote=False,
        sbase=0.0,
        tc=0,
        te=0,
        ti=0,
        tp=0,
        tr=0,
        uimax=0.0,
        uimin=0.0,
        urmax=0.0,
        urmin=0.0,
        vtmax=0.0,
        vtmin=0.0,
        yp=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.efdmin = efdmin
        self.emax = emax
        self.emin = emin
        self.k = k
        self.k1 = k1
        self.k2 = k2
        self.kc = kc
        self.kce = kce
        self.kd = kd
        self.kgob = kgob
        self.kp = kp
        self.kqi = kqi
        self.kqob = kqob
        self.kqp = kqp
        self.nq = nq
        self.qconoff = qconoff
        self.qz = qz
        self.remote = remote
        self.sbase = sbase
        self.tc = tc
        self.te = te
        self.ti = ti
        self.tp = tp
        self.tr = tr
        self.uimax = uimax
        self.uimin = uimin
        self.urmax = urmax
        self.urmin = urmin
        self.vtmax = vtmax
        self.vtmin = vtmin
        self.yp = yp

    def __str__(self):
        str = "class=ExcSK\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
