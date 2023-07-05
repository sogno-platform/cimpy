from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST3A(ExcitationSystemDynamics):
	'''
	Modified IEEE ST3A static excitation system with added speed multiplier.

	:vimax: Maximum voltage regulator input limit (<i>Vimax</i>) (&gt; 0).  Typical value = 0,2. Default: 0.0
	:vimin: Minimum voltage regulator input limit (<i>Vimin</i>) (&lt; 0).  Typical value = -0,2. Default: 0.0
	:kj: AVR gain (<i>Kj</i>) (&gt; 0).  Typical value = 200. Default: 0.0
	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 6,67. Default: 0
	:tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:efdmax: Maximum AVR output (<i>Efdmax</i>) (&gt;= 0).  Typical value = 6,9. Default: 0.0
	:km: Forward gain constant of the inner loop field regulator (<i>Km</i>) (&gt; 0).  Typical value = 7,04. Default: 0.0
	:tm: Forward time constant of inner loop field regulator (<i>Tm</i>) (&gt; 0).  Typical value = 1. Default: 0
	:vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0).  Typical value = -1. Default: 0.0
	:kg: Feedback gain constant of the inner loop field regulator (<i>Kg</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kp: Potential source gain (<i>K</i><i><sub>p</sub></i>) (&gt; 0).  Typical value = 4,37. Default: 0.0
	:thetap: Potential circuit phase angle (<i>theta</i><i><sub>p</sub></i>).  Typical value = 20. Default: 0.0
	:ki: Potential circuit gain coefficient (<i>K</i><i><sub>i</sub></i>) (&gt;= 0).  Typical value = 4,83. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0). Typical value = 1,1. Default: 0.0
	:xl: Reactance associated with potential source (<i>Xl</i>) (&gt;= 0).  Typical value = 0,09. Default: 0.0
	:vbmax: Maximum excitation voltage (<i>Vbmax</i>) (&gt; 0).  Typical value = 8,63. Default: 0.0
	:vgmax: Maximum inner loop feedback voltage (<i>Vgmax</i>) (&gt;= 0).  Typical value = 6,53. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
	:ks1: Coefficient to allow different usage of the model-speed coefficient (<i>Ks1</i>).  Typical value = 0. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'kj': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'tm': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'thetap': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'xl': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						'vgmax': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = 0.0, vimin = 0.0, kj = 0.0, tb = 0, tc = 0, efdmax = 0.0, km = 0.0, tm = 0, vrmax = 0.0, vrmin = 0.0, kg = 0.0, kp = 0.0, thetap = 0.0, ki = 0.0, kc = 0.0, xl = 0.0, vbmax = 0.0, vgmax = 0.0, ks = 0.0, ks1 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vimax = vimax
		self.vimin = vimin
		self.kj = kj
		self.tb = tb
		self.tc = tc
		self.efdmax = efdmax
		self.km = km
		self.tm = tm
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kg = kg
		self.kp = kp
		self.thetap = thetap
		self.ki = ki
		self.kc = kc
		self.xl = xl
		self.vbmax = vbmax
		self.vgmax = vgmax
		self.ks = ks
		self.ks1 = ks1
		
	def __str__(self):
		str = 'class=ExcST3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
