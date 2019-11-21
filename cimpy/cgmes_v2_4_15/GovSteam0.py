from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam0(TurbineGovernorDynamics):
	'''
	A simplified steam turbine governor model.

	:mwbase: Base for power values (MWbase)  (>0).  Unit = MW. Default: 0.0
	:r: Permanent droop (R).  Typical Value = 0.05. Default: 0.0
	:t1: Steam bowl time constant (T1).  Typical Value = 0.5. Default: 0.0
	:vmax: Maximum valve position, PU of mwcap (Vmax).  Typical Value = 1. Default: 0.0
	:vmin: Minimum valve position, PU of mwcap (Vmin).  Typical Value = 0. Default: 0.0
	:t2: Numerator time constant of T2/T3 block (T2).  Typical Value = 3. Default: 0.0
	:t3: Reheater time constant (T3).  Typical Value = 10. Default: 0.0
	:dt: Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical Value = 0. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'dt': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, r = 0.0, t1 = 0.0, vmax = 0.0, vmin = 0.0, t2 = 0.0, t3 = 0.0, dt = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.t1 = t1
		self.vmax = vmax
		self.vmin = vmin
		self.t2 = t2
		self.t3 = t3
		self.dt = dt
		
	def __str__(self):
		str = 'class=GovSteam0\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
