from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST2A(ExcitationSystemDynamics):
	'''
	Modified IEEE ST2A static excitation system with another lead-lag block added to match the model defined by WECC.

	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 120. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,15. Default: 0
	:vrmax: Maximum voltage regulator outputs (<i>Vrmax</i>) (&gt; 0).  Typical value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (<i>Vrmin</i>) (&lt; 0).  Typical value = -1. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 0,5. Default: 0
	:kf: Excitation control system stabilizer gains (<i>kf</i>) (&gt;= 0).  Typical value = 0,05. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 0,7. Default: 0
	:kp: Potential circuit gain coefficient (<i>K</i><i><sub>p</sub></i>) (&gt;= 0).  Typical value = 4,88. Default: 0.0
	:ki: Potential circuit gain coefficient (<i>K</i><i><sub>i</sub></i>) (&gt;= 0).  Typical value = 8. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0).  Typical value = 1,82. Default: 0.0
	:efdmax: Maximum field voltage (<i>Efdmax</i>) (&gt;= 0).  Typical value = 99. Default: 0.0
	:uelin: UEL input (<i>UELin</i>). true = HV gate false = add to error signal. Typical value = false. Default: False
	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0, kf = 0.0, tf = 0, kp = 0.0, ki = 0.0, kc = 0.0, efdmax = 0.0, uelin = False, tb = 0, tc = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.kc = kc
		self.efdmax = efdmax
		self.uelin = uelin
		self.tb = tb
		self.tc = tc
		
	def __str__(self):
		str = 'class=ExcST2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
