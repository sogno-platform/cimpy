from cimpy.cgmes_v2_4_15_flat.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLimIEEE(OverexcitationLimiterDynamics):
	'''
	The over excitation limiter model is intended to represent the significant features of OELs necessary for some large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely applied with attainable data from generator owners. An attempt to include all variations in the functionality of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level of application insufficient for the studies for which they are intended.  Reference: IEEE OEL 421.5-2005 Section 9.

	:itfpu: OEL timed field current limiter pickup level (I).  Typical Value = 1.05. Default: 0.0
	:ifdmax: OEL instantaneous field current limit (I).  Typical Value = 1.5. Default: 0.0
	:ifdlim: OEL timed field current limit (I).  Typical Value = 1.05. Default: 0.0
	:hyst: OEL pickup/drop-out hysteresis (HYST).  Typical Value = 0.03. Default: 0.0
	:kcd: OEL cooldown gain (K).  Typical Value = 1. Default: 0.0
	:kramp: OEL ramped limit rate (K).  Unit = PU/sec.  Typical Value = 10. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'itfpu': [cgmesProfile.DY.value, ],
						'ifdmax': [cgmesProfile.DY.value, ],
						'ifdlim': [cgmesProfile.DY.value, ],
						'hyst': [cgmesProfile.DY.value, ],
						'kcd': [cgmesProfile.DY.value, ],
						'kramp': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, itfpu = 0.0, ifdmax = 0.0, ifdlim = 0.0, hyst = 0.0, kcd = 0.0, kramp = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.itfpu = itfpu
		self.ifdmax = ifdmax
		self.ifdlim = ifdlim
		self.hyst = hyst
		self.kcd = kcd
		self.kramp = kramp
		
	def __str__(self):
		str = 'class=OverexcLimIEEE\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
