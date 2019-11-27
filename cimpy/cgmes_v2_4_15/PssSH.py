from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSH(PowerSystemStabilizerDynamics):
	'''
	Model for Siemens "H infinity" power system stabilizer with generator electrical power input.

	:k: Main gain (K).  Typical Value = 1. Default: 0.0
	:k0: Gain 0 (K0).  Typical Value = 0.012. Default: 0.0
	:k1: Gain 1 (K1).  Typical Value = 0.488. Default: 0.0
	:k2: Gain 2 (K2).  Typical Value = 0.064. Default: 0.0
	:k3: Gain 3 (K3).  Typical Value = 0.224. Default: 0.0
	:k4: Gain 4 (K4).  Typical Value = 0.1. Default: 0.0
	:td: Input time constant (Td).  Typical Value = 10. Default: 0.0
	:t1: Time constant 1 (T1).  Typical Value = 0.076. Default: 0.0
	:t2: Time constant 2 (T2).  Typical Value = 0.086. Default: 0.0
	:t3: Time constant 3 (T3).   Typical Value = 1.068. Default: 0.0
	:t4: Time constant 4 (T4).  Typical Value = 1.913. Default: 0.0
	:vsmax: Output maximum limit (Vsmax).  Typical Value = 0.1. Default: 0.0
	:vsmin: Output minimum limit (Vsmin).  Typical Value = -0.1. Default: 0.0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'k0': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'k4': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'vsmax': [cgmesProfile.DY.value, ],
						'vsmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, k = 0.0, k0 = 0.0, k1 = 0.0, k2 = 0.0, k3 = 0.0, k4 = 0.0, td = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, vsmax = 0.0, vsmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k = k
		self.k0 = k0
		self.k1 = k1
		self.k2 = k2
		self.k3 = k3
		self.k4 = k4
		self.td = td
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.vsmax = vsmax
		self.vsmin = vsmin
		
	def __str__(self):
		str = 'class=PssSH\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
