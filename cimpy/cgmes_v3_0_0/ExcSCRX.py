from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSCRX(ExcitationSystemDynamics):
	'''
	Simple excitation system with generic characteristics typical of many excitation systems; intended for use where negative field current could be a problem.

	:tatb: Gain reduction ratio of lag-lead element ([<i>Ta</i> / <i>Tb</i>]). The parameter <i>Ta</i> is not defined explicitly.  Typical value = 0.1. Default: 0.0
	:tb: Denominator time constant of lag-lead block (<i>Tb</i>) (&gt;= 0).  Typical value = 10. Default: 0
	:k: Gain (<i>K</i>) (&gt; 0).  Typical value = 200. Default: 0.0
	:te: Time constant of gain block (<i>Te</i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:emin: Minimum field voltage output (<i>Emin</i>) (&lt; ExcSCRX.emax).  Typical value = 0. Default: 0.0
	:emax: Maximum field voltage output (<i>Emax</i>) (&gt; ExcSCRX.emin).  Typical value = 5. Default: 0.0
	:cswitch: Power source switch (<i>Cswitch</i>). true = fixed voltage of 1.0 PU false = generator terminal voltage. Default: False
	:rcrfd: Ratio of field discharge resistance to field winding resistance ([<i>rc / rfd]</i>).  Typical value = 0. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tatb': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'emin': [cgmesProfile.DY.value, ],
						'emax': [cgmesProfile.DY.value, ],
						'cswitch': [cgmesProfile.DY.value, ],
						'rcrfd': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tatb = 0.0, tb = 0, k = 0.0, te = 0, emin = 0.0, emax = 0.0, cswitch = False, rcrfd = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tatb = tatb
		self.tb = tb
		self.k = k
		self.te = te
		self.emin = emin
		self.emax = emax
		self.cswitch = cswitch
		self.rcrfd = rcrfd
		
	def __str__(self):
		str = 'class=ExcSCRX\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
