from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST5B(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type ST5B model. The type ST5B excitation system is a variation of the type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The block diagram in the IEEE 421.5 standard has input signal <i>Vc </i>and does not indicate the summation point with <i>Vref</i>. The implementation of the ExcIEEEST5B shall consider summation point with <i>Vref</i>. Reference: IEEE 421.5-2005, 7.5.

	:kr: Regulator gain (<i>K</i><i><sub>R</sub></i>) (&gt; 0).  Typical value = 200. Default: 0.0
	:t1: Firing circuit time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0,004. Default: 0
	:kc: Rectifier regulation factor (<i>K</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0,004. Default: 0.0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -4. Default: 0.0
	:tc1: Regulator lead time constant (<i>T</i><i><sub>C1</sub></i>) (&gt;= 0).  Typical value = 0,8. Default: 0
	:tb1: Regulator lag time constant (<i>T</i><i><sub>B1</sub></i>) (&gt;= 0).  Typical value = 6. Default: 0
	:tc2: Regulator lead time constant (<i>T</i><i><sub>C2</sub></i>) (&gt;= 0).  Typical value = 0,08. Default: 0
	:tb2: Regulator lag time constant (<i>T</i><i><sub>B2</sub></i>) (&gt;= 0).  Typical value = 0,01. Default: 0
	:toc1: OEL lead time constant (<i>T</i><i><sub>OC1</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:tob1: OEL lag time constant (<i>T</i><i><sub>OB1</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:toc2: OEL lead time constant (<i>T</i><i><sub>OC2</sub></i>) (&gt;= 0).  Typical value = 0,08. Default: 0
	:tob2: OEL lag time constant (<i>T</i><i><sub>OB2</sub></i>) (&gt;= 0).  Typical value = 0,08. Default: 0
	:tuc1: UEL lead time constant (<i>T</i><i><sub>UC1</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:tub1: UEL lag time constant (<i>T</i><i><sub>UB1</sub></i>) (&gt;= 0).  Typical value = 10. Default: 0
	:tuc2: UEL lead time constant (<i>T</i><i><sub>UC2</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:tub2: UEL lag time constant (<i>T</i><i><sub>UB2</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kr': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'tc1': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'tc2': [cgmesProfile.DY.value, ],
						'tb2': [cgmesProfile.DY.value, ],
						'toc1': [cgmesProfile.DY.value, ],
						'tob1': [cgmesProfile.DY.value, ],
						'toc2': [cgmesProfile.DY.value, ],
						'tob2': [cgmesProfile.DY.value, ],
						'tuc1': [cgmesProfile.DY.value, ],
						'tub1': [cgmesProfile.DY.value, ],
						'tuc2': [cgmesProfile.DY.value, ],
						'tub2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kr = 0.0, t1 = 0, kc = 0.0, vrmax = 0.0, vrmin = 0.0, tc1 = 0, tb1 = 0, tc2 = 0, tb2 = 0, toc1 = 0, tob1 = 0, toc2 = 0, tob2 = 0, tuc1 = 0, tub1 = 0, tuc2 = 0, tub2 = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kr = kr
		self.t1 = t1
		self.kc = kc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.tc1 = tc1
		self.tb1 = tb1
		self.tc2 = tc2
		self.tb2 = tb2
		self.toc1 = toc1
		self.tob1 = tob1
		self.toc2 = toc2
		self.tob2 = tob2
		self.tuc1 = tuc1
		self.tub1 = tub1
		self.tuc2 = tuc2
		self.tub2 = tub2
		
	def __str__(self):
		str = 'class=ExcIEEEST5B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
