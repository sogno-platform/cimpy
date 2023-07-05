from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST6B(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response. Reference: IEEE 421.5-2005, 7.6.

	:ilr: Exciter output current limit reference (<i>I</i><i><sub>LR</sub></i>) (&gt; 0).  Typical value = 4,164. Default: 0.0
	:kci: Exciter output current limit adjustment (<i>K</i><i><sub>CI</sub></i>) (&gt; 0).  Typical value = 1,0577. Default: 0.0
	:kff: Pre-control gain constant of the inner loop field regulator (<i>K</i><i><sub>FF</sub></i>). Typical value = 1. Default: 0.0
	:kg: Feedback gain constant of the inner loop field regulator (<i>K</i><i><sub>G</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kia: Voltage regulator integral gain (<i>K</i><i><sub>IA</sub></i>) (&gt; 0).  Typical value = 45,094. Default: 0.0
	:klr: Exciter output current limiter gain (<i>K</i><i><sub>LR</sub></i>) (&gt; 0).  Typical value = 17,33. Default: 0.0
	:km: Forward gain constant of the inner loop field regulator (<i>K</i><i><sub>M</sub></i>).  Typical value = 1. Default: 0.0
	:kpa: Voltage regulator proportional gain (<u>K</u><u><sub>PA</sub></u>) (&gt; 0).  Typical value = 18,038. Default: 0.0
	:oelin: OEL input selector (<i>OELin</i>). Typical value = noOELinput. Default: None
	:tg: Feedback time constant of inner loop field voltage regulator (<i>T</i><i><sub>G</sub></i>) (&gt;= 0). Typical value = 0,02. Default: 0
	:vamax: Maximum voltage regulator output (V<i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 4,81. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>V</i><i><sub>AMIN</sub></i>) (&lt; 0).  Typical value = -3,85. Default: 0.0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 4,81. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -3,85. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'kci': [cgmesProfile.DY.value, ],
						'kff': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kia': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'kpa': [cgmesProfile.DY.value, ],
						'oelin': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = 0.0, kci = 0.0, kff = 0.0, kg = 0.0, kia = 0.0, klr = 0.0, km = 0.0, kpa = 0.0, oelin = None, tg = 0, vamax = 0.0, vamin = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.kci = kci
		self.kff = kff
		self.kg = kg
		self.kia = kia
		self.klr = klr
		self.km = km
		self.kpa = kpa
		self.oelin = oelin
		self.tg = tg
		self.vamax = vamax
		self.vamin = vamin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST6B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
