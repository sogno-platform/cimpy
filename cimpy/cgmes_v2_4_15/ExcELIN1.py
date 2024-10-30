from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcELIN1(ExcitationSystemDynamics):
    """
    Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  A power system stabilizer with power input is included in the model.

    :dpnf: Controller follow up dead band (Dpnf).  Typical Value = 0. Default: 0.0
    :efmax: Maximum open circuit excitation voltage (Efmax).  Typical Value = 5. Default: 0.0
    :efmin: Minimum open circuit excitation voltage (Efmin).  Typical Value = -5. Default: 0.0
    :ks1: Stabilizer Gain 1 (Ks1).  Typical Value = 0. Default: 0.0
    :ks2: Stabilizer Gain 2 (Ks2).  Typical Value = 0. Default: 0.0
    :smax: Stabilizer Limit Output (smax).  Typical Value = 0.1. Default: 0.0
    :tfi: Current transducer time constant (Tfi).  Typical Value = 0. Default: 0.0
    :tnu: Controller reset time constant (Tnu).  Typical Value = 2. Default: 0.0
    :ts1: Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1. Default: 0.0
    :ts2: Stabilizer Filter Time Constant (Ts2).  Typical Value = 1. Default: 0.0
    :tsw: Stabilizer parameters (Tsw).  Typical Value = 3. Default: 0.0
    :vpi: Current controller gain (Vpi).  Typical Value = 12.45. Default: 0.0
    :vpnf: Controller follow up gain (Vpnf).  Typical Value = 2. Default: 0.0
    :vpu: Voltage controller proportional gain (Vpu).  Typical Value = 34.5. Default: 0.0
    :xe: Excitation transformer effective reactance (Xe) (>=0).  Xe represents the regulation of the transformer/rectifier unit.  Typical Value = 0.06. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dpnf": [Profile.DY.value, ],
        "efmax": [Profile.DY.value, ],
        "efmin": [Profile.DY.value, ],
        "ks1": [Profile.DY.value, ],
        "ks2": [Profile.DY.value, ],
        "smax": [Profile.DY.value, ],
        "tfi": [Profile.DY.value, ],
        "tnu": [Profile.DY.value, ],
        "ts1": [Profile.DY.value, ],
        "ts2": [Profile.DY.value, ],
        "tsw": [Profile.DY.value, ],
        "vpi": [Profile.DY.value, ],
        "vpnf": [Profile.DY.value, ],
        "vpu": [Profile.DY.value, ],
        "xe": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, dpnf = 0.0, efmax = 0.0, efmin = 0.0, ks1 = 0.0, ks2 = 0.0, smax = 0.0, tfi = 0.0, tnu = 0.0, ts1 = 0.0, ts2 = 0.0, tsw = 0.0, vpi = 0.0, vpnf = 0.0, vpu = 0.0, xe = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dpnf = dpnf
        self.efmax = efmax
        self.efmin = efmin
        self.ks1 = ks1
        self.ks2 = ks2
        self.smax = smax
        self.tfi = tfi
        self.tnu = tnu
        self.ts1 = ts1
        self.ts2 = ts2
        self.tsw = tsw
        self.vpi = vpi
        self.vpnf = vpnf
        self.vpu = vpu
        self.xe = xe

    def __str__(self):
        str = "class=ExcELIN1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
