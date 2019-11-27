from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSB4(PowerSystemStabilizerDynamics):
	'''
	Power sensitive stabilizer model.

	:tt: Time constant (Tt). Default: 0.0
	:kx: Gain (Kx). Default: 0.0
	:tx2: Time constant (Tx2). Default: 0.0
	:ta: Time constant (Ta). Default: 0.0
	:tx1: Reset time constant (Tx1). Default: 0.0
	:tb: Time constant (Tb). Default: 0.0
	:tc: Time constant (Tc). Default: 0.0
	:td: Time constant (Td). Default: 0.0
	:te: Time constant (Te). Default: 0.0
	:vsmax: Limiter (Vsmax). Default: 0.0
	:vsmin: Limiter (Vsmin). Default: 0.0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'kx': [cgmesProfile.DY.value, ],
						'tx2': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tx1': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vsmax': [cgmesProfile.DY.value, ],
						'vsmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, tt = 0.0, kx = 0.0, tx2 = 0.0, ta = 0.0, tx1 = 0.0, tb = 0.0, tc = 0.0, td = 0.0, te = 0.0, vsmax = 0.0, vsmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tt = tt
		self.kx = kx
		self.tx2 = tx2
		self.ta = ta
		self.tx1 = tx1
		self.tb = tb
		self.tc = tc
		self.td = td
		self.te = te
		self.vsmax = vsmax
		self.vsmin = vsmin
		
	def __str__(self):
		str = 'class=PssSB4\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
