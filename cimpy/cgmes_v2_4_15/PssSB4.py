from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSB4(PowerSystemStabilizerDynamics):
	'''
	Power sensitive stabilizer model.

	:tt: Time constant (Tt). Default: 
	:kx: Gain (Kx). Default: 
	:tx2: Time constant (Tx2). Default: 
	:ta: Time constant (Ta). Default: 
	:tx1: Reset time constant (Tx1). Default: 
	:tb: Time constant (Tb). Default: 
	:tc: Time constant (Tc). Default: 
	:td: Time constant (Td). Default: 
	:te: Time constant (Te). Default: 
	:vsmax: Limiter (Vsmax). Default: 
	:vsmin: Limiter (Vsmin). Default: 
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

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, tt = , kx = , tx2 = , ta = , tx1 = , tb = , tc = , td = , te = , vsmax = , vsmin = ,  *args, **kw_args):
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
