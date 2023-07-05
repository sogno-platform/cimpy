from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST3(TurbineGovernorDynamics):
	'''
	Generic turbogas with acceleration and temperature controller.

	:bp: Droop (<i>bp</i>).  Typical value = 0,05. Default: 0.0
	:tg: Time constant of speed governor (<i>Tg</i>) (&gt;= 0).  Typical value = 0,05. Default: 0
	:rcmx: Maximum fuel flow (<i>RCMX</i>).  Typical value = 1. Default: 0.0
	:rcmn: Minimum fuel flow (<i>RCMN</i>).  Typical value = -0,1. Default: 0.0
	:ky: Coefficient of transfer function of fuel valve positioner (<i>Ky</i>).  Typical value = 1. Default: 0.0
	:ty: Time constant of fuel valve positioner (<i>Ty</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
	:tac: Fuel control time constant (<i>Tac</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:kac: Fuel system feedback (<i>K</i><i><sub>AC</sub></i>).  Typical value = 0. Default: 0.0
	:tc: Compressor discharge volume time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
	:bca: Acceleration limit set-point (<i>Bca</i>).  Unit = 1/s.  Typical value = 0,01. Default: 0.0
	:kca: Acceleration control integral gain (<i>Kca</i>). Unit = 1/s.  Typical value = 100. Default: 0.0
	:dtc: Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (<i>deltaTc</i>).  Typical value = 390. Default: 0.0
	:ka: Minimum fuel flow (<i>Ka</i>).  Typical value = 0,23. Default: 0.0
	:tsi: Time constant of radiation shield (<i>Tsi</i>) (&gt;= 0).  Typical value = 15. Default: 0
	:ksi: Gain of radiation shield (<i>Ksi</i>).  Typical value = 0,8. Default: 0.0
	:ttc: Time constant of thermocouple (<i>Ttc</i>) (&gt;= 0).  Typical value = 2,5. Default: 0
	:tfen: Turbine rated exhaust temperature correspondent to Pm=1 PU (<i>Tfen</i>).  Typical value = 540. Default: 0.0
	:td: Temperature controller derivative gain (<i>Td</i>) (&gt;= 0).  Typical value = 3,3. Default: 0
	:tt: Temperature controller integration rate (<i>Tt</i>).  Typical value = 250. Default: 0.0
	:mxef: Fuel flow maximum positive error value (<i>MXef</i>).  Typical value = 0,05. Default: 0.0
	:mnef: Fuel flow maximum negative error value (<i>MNef</i>).  Typical value = -0,05. Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'bp': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'rcmx': [cgmesProfile.DY.value, ],
						'rcmn': [cgmesProfile.DY.value, ],
						'ky': [cgmesProfile.DY.value, ],
						'ty': [cgmesProfile.DY.value, ],
						'tac': [cgmesProfile.DY.value, ],
						'kac': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'bca': [cgmesProfile.DY.value, ],
						'kca': [cgmesProfile.DY.value, ],
						'dtc': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'tsi': [cgmesProfile.DY.value, ],
						'ksi': [cgmesProfile.DY.value, ],
						'ttc': [cgmesProfile.DY.value, ],
						'tfen': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'mxef': [cgmesProfile.DY.value, ],
						'mnef': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, bp = 0.0, tg = 0, rcmx = 0.0, rcmn = 0.0, ky = 0.0, ty = 0, tac = 0, kac = 0.0, tc = 0, bca = 0.0, kca = 0.0, dtc = 0.0, ka = 0.0, tsi = 0, ksi = 0.0, ttc = 0, tfen = 0.0, td = 0, tt = 0.0, mxef = 0.0, mnef = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bp = bp
		self.tg = tg
		self.rcmx = rcmx
		self.rcmn = rcmn
		self.ky = ky
		self.ty = ty
		self.tac = tac
		self.kac = kac
		self.tc = tc
		self.bca = bca
		self.kca = kca
		self.dtc = dtc
		self.ka = ka
		self.tsi = tsi
		self.ksi = ksi
		self.ttc = ttc
		self.tfen = tfen
		self.td = td
		self.tt = tt
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovGAST3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
