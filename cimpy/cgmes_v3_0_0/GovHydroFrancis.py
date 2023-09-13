from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroFrancis(TurbineGovernorDynamics):
	'''
	Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of the hydraulic system of detailed hydro unit models, such as Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram.

	:am: Opening section <i>S</i><i><sub>EFF</sub></i> at the maximum efficiency (<i>Am</i>).  Typical value = 0,7. Default: 0.0
	:av0: Area of the surge tank (<i>A</i><i><sub>V0</sub></i>). Unit = m<sup>2</sup>. Typical value = 30. Default: 0.0
	:av1: Area of the compensation tank (<i>A</i><i><sub>V1</sub></i>). Unit = m<sup>2</sup>. Typical value = 700. Default: 0.0
	:bp: Droop (<i>Bp</i>).  Typical value = 0,05. Default: 0.0
	:db1: Intentional dead-band width (<i>DB1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:etamax: Maximum efficiency (<i>EtaMax</i>).  Typical value = 1,05. Default: 0.0
	:governorControl: Governor control flag (<i>Cflag</i>).  Typical value = mechanicHydrolicTachoAccelerator. Default: None
	:h1: Head of compensation chamber water level with respect to the level of penstock (<i>H</i><i><sub>1</sub></i>).  Unit = km.  Typical value = 0,004. Default: 0.0
	:h2: Head of surge tank water level with respect to the level of penstock (<i>H</i><i><sub>2</sub></i>).  Unit = km.  Typical value = 0,040. Default: 0.0
	:hn: Rated hydraulic head (<i>H</i><i><sub>n</sub></i>).  Unit = km.  Typical value = 0,250. Default: 0.0
	:kc: Penstock loss coefficient (due to friction) (<i>Kc</i>).  Typical value = 0,025. Default: 0.0
	:kg: Water tunnel and surge chamber loss coefficient (due to friction) (<i>Kg</i>).  Typical value = 0,025. Default: 0.0
	:kt: Washout gain (<i>Kt</i>).  Typical value = 0,25. Default: 0.0
	:qc0: No-load turbine flow at nominal head (<i>Qc0</i>).  Typical value = 0,1. Default: 0.0
	:qn: Rated flow (<i>Q</i><i><sub>n</sub></i>). Unit = m<sup>3</sup>/s. Typical value = 250. Default: 0.0
	:ta: Derivative gain (<i>Ta</i>) (&gt;= 0).  Typical value = 3. Default: 0
	:td: Washout time constant (<i>Td</i>) (&gt;= 0).  Typical value = 6. Default: 0
	:ts: Gate servo time constant (<i>Ts</i>) (&gt;= 0).  Typical value = 0,5. Default: 0
	:twnc: Water inertia time constant (<i>Twnc</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:twng: Water tunnel and surge chamber inertia time constant (<i>Twng</i>) (&gt;= 0). Typical value = 3. Default: 0
	:tx: Derivative feedback gain (<i>Tx</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:va: Maximum gate opening velocity (<i>Va</i>).  Unit = PU / s.  Typical value = 0,06. Default: 0.0
	:valvmax: Maximum gate opening (<i>ValvMax</i>) (&gt; GovHydroFrancis.valvmin).  Typical value = 1,1. Default: 0.0
	:valvmin: Minimum gate opening (<i>ValvMin</i>) (&lt; GovHydroFrancis.valvmax).  Typical value = 0. Default: 0.0
	:vc: Maximum gate closing velocity (<i>Vc</i>).  Unit = PU / s.  Typical value = -0,06. Default: 0.0
	:waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (<i>Tflag</i>). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical value = false. Default: False
	:zsfc: Head of upper water level with respect to the level of penstock (<i>Zsfc</i>). Unit = km.  Typical value = 0,025. Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'am': [cgmesProfile.DY.value, ],
						'av0': [cgmesProfile.DY.value, ],
						'av1': [cgmesProfile.DY.value, ],
						'bp': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'etamax': [cgmesProfile.DY.value, ],
						'governorControl': [cgmesProfile.DY.value, ],
						'h1': [cgmesProfile.DY.value, ],
						'h2': [cgmesProfile.DY.value, ],
						'hn': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kt': [cgmesProfile.DY.value, ],
						'qc0': [cgmesProfile.DY.value, ],
						'qn': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'ts': [cgmesProfile.DY.value, ],
						'twnc': [cgmesProfile.DY.value, ],
						'twng': [cgmesProfile.DY.value, ],
						'tx': [cgmesProfile.DY.value, ],
						'va': [cgmesProfile.DY.value, ],
						'valvmax': [cgmesProfile.DY.value, ],
						'valvmin': [cgmesProfile.DY.value, ],
						'vc': [cgmesProfile.DY.value, ],
						'waterTunnelSurgeChamberSimulation': [cgmesProfile.DY.value, ],
						'zsfc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, am = 0.0, av0 = 0.0, av1 = 0.0, bp = 0.0, db1 = 0.0, etamax = 0.0, governorControl = None, h1 = 0.0, h2 = 0.0, hn = 0.0, kc = 0.0, kg = 0.0, kt = 0.0, qc0 = 0.0, qn = 0.0, ta = 0, td = 0, ts = 0, twnc = 0, twng = 0, tx = 0, va = 0.0, valvmax = 0.0, valvmin = 0.0, vc = 0.0, waterTunnelSurgeChamberSimulation = False, zsfc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.am = am
		self.av0 = av0
		self.av1 = av1
		self.bp = bp
		self.db1 = db1
		self.etamax = etamax
		self.governorControl = governorControl
		self.h1 = h1
		self.h2 = h2
		self.hn = hn
		self.kc = kc
		self.kg = kg
		self.kt = kt
		self.qc0 = qc0
		self.qn = qn
		self.ta = ta
		self.td = td
		self.ts = ts
		self.twnc = twnc
		self.twng = twng
		self.tx = tx
		self.va = va
		self.valvmax = valvmax
		self.valvmin = valvmin
		self.vc = vc
		self.waterTunnelSurgeChamberSimulation = waterTunnelSurgeChamberSimulation
		self.zsfc = zsfc
		
	def __str__(self):
		str = 'class=GovHydroFrancis\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
