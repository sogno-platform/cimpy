from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroWEH(TurbineGovernorDynamics):
    """
    Woodward Electric Hydro Governor Model.

    :db: Speed Dead Band (db). Default: 0.0
    :dicn: Value to allow the integral controller to advance beyond the gate limits (Dicn). Default: 0.0
    :dpv: Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv). Default: 0.0
    :dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Default: 0.0
    :feedbackSignal: Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0). Default: False
    :fl1: Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl2: Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl3: Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl4: Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fl5: Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :fp1: Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp10: Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp2: Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp3: Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp4: Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp5: Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp6: Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp7: Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp8: Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :fp9: Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :gmax: Maximum Gate Position (Gmax). Default: 0.0
    :gmin: Minimum Gate Position (Gmin). Default: 0.0
    :gtmxcl: Maximum gate closing rate (Gtmxcl). Default: 0.0
    :gtmxop: Maximum gate opening rate (Gtmxop). Default: 0.0
    :gv1: Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv2: Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv3: Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv4: Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :gv5: Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as a function of gate position to produce steady state flow. Default: 0.0
    :kd: Derivative controller derivative gain (Kd). Default: 0.0
    :ki: Derivative controller Integral gain (Ki). Default: 0.0
    :kp: Derivative control gain (Kp). Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pmss1: Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss10: Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss2: Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss3: Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss4: Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss5: Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss6: Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss7: Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss8: Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :pmss9: Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing per unit mechanical power on machine MVA rating as a function of turbine flow. Default: 0.0
    :rpg: Permanent droop for governor output feedback (R-Perm-Gate). Default: 0.0
    :rpp: Permanent droop for electrical power feedback (R-Perm-Pe). Default: 0.0
    :td: Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid amplification of high-frequency noise (Td). Default: 0.0
    :tdv: Distributive Valve time lag time constant (Tdv). Default: 0.0
    :tg: Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg). Default: 0.0
    :tp: Pilot Valve time lag time constant (Tp). Default: 0.0
    :tpe: Electrical power droop time constant (Tpe). Default: 0.0
    :tw: Water inertia time constant (Tw) (>0). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "db": [Profile.DY.value, ],
        "dicn": [Profile.DY.value, ],
        "dpv": [Profile.DY.value, ],
        "dturb": [Profile.DY.value, ],
        "feedbackSignal": [Profile.DY.value, ],
        "fl1": [Profile.DY.value, ],
        "fl2": [Profile.DY.value, ],
        "fl3": [Profile.DY.value, ],
        "fl4": [Profile.DY.value, ],
        "fl5": [Profile.DY.value, ],
        "fp1": [Profile.DY.value, ],
        "fp10": [Profile.DY.value, ],
        "fp2": [Profile.DY.value, ],
        "fp3": [Profile.DY.value, ],
        "fp4": [Profile.DY.value, ],
        "fp5": [Profile.DY.value, ],
        "fp6": [Profile.DY.value, ],
        "fp7": [Profile.DY.value, ],
        "fp8": [Profile.DY.value, ],
        "fp9": [Profile.DY.value, ],
        "gmax": [Profile.DY.value, ],
        "gmin": [Profile.DY.value, ],
        "gtmxcl": [Profile.DY.value, ],
        "gtmxop": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmss1": [Profile.DY.value, ],
        "pmss10": [Profile.DY.value, ],
        "pmss2": [Profile.DY.value, ],
        "pmss3": [Profile.DY.value, ],
        "pmss4": [Profile.DY.value, ],
        "pmss5": [Profile.DY.value, ],
        "pmss6": [Profile.DY.value, ],
        "pmss7": [Profile.DY.value, ],
        "pmss8": [Profile.DY.value, ],
        "pmss9": [Profile.DY.value, ],
        "rpg": [Profile.DY.value, ],
        "rpp": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "tdv": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tpe": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, db = 0.0, dicn = 0.0, dpv = 0.0, dturb = 0.0, feedbackSignal = False, fl1 = 0.0, fl2 = 0.0, fl3 = 0.0, fl4 = 0.0, fl5 = 0.0, fp1 = 0.0, fp10 = 0.0, fp2 = 0.0, fp3 = 0.0, fp4 = 0.0, fp5 = 0.0, fp6 = 0.0, fp7 = 0.0, fp8 = 0.0, fp9 = 0.0, gmax = 0.0, gmin = 0.0, gtmxcl = 0.0, gtmxop = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, kd = 0.0, ki = 0.0, kp = 0.0, mwbase = 0.0, pmss1 = 0.0, pmss10 = 0.0, pmss2 = 0.0, pmss3 = 0.0, pmss4 = 0.0, pmss5 = 0.0, pmss6 = 0.0, pmss7 = 0.0, pmss8 = 0.0, pmss9 = 0.0, rpg = 0.0, rpp = 0.0, td = 0.0, tdv = 0.0, tg = 0.0, tp = 0.0, tpe = 0.0, tw = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.db = db
        self.dicn = dicn
        self.dpv = dpv
        self.dturb = dturb
        self.feedbackSignal = feedbackSignal
        self.fl1 = fl1
        self.fl2 = fl2
        self.fl3 = fl3
        self.fl4 = fl4
        self.fl5 = fl5
        self.fp1 = fp1
        self.fp10 = fp10
        self.fp2 = fp2
        self.fp3 = fp3
        self.fp4 = fp4
        self.fp5 = fp5
        self.fp6 = fp6
        self.fp7 = fp7
        self.fp8 = fp8
        self.fp9 = fp9
        self.gmax = gmax
        self.gmin = gmin
        self.gtmxcl = gtmxcl
        self.gtmxop = gtmxop
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.kd = kd
        self.ki = ki
        self.kp = kp
        self.mwbase = mwbase
        self.pmss1 = pmss1
        self.pmss10 = pmss10
        self.pmss2 = pmss2
        self.pmss3 = pmss3
        self.pmss4 = pmss4
        self.pmss5 = pmss5
        self.pmss6 = pmss6
        self.pmss7 = pmss7
        self.pmss8 = pmss8
        self.pmss9 = pmss9
        self.rpg = rpg
        self.rpp = rpp
        self.td = td
        self.tdv = tdv
        self.tg = tg
        self.tp = tp
        self.tpe = tpe
        self.tw = tw

    def __str__(self):
        str = "class=GovHydroWEH\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
