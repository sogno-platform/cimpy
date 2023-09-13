from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC5A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.

	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 400. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 7,3. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0).  Typical value =-7,3. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 0,8. Default: 0
	:kf: Excitation control system stabilizer gains (<i>Kf</i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:tf1: Excitation control system stabilizer time constant (<i>Tf1</i>) (&gt; 0).  Typical value  = 1. Default: 0
	:tf2: Excitation control system stabilizer time constant (<i>Tf2</i>) (&gt;= 0).  Typical value = 0,8. Default: 0
	:tf3: Excitation control system stabilizer time constant (<i>Tf3</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:efd1: Exciter voltage at which exciter saturation is defined (<i>Efd1</i>) (&gt; 0).  Typical value = 5,6. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>1</sub></i> (<i>Se[Efd</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,86. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (<i>Efd2</i>) (&gt; 0).  Typical value = 4,2. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>2</sub></i> (<i>Se[Efd</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,5. Default: 0.0
	:a: Coefficient to allow different usage of the model (<i>a</i>).  Typical value = 1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'tf3': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ks = 0.0, tb = 0, tc = 0, ta = 0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0, kf = 0.0, tf1 = 0, tf2 = 0, tf3 = 0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, a = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
		self.tb = tb
		self.tc = tc
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		self.tf3 = tf3
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.a = a
		
	def __str__(self):
		str = 'class=ExcAC5A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
