from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindContPType3IEC(IdentifiedObject):
    """
    P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.

    :WindDynamicsLookupTable: The P control type 3 model with which this wind dynamics lookup table is associated. Default: "list"
    :WindGenTurbineType3IEC: Wind turbine type 3 model with which this Wind control P type 3 model is associated. Default: None
    :dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0
    :dtrisemaxlvrt: Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter. Default: 0.0
    :kdtd: Gain for active drive train damping (). It is type dependent parameter. Default: 0.0
    :kip: PI controller integration parameter (). It is type dependent parameter. Default: 0.0
    :kpp: PI controller proportional gain (). It is type dependent parameter. Default: 0.0
    :mplvrt: Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is project dependent parameter. Default: False
    :omegaoffset: Offset to reference value that limits controller action during rotor speed changes (omega). It is case dependent parameter. Default: 0.0
    :pdtdmax: Maximum active drive train damping power (). It is type dependent parameter. Default: 0.0
    :rramp: Ramp limitation of torque, required in some grid codes (). It is project dependent parameter. Default: 0.0
    :tdvs: Timedelay after deep voltage sags (T). It is project dependent parameter. Default: 0.0
    :temin: Minimum electrical generator torque (). It is type dependent parameter. Default: 0.0
    :tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0.0
    :tpfilt: Filter time constant for power measurement (). It is type dependent parameter. Default: 0.0
    :tpord: Time constant in power order lag (). It is type dependent parameter. Default: 0.0
    :tufilt: Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0.0
    :tuscale: Voltage scaling factor of reset-torque (T). It is project dependent parameter. Default: 0.0
    :twref: Time constant in speed reference filter (). It is type dependent parameter. Default: 0.0
    :udvs: Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter. Default: 0.0
    :updip: Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is project dependent parameter. Default: 0.0
    :wdtd: Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type dependent parameter. Default: 0.0
    :zeta: Coefficient for active drive train damping (zeta). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindDynamicsLookupTable": [Profile.DY.value, ],
        "WindGenTurbineType3IEC": [Profile.DY.value, ],
        "dpmax": [Profile.DY.value, ],
        "dtrisemaxlvrt": [Profile.DY.value, ],
        "kdtd": [Profile.DY.value, ],
        "kip": [Profile.DY.value, ],
        "kpp": [Profile.DY.value, ],
        "mplvrt": [Profile.DY.value, ],
        "omegaoffset": [Profile.DY.value, ],
        "pdtdmax": [Profile.DY.value, ],
        "rramp": [Profile.DY.value, ],
        "tdvs": [Profile.DY.value, ],
        "temin": [Profile.DY.value, ],
        "tomegafilt": [Profile.DY.value, ],
        "tpfilt": [Profile.DY.value, ],
        "tpord": [Profile.DY.value, ],
        "tufilt": [Profile.DY.value, ],
        "tuscale": [Profile.DY.value, ],
        "twref": [Profile.DY.value, ],
        "udvs": [Profile.DY.value, ],
        "updip": [Profile.DY.value, ],
        "wdtd": [Profile.DY.value, ],
        "zeta": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindDynamicsLookupTable = "list", WindGenTurbineType3IEC = None, dpmax = 0.0, dtrisemaxlvrt = 0.0, kdtd = 0.0, kip = 0.0, kpp = 0.0, mplvrt = False, omegaoffset = 0.0, pdtdmax = 0.0, rramp = 0.0, tdvs = 0.0, temin = 0.0, tomegafilt = 0.0, tpfilt = 0.0, tpord = 0.0, tufilt = 0.0, tuscale = 0.0, twref = 0.0, udvs = 0.0, updip = 0.0, wdtd = 0.0, zeta = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
        self.dpmax = dpmax
        self.dtrisemaxlvrt = dtrisemaxlvrt
        self.kdtd = kdtd
        self.kip = kip
        self.kpp = kpp
        self.mplvrt = mplvrt
        self.omegaoffset = omegaoffset
        self.pdtdmax = pdtdmax
        self.rramp = rramp
        self.tdvs = tdvs
        self.temin = temin
        self.tomegafilt = tomegafilt
        self.tpfilt = tpfilt
        self.tpord = tpord
        self.tufilt = tufilt
        self.tuscale = tuscale
        self.twref = twref
        self.udvs = udvs
        self.updip = updip
        self.wdtd = wdtd
        self.zeta = zeta

    def __str__(self):
        str = "class=WindContPType3IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
