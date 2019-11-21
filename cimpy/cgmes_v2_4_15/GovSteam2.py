from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam2(TurbineGovernorDynamics):
	'''
	Simplified governor model.

	:k: Governor gain (reciprocal of droop) (K).  Typical Value = 20. Default: 0.0
	:dbf: Frequency dead band (DBF).  Typical Value = 0. Default: 0.0
	:t1: Governor lag time constant (T) (>0).  Typical Value = 0.45. Default: 0.0
	:t2: Governor lead time constant (T) (may be 0).  Typical Value = 0. Default: 0.0
	:pmax: Maximum fuel flow (P).  Typical Value = 1. Default: 0.0
	:pmin: Minimum fuel flow (P).  Typical Value = 0. Default: 0.0
	:mxef: Fuel flow maximum positive error value (MX).  Typical Value = 1. Default: 0.0
	:mnef: Fuel flow maximum negative error value (MN).  Typical Value = -1. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'dbf': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'mxef': [cgmesProfile.DY.value, ],
						'mnef': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, k = 0.0, dbf = 0.0, t1 = 0.0, t2 = 0.0, pmax = 0.0, pmin = 0.0, mxef = 0.0, mnef = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k = k
		self.dbf = dbf
		self.t1 = t1
		self.t2 = t2
		self.pmax = pmax
		self.pmin = pmin
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovSteam2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
