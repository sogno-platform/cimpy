from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST1A(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type ST1A model. This model represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier.  The maximum exciter voltage available from such systems is directly related to the generator terminal voltage. Reference: IEEE 421.5-2005, 7.1.

	:ilr: Exciter output current limit reference (<i>I</i><i><sub>LR</sub></i><i>)</i>.  Typical value = 0. Default: 0.0
	:ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 190. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0). Typical value = 0,08. Default: 0.0
	:kf: Excitation control system stabilizer gains (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:klr: Exciter output current limiter gain (<i>K</i><i><sub>LR</sub></i>).  Typical value = 0. Default: 0.0
	:pssin: Selector of the Power System Stabilizer (PSS) input (<i>PSSin</i>). true = PSS input (<i>Vs</i>) added to error signal false = PSS input (<i>Vs</i>) added to voltage regulator output. Typical value = true. Default: False
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 10. Default: 0
	:tb1: Voltage regulator time constant (<i>T</i><i><sub>B1</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tc1: Voltage regulator time constant (<i>T</i><i><sub>C1</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:uelin: Selector of the connection of the UEL input (<i>UELin</i>).  Typical value = ignoreUELsignal. Default: None
	:vamax: Maximum voltage regulator output (<i>V</i><i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 14,5. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>V</i><i><sub>AMIN</sub></i>) (&lt; 0).  Typical value = -14,5. Default: 0.0
	:vimax: Maximum voltage regulator input limit (<i>V</i><i><sub>IMAX</sub></i>) (&gt; 0).  Typical value = 999. Default: 0.0
	:vimin: Minimum voltage regulator input limit (<i>V</i><i><sub>IMIN</sub></i>) (&lt; 0).  Typical value = -999. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 7,8. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -6,7. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'pssin': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tc1': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = 0.0, ka = 0.0, kc = 0.0, kf = 0.0, klr = 0.0, pssin = False, ta = 0, tb = 0, tb1 = 0, tc = 0, tc1 = 0, tf = 0, uelin = None, vamax = 0.0, vamin = 0.0, vimax = 0.0, vimin = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.ka = ka
		self.kc = kc
		self.kf = kf
		self.klr = klr
		self.pssin = pssin
		self.ta = ta
		self.tb = tb
		self.tb1 = tb1
		self.tc = tc
		self.tc1 = tc1
		self.tf = tf
		self.uelin = uelin
		self.vamax = vamax
		self.vamin = vamin
		self.vimax = vimax
		self.vimin = vimin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
