from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSEXS(ExcitationSystemDynamics):
	'''
	Simplified Excitation System Model.

	:tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1. Default: 0.0
	:tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 0.0
	:k: Gain (K) (>0).  Typical Value = 100. Default: 0.0
	:te: Time constant of gain block (Te).  Typical Value = 0.05. Default: 0.0
	:emin: Minimum field voltage output (Emin).  Typical Value = -5. Default: 0.0
	:emax: Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
	:kc: PI controller gain (Kc).  Typical Value = 0.08. Default: 0.0
	:tc: PI controller phase lead time constant (Tc).  Typical Value = 0. Default: 0.0
	:efdmin: Field voltage clipping minimum limit (Efdmin).  Typical Value = -5. Default: 0.0
	:efdmax: Field voltage clipping maximum limit (Efdmax).  Typical Value = 5. Default: 0.0
		'''

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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tatb = 0.0, tb = 0.0, k = 0.0, te = 0.0, emin = 0.0, emax = 0.0, kc = 0.0, tc = 0.0, efdmin = 0.0, efdmax = 0.0,  *args, **kw_args):
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
