from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroPelton(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and surge chamber. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is located under the GovHydroFrancis class.

    :av0: Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 0.0
    :av1: Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 0.0
    :bp: Droop (bp).  Typical Value = 0.05. Default: 0.0
    :db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :db2: Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01. Default: 0.0
    :h1: Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 0.0
    :h2: Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 0.0
    :hn: Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 0.0
    :kc: Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 0.0
    :kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025. Default: 0.0
    :qc0: No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05. Default: 0.0
    :qn: Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 0.0
    :simplifiedPelton: Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation false = enable of complete Pelton model simulation (non linear gain). Typical Value = false. Default: False
    :staticCompensating: Static compensating characteristic (Cflag). true = enable of static compensating characteristic  false = inhibit of static compensating characteristic. Typical Value = false. Default: False
    :ta: Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3. Default: 0.0
    :ts: Gate servo time constant (Ts).  Typical Value = 0.15. Default: 0.0
    :tv: Servomotor integrator time constant (TV).  Typical Value = 0.3. Default: 0.0
    :twnc: Water inertia time constant (Twnc).  Typical Value = 1. Default: 0.0
    :twng: Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 0.0
    :tx: Electronic integrator time constant (Tx).  Typical Value = 0.5. Default: 0.0
    :va: Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016. Default: 0.0
    :valvmax: Maximum gate opening (ValvMax).  Typical Value = 1. Default: 0.0
    :valvmin: Minimum gate opening (ValvMin).  Typical Value = 0. Default: 0.0
    :vav: Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017. Default: 0.0
    :vc: Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016. Default: 0.0
    :vcv: Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017. Default: 0.0
    :waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: False
    :zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "av0": [Profile.DY.value, ],
        "av1": [Profile.DY.value, ],
        "bp": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "h1": [Profile.DY.value, ],
        "h2": [Profile.DY.value, ],
        "hn": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "qc0": [Profile.DY.value, ],
        "qn": [Profile.DY.value, ],
        "simplifiedPelton": [Profile.DY.value, ],
        "staticCompensating": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "ts": [Profile.DY.value, ],
        "tv": [Profile.DY.value, ],
        "twnc": [Profile.DY.value, ],
        "twng": [Profile.DY.value, ],
        "tx": [Profile.DY.value, ],
        "va": [Profile.DY.value, ],
        "valvmax": [Profile.DY.value, ],
        "valvmin": [Profile.DY.value, ],
        "vav": [Profile.DY.value, ],
        "vc": [Profile.DY.value, ],
        "vcv": [Profile.DY.value, ],
        "waterTunnelSurgeChamberSimulation": [Profile.DY.value, ],
        "zsfc": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, av0 = 0.0, av1 = 0.0, bp = 0.0, db1 = 0.0, db2 = 0.0, h1 = 0.0, h2 = 0.0, hn = 0.0, kc = 0.0, kg = 0.0, qc0 = 0.0, qn = 0.0, simplifiedPelton = False, staticCompensating = False, ta = 0.0, ts = 0.0, tv = 0.0, twnc = 0.0, twng = 0.0, tx = 0.0, va = 0.0, valvmax = 0.0, valvmin = 0.0, vav = 0.0, vc = 0.0, vcv = 0.0, waterTunnelSurgeChamberSimulation = False, zsfc = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.av0 = av0
        self.av1 = av1
        self.bp = bp
        self.db1 = db1
        self.db2 = db2
        self.h1 = h1
        self.h2 = h2
        self.hn = hn
        self.kc = kc
        self.kg = kg
        self.qc0 = qc0
        self.qn = qn
        self.simplifiedPelton = simplifiedPelton
        self.staticCompensating = staticCompensating
        self.ta = ta
        self.ts = ts
        self.tv = tv
        self.twnc = twnc
        self.twng = twng
        self.tx = tx
        self.va = va
        self.valvmax = valvmax
        self.valvmin = valvmin
        self.vav = vav
        self.vc = vc
        self.vcv = vcv
        self.waterTunnelSurgeChamberSimulation = waterTunnelSurgeChamberSimulation
        self.zsfc = zsfc

    def __str__(self):
        str = "class=GovHydroPelton\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
