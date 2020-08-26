from cimpy.cgmes_v2_4_15.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
	'''
	This model can be derived from UnderexcLimIEEE2. The limit characteristic (look -up table) is a single straight-line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).

	:q0: Segment Q initial point (Q0).  Typical Value = -0.31. Default: 
	:q1: Segment Q end point (Q1).  Typical Value = -0.1. Default: 
	:p0: Segment P initial point (P0).  Typical Value = 0. Default: 
	:p1: Segment P end point (P1).  Typical Value = 1. Default: 
	:kui: Gain Under excitation limiter (Kui).  Typical Value = 0.1. Default: 
	:vuimin: Minimum error signal (V).  Typical Value = 0. Default: 
	:vuimax: Maximum error signal (V).  Typical Value = 1. Default: 
		'''

	cgmesProfile = UnderexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'q0': [cgmesProfile.DY.value, ],
						'q1': [cgmesProfile.DY.value, ],
						'p0': [cgmesProfile.DY.value, ],
						'p1': [cgmesProfile.DY.value, ],
						'kui': [cgmesProfile.DY.value, ],
						'vuimin': [cgmesProfile.DY.value, ],
						'vuimax': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class UnderexcitationLimiterDynamics: \n' + UnderexcitationLimiterDynamics.__doc__ 

	def __init__(self, q0 = , q1 = , p0 = , p1 = , kui = , vuimin = , vuimax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.q0 = q0
		self.q1 = q1
		self.p0 = p0
		self.p1 = p1
		self.kui = kui
		self.vuimin = vuimin
		self.vuimax = vuimax
		
	def __str__(self):
		str = 'class=UnderexcLim2Simplified\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
