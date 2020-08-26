from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC4A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

	:vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 
	:vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 10. Default: 
	:ka: Voltage regulator gain (Ka).  Typical Value = 200. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.015. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5.64. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.53. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = , vimin = , tc = , tb = , ka = , ta = , vrmax = , vrmin = , kc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vimax = vimax
		self.vimin = vimin
		self.tc = tc
		self.tb = tb
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kc = kc
		
	def __str__(self):
		str = 'class=ExcAC4A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
