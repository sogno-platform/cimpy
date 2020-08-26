from cimpy.cgmes_v2_4_15.LoadDynamics import LoadDynamics


class LoadGenericNonLinear(LoadDynamics):
	'''
	These load models (known also as generic non-linear dynamic (GNLD) load models) can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as they can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

	:genericNonLinearLoadModelType: Type of generic non-linear load model. Default: 
	:pt: Dynamic portion of active load (P). Default: 
	:qt: Dynamic portion of reactive load (Q). Default: 
	:tp: Time constant of lag function of active power (T). Default: 
	:tq: Time constant of lag function of reactive power (T). Default: 
	:ls: Steady state voltage index for active power (LS). Default: 
	:lt: Transient voltage index for active power (LT). Default: 
	:bs: Steady state voltage index for reactive power (BS). Default: 
	:bt: Transient voltage index for reactive power (BT). Default: 
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

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, genericNonLinearLoadModelType = , pt = , qt = , tp = , tq = , ls = , lt = , bs = , bt = ,  *args, **kw_args):
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
