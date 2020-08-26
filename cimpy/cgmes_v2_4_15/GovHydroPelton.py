from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPelton(TurbineGovernorDynamics):
	'''
	Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and surge chamber. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is located under the GovHydroFrancis class.

	:av0: Area of the surge tank (A). Unit = m. Typical Value = 30. Default: 
	:av1: Area of the compensation tank (A). Unit = m. Typical Value = 700. Default: 
	:bp: Droop (bp).  Typical Value = 0.05. Default: 
	:db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0. Default: 
	:db2: Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01. Default: 
	:h1: Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value = 4. Default: 
	:h2: Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40. Default: 
	:hn: Rated hydraulic head (H).  Unit = m. Typical Value = 250. Default: 
	:kc: Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025. Default: 
	:kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025. Default: 
	:qc0: No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05. Default: 
	:qn: Rated flow (Q). Unit = m/s. Typical Value = 40. Default: 
	:simplifiedPelton: Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation false = enable of complete Pelton model simulation (non linear gain). Typical Value = false. Default: 
	:staticCompensating: Static compensating characteristic (Cflag). true = enable of static compensating characteristic  false = inhibit of static compensating characteristic. Typical Value = false. Default: 
	:ta: Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3. Default: 
	:ts: Gate servo time constant (Ts).  Typical Value = 0.15. Default: 
	:tv: Servomotor integrator time constant (TV).  Typical Value = 0.3. Default: 
	:twnc: Water inertia time constant (Twnc).  Typical Value = 1. Default: 
	:twng: Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3. Default: 
	:tx: Electronic integrator time constant (Tx).  Typical Value = 0.5. Default: 
	:va: Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016. Default: 
	:valvmax: Maximum gate opening (ValvMax).  Typical Value = 1. Default: 
	:valvmin: Minimum gate opening (ValvMin).  Typical Value = 0. Default: 
	:vav: Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017. Default: 
	:vc: Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016. Default: 
	:vcv: Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017. Default: 
	:waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical Value = false. Default: 
	:zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'av0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'av1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'bp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'db1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'db2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'h1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'h2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'hn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qc0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'simplifiedPelton': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'staticCompensating': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ts': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tv': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'twnc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'twng': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tx': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'va': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'valvmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'valvmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vav': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcv': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'waterTunnelSurgeChamberSimulation': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'zsfc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, av0 = , av1 = , bp = , db1 = , db2 = , h1 = , h2 = , hn = , kc = , kg = , qc0 = , qn = , simplifiedPelton = , staticCompensating = , ta = , ts = , tv = , twnc = , twng = , tx = , va = , valvmax = , valvmin = , vav = , vc = , vcv = , waterTunnelSurgeChamberSimulation = , zsfc = ,  *args, **kw_args):
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
		str = 'class=GovHydroPelton\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
