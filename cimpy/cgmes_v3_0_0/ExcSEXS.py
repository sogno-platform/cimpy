from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSEXS(ExcitationSystemDynamics):
	'''
	Simplified excitation system.

	:tatb: Gain reduction ratio of lag-lead element (<i>[Ta / Tb]</i>).  Typical value = 0,1. Default: 0.0
	:tb: Denominator time constant of lag-lead block (<i>Tb</i>) (&gt;= 0).  Typical value = 10. Default: 0
	:k: Gain (<i>K</i>) (&gt; 0).  Typical value = 100. Default: 0.0
	:te: Time constant of gain block (<i>Te</i>) (&gt; 0).  Typical value = 0,05. Default: 0
	:emin: Minimum field voltage output (<i>Emin</i>) (&lt; ExcSEXS.emax).  Typical value = -5. Default: 0.0
	:emax: Maximum field voltage output (<i>Emax</i>) (&gt; ExcSEXS.emin).  Typical value = 5. Default: 0.0
	:kc: PI controller gain (<i>Kc</i>) (&gt; 0 if ExcSEXS.tc &gt; 0).  Typical value = 0,08. Default: 0.0
	:tc: PI controller phase lead time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:efdmin: Field voltage clipping minimum limit (<i>Efdmin</i>) (&lt; ExcSEXS.efdmax).  Typical value = -5. Default: 0.0
	:efdmax: Field voltage clipping maximum limit (<i>Efdmax</i>) (&gt; ExcSEXS.efdmin).  Typical value = 5. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tatb': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'emin': [cgmesProfile.DY.value, ],
						'emax': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'efdmin': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tatb = 0.0, tb = 0, k = 0.0, te = 0, emin = 0.0, emax = 0.0, kc = 0.0, tc = 0, efdmin = 0.0, efdmax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tatb = tatb
		self.tb = tb
		self.k = k
		self.te = te
		self.emin = emin
		self.emax = emax
		self.kc = kc
		self.tc = tc
		self.efdmin = efdmin
		self.efdmax = efdmax
		
	def __str__(self):
		str = 'class=ExcSEXS\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
