from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroIEEE0(TurbineGovernorDynamics):
	'''
	IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic and Electro-Hydraulic turbine governors, with our without steam feedback. Typical values given are for Mechanical-Hydraulic.  Ref

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
	:k: Governor gain (K. Default: 0.0
	:t1: Governor lag time constant (T1).  Typical Value = 0.25. Default: 0.0
	:t2: Governor lead time constant (T2.  Typical Value = 0. Default: 0.0
	:t3: Gate actuator time constant (T3).  Typical Value = 0.1. Default: 0.0
	:t4: Water starting time (T4). Default: 0.0
	:pmax: Gate maximum (Pmax). Default: 0.0
	:pmin: Gate minimum (Pmin). Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, k = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, pmax = 0.0, pmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.k = k
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.pmax = pmax
		self.pmin = pmin
		
	def __str__(self):
		str = 'class=GovHydroIEEE0\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
