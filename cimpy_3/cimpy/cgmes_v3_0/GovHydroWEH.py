from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWEH(TurbineGovernorDynamics):
    """
    Woodward<sup>TM </sup>electric hydro governor.  [Footnote: Woodward electric hydro governors are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :rpg: Permanent droop for governor output feedback (<i>R-Perm-Gate</i>). Default: 0.0
    :rpp: Permanent droop for electrical power feedback (<i>R-Perm-Pe</i>). Default: 0.0
    :tpe: Electrical power droop time constant (<i>Tpe</i>) (&gt;= 0). Default: 0
    :kp: Derivative control gain (<i>Kp</i>). Default: 0.0
    :ki: Derivative controller Integral gain (<i>Ki</i>). Default: 0.0
    :kd: Derivative controller derivative gain (<i>Kd</i>). Default: 0.0
    :td: Derivative controller time constant (<i>Td</i>) (&gt;= 0).  Limits the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise. Default: 0
    :tp: Pilot valve time lag time constant (<i>Tp</i>) (&gt;= 0). Default: 0
    :tdv: Distributive valve time lag time constant (<i>Tdv</i>) (&gt;= 0). Default: 0
    :tg: Value to allow the distribution valve controller to advance beyond the gate movement rate limit (<i>Tg</i>) (&gt;= 0). Default: 0
    :gtmxop: Maximum gate opening rate (<i>Gtmxop</i>). Default: 0.0
    :gtmxcl: Maximum gate closing rate (<i>Gtmxcl</i>). Default: 0.0
    :gmax: Maximum gate position (<i>Gmax</i>) (&gt; GovHydroWEH.gmin). Default: 0.0
    :gmin: Minimum gate position (<i>Gmin</i>) (&lt; GovHydroWEH.gmax). Default: 0.0
    :dturb: Turbine damping factor (<i>Dturb</i>).  Unit = delta P (PU of <i>MWbase</i>) / delta speed (PU). Default: 0.0
    :tw: Water inertia time constant (<i>Tw</i>) (&gt; 0). Default: 0
    :db: Speed deadband (<i>db</i>). Default: 0.0
    :dpv: Value to allow the pilot valve controller to advance beyond the gate limits (<i>Dpv</i>). Default: 0.0
    :dicn: Value to allow the integral controller to advance beyond the gate limits (<i>Dicn</i>). Default: 0.0
    :feedbackSignal: Feedback signal selection (<i>Sw</i>). true = PID output (if <i>R-Perm-Gate </i>= droop and <i>R-Perm-Pe </i>= 0) false = electrical power (if <i>R-Perm-Gate </i>= 0 and <i>R-Perm-Pe </i>= droop) or false = gate position (if R<i>-Perm-Gate </i>= droop and <i>R-Perm-Pe </i>= 0). Typical value = false. Default: False
    :gv1: Gate 1 (<i>Gv1</i>).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv2: Gate 2 (<i>Gv2</i>).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv3: Gate 3 (<i>Gv3</i>).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv4: Gate 4 (<i>Gv4</i>).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv5: Gate 5 (<i>Gv5</i>).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl1: Flowgate 1 (<i>Fl1</i>).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl2: Flowgate 2 (<i>Fl2</i>).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl3: Flowgate 3 (<i>Fl3</i>).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl4: Flowgate 4 (<i>Fl4</i>).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl5: Flowgate 5 (<i>Fl5</i>).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fp1: Flow P1 (<i>Fp1</i>).  Turbine flow value for point 1 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp2: Flow P2 (<i>Fp2</i>).  Turbine flow value for point 2 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp3: Flow P3 (<i>Fp3</i>).  Turbine flow value for point 3 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp4: Flow P4 (<i>Fp4</i>).  Turbine flow value for point 4 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp5: Flow P5 (<i>Fp5</i>).  Turbine flow value for point 5 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp6: Flow P6 (<i>Fp6</i>).  Turbine flow value for point 6 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp7: Flow P7 (<i>Fp7</i>).  Turbine flow value for point 7 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp8: Flow P8 (<i>Fp8</i>).  Turbine flow value for point 8 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp9: Flow P9 (<i>Fp9</i>).  Turbine flow value for point 9 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp10: Flow P10 (<i>Fp10</i>).  Turbine flow value for point 10 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss1: Pmss flow P1 (<i>Pmss1</i>).  Mechanical power output for turbine flow point 1 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss2: Pmss flow P2 (<i>Pmss2</i>).  Mechanical power output for turbine flow point 2 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss3: Pmss flow P3 (<i>Pmss3</i>).  Mechanical power output for turbine flow point 3 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss4: Pmss flow P4 (<i>Pmss4</i>).  Mechanical power output for turbine flow point 4 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss5: Pmss flow P5 (<i>Pmss5</i>).  Mechanical power output for turbine flow point 5 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss6: Pmss flow P6 (<i>Pmss6</i>).  Mechanical power output for turbine flow point 6 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss7: Pmss flow P7 (<i>Pmss7</i>).  Mechanical power output for turbine flow point 7 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss8: Pmss flow P8 (<i>Pmss8</i>).  Mechanical power output for turbine flow point 8 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss9: Pmss flow P9 (<i>Pmss9</i>).  Mechanical power output for turbine flow point 9 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss10: Pmss flow P10 (<i>Pmss10</i>).  Mechanical power output for turbine flow point 10 for lookup table representing PU mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "rpg": [
            cgmesProfile.DY.value,
        ],
        "rpp": [
            cgmesProfile.DY.value,
        ],
        "tpe": [
            cgmesProfile.DY.value,
        ],
        "kp": [
            cgmesProfile.DY.value,
        ],
        "ki": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "td": [
            cgmesProfile.DY.value,
        ],
        "tp": [
            cgmesProfile.DY.value,
        ],
        "tdv": [
            cgmesProfile.DY.value,
        ],
        "tg": [
            cgmesProfile.DY.value,
        ],
        "gtmxop": [
            cgmesProfile.DY.value,
        ],
        "gtmxcl": [
            cgmesProfile.DY.value,
        ],
        "gmax": [
            cgmesProfile.DY.value,
        ],
        "gmin": [
            cgmesProfile.DY.value,
        ],
        "dturb": [
            cgmesProfile.DY.value,
        ],
        "tw": [
            cgmesProfile.DY.value,
        ],
        "db": [
            cgmesProfile.DY.value,
        ],
        "dpv": [
            cgmesProfile.DY.value,
        ],
        "dicn": [
            cgmesProfile.DY.value,
        ],
        "feedbackSignal": [
            cgmesProfile.DY.value,
        ],
        "gv1": [
            cgmesProfile.DY.value,
        ],
        "gv2": [
            cgmesProfile.DY.value,
        ],
        "gv3": [
            cgmesProfile.DY.value,
        ],
        "gv4": [
            cgmesProfile.DY.value,
        ],
        "gv5": [
            cgmesProfile.DY.value,
        ],
        "fl1": [
            cgmesProfile.DY.value,
        ],
        "fl2": [
            cgmesProfile.DY.value,
        ],
        "fl3": [
            cgmesProfile.DY.value,
        ],
        "fl4": [
            cgmesProfile.DY.value,
        ],
        "fl5": [
            cgmesProfile.DY.value,
        ],
        "fp1": [
            cgmesProfile.DY.value,
        ],
        "fp2": [
            cgmesProfile.DY.value,
        ],
        "fp3": [
            cgmesProfile.DY.value,
        ],
        "fp4": [
            cgmesProfile.DY.value,
        ],
        "fp5": [
            cgmesProfile.DY.value,
        ],
        "fp6": [
            cgmesProfile.DY.value,
        ],
        "fp7": [
            cgmesProfile.DY.value,
        ],
        "fp8": [
            cgmesProfile.DY.value,
        ],
        "fp9": [
            cgmesProfile.DY.value,
        ],
        "fp10": [
            cgmesProfile.DY.value,
        ],
        "pmss1": [
            cgmesProfile.DY.value,
        ],
        "pmss2": [
            cgmesProfile.DY.value,
        ],
        "pmss3": [
            cgmesProfile.DY.value,
        ],
        "pmss4": [
            cgmesProfile.DY.value,
        ],
        "pmss5": [
            cgmesProfile.DY.value,
        ],
        "pmss6": [
            cgmesProfile.DY.value,
        ],
        "pmss7": [
            cgmesProfile.DY.value,
        ],
        "pmss8": [
            cgmesProfile.DY.value,
        ],
        "pmss9": [
            cgmesProfile.DY.value,
        ],
        "pmss10": [
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
        rpg=0.0,
        rpp=0.0,
        tpe=0,
        kp=0.0,
        ki=0.0,
        kd=0.0,
        td=0,
        tp=0,
        tdv=0,
        tg=0,
        gtmxop=0.0,
        gtmxcl=0.0,
        gmax=0.0,
        gmin=0.0,
        dturb=0.0,
        tw=0,
        db=0.0,
        dpv=0.0,
        dicn=0.0,
        feedbackSignal=False,
        gv1=0.0,
        gv2=0.0,
        gv3=0.0,
        gv4=0.0,
        gv5=0.0,
        fl1=0.0,
        fl2=0.0,
        fl3=0.0,
        fl4=0.0,
        fl5=0.0,
        fp1=0.0,
        fp2=0.0,
        fp3=0.0,
        fp4=0.0,
        fp5=0.0,
        fp6=0.0,
        fp7=0.0,
        fp8=0.0,
        fp9=0.0,
        fp10=0.0,
        pmss1=0.0,
        pmss2=0.0,
        pmss3=0.0,
        pmss4=0.0,
        pmss5=0.0,
        pmss6=0.0,
        pmss7=0.0,
        pmss8=0.0,
        pmss9=0.0,
        pmss10=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.rpg = rpg
        self.rpp = rpp
        self.tpe = tpe
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.td = td
        self.tp = tp
        self.tdv = tdv
        self.tg = tg
        self.gtmxop = gtmxop
        self.gtmxcl = gtmxcl
        self.gmax = gmax
        self.gmin = gmin
        self.dturb = dturb
        self.tw = tw
        self.db = db
        self.dpv = dpv
        self.dicn = dicn
        self.feedbackSignal = feedbackSignal
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.fl1 = fl1
        self.fl2 = fl2
        self.fl3 = fl3
        self.fl4 = fl4
        self.fl5 = fl5
        self.fp1 = fp1
        self.fp2 = fp2
        self.fp3 = fp3
        self.fp4 = fp4
        self.fp5 = fp5
        self.fp6 = fp6
        self.fp7 = fp7
        self.fp8 = fp8
        self.fp9 = fp9
        self.fp10 = fp10
        self.pmss1 = pmss1
        self.pmss2 = pmss2
        self.pmss3 = pmss3
        self.pmss4 = pmss4
        self.pmss5 = pmss5
        self.pmss6 = pmss6
        self.pmss7 = pmss7
        self.pmss8 = pmss8
        self.pmss9 = pmss9
        self.pmss10 = pmss10

    def __str__(self):
        str = "class=GovHydroWEH\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
