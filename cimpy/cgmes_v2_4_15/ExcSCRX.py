from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSCRX(ExcitationSystemDynamics):
	'''
	Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem.

	:tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is not defined explicitly.  Typical Value = 0.1. Default: 0.0
	:tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 0.0
	:k: Gain (K) (>0).  Typical Value = 200. Default: 0.0
	:te: Time constant of gain block (Te) (>0).  Typical Value = 0.02. Default: 0.0
	:emin: Minimum field voltage output (Emin).  Typical Value = 0. Default: 0.0
	:emax: Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
	:cswitch: Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage. Default: False
	:rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance (RcRfd).  Typical Value = 0. Default: 0.0
		'''

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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tatb = 0.0, tb = 0.0, k = 0.0, te = 0.0, emin = 0.0, emax = 0.0, cswitch = False, rcrfd = 0.0,  *args, **kw_args):
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
