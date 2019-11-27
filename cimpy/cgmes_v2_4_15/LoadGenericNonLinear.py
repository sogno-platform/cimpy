from cimpy.cgmes_v2_4_15.LoadDynamics import LoadDynamics


class LoadGenericNonLinear(LoadDynamics):
	'''
	These load models (known also as generic non-linear dynamic (GNLD) load models) can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as they can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

	:genericNonLinearLoadModelType: Type of generic non-linear load model. Default: None
	:pt: Dynamic portion of active load (P). Default: 0.0
	:qt: Dynamic portion of reactive load (Q). Default: 0.0
	:tp: Time constant of lag function of active power (T). Default: 0.0
	:tq: Time constant of lag function of reactive power (T). Default: 0.0
	:ls: Steady state voltage index for active power (LS). Default: 0.0
	:lt: Transient voltage index for active power (LT). Default: 0.0
	:bs: Steady state voltage index for reactive power (BS). Default: 0.0
	:bt: Transient voltage index for reactive power (BT). Default: 0.0
		'''

	cgmesProfile = LoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'genericNonLinearLoadModelType': [cgmesProfile.DY.value, ],
						'pt': [cgmesProfile.DY.value, ],
						'qt': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'tq': [cgmesProfile.DY.value, ],
						'ls': [cgmesProfile.DY.value, ],
						'lt': [cgmesProfile.DY.value, ],
						'bs': [cgmesProfile.DY.value, ],
						'bt': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, genericNonLinearLoadModelType = None, pt = 0.0, qt = 0.0, tp = 0.0, tq = 0.0, ls = 0.0, lt = 0.0, bs = 0.0, bt = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.genericNonLinearLoadModelType = genericNonLinearLoadModelType
		self.pt = pt
		self.qt = qt
		self.tp = tp
		self.tq = tq
		self.ls = ls
		self.lt = lt
		self.bs = bs
		self.bt = bt
		
	def __str__(self):
		str = 'class=LoadGenericNonLinear\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
