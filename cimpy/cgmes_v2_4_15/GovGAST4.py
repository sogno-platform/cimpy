from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST4(TurbineGovernorDynamics):
	'''
	Generic turbogas.

	:bp: Droop (bp).  Typical Value = 0.05. Default: 0.0
	:tv: Time constant of fuel valve positioner (T).  Typical Value = 0.1. Default: 0.0
	:ta: Maximum gate opening velocity (T).  Typical Value = 3. Default: 0.0
	:tc: Maximum gate closing velocity (T).  Typical Value = 0.5. Default: 0.0
	:tcm: Fuel control time constant (T).  Typical Value = 0.1. Default: 0.0
	:ktm: Compressor gain (K).  Typical Value = 0. Default: 0.0
	:tm: Compressor discharge volume time constant (T).  Typical Value = 0.2. Default: 0.0
	:rymx: Maximum valve opening (RYMX).  Typical Value = 1.1. Default: 0.0
	:rymn: Minimum valve opening (RYMN).  Typical Value = 0. Default: 0.0
	:mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 0.0
	:mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'bp': [cgmesProfile.DY.value, ],
						'tv': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tcm': [cgmesProfile.DY.value, ],
						'ktm': [cgmesProfile.DY.value, ],
						'tm': [cgmesProfile.DY.value, ],
						'rymx': [cgmesProfile.DY.value, ],
						'rymn': [cgmesProfile.DY.value, ],
						'mxef': [cgmesProfile.DY.value, ],
						'mnef': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, bp = 0.0, tv = 0.0, ta = 0.0, tc = 0.0, tcm = 0.0, ktm = 0.0, tm = 0.0, rymx = 0.0, rymn = 0.0, mxef = 0.0, mnef = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bp = bp
		self.tv = tv
		self.ta = ta
		self.tc = tc
		self.tcm = tcm
		self.ktm = ktm
		self.tm = tm
		self.rymx = rymx
		self.rymn = rymn
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovGAST4\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
