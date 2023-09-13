from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC2A(ExcitationSystemDynamics):
	'''
	Modified IEEE DC2A direct current commutator exciter with speed input, one more leg block in feedback loop and without underexcitation limiters (UEL) inputs.  DC type 2 excitation system model with added speed multiplier, added lead-lag, and voltage-dependent limits.

	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 300. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,01. Default: 0
	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; ExcDC2A.vrmin).  Typical value = 4,95. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0 and &lt; ExcDC2A.vrmax).  Typical value = -4,9. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  If <i>Ke</i> is entered as zero, the model calculates an effective value of <i>Ke</i> such that the initial condition value of <i>Vr</i> is zero. The zero value of <i>Ke</i> is not changed.  If <i>Ke</i> is entered as non-zero, its value is used directly, without change.  Typical value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 1,33. Default: 0
	:kf: Excitation control system stabilizer gain (<i>Kf</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt; 0).  Typical value = 0,675. Default: 0
	:tf1: Excitation control system stabilizer time constant (<i>Tf1</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:efd1: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>1</sub></i>) (&gt; 0).  Typical value = 3,05. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>1</sub></i> (<i>Se[Efd</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,279. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>2</sub></i>) (&gt; 0).  Typical value = 2,29. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>2</sub></i> (<i>Se[Efd</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,117. Default: 0.0
	:exclim: (<i>exclim</i>).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical value = true. Default: False
	:vtlim: (<i>Vtlim</i>). true = limiter at the block (<i>Ka / [1 + sTa]</i>) is dependent on <i>Vt </i> false = limiter at the block is not dependent on <i>Vt</i>. Typical value = true. Default: False
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						'vtlim': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ks = 0.0, ta = 0, tb = 0, tc = 0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0, kf = 0.0, tf = 0, tf1 = 0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, exclim = False, vtlim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.tf1 = tf1
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.exclim = exclim
		self.vtlim = vtlim
		
	def __str__(self):
		str = 'class=ExcDC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
