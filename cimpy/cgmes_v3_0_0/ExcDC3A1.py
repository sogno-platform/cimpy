from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC3A1(ExcitationSystemDynamics):
	'''
	Modified old IEEE type 3 excitation system.

	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 300. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,01. Default: 0
	:vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; ExcDC3A1.vrmin).  Typical value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0 and &lt; ExcDC3A1.vrmax).  Typical value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 1,83. Default: 0
	:kf: Excitation control system stabilizer gain (<i>Kf</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 0,675. Default: 0
	:kp: Potential circuit gain coefficient (<i>Kp</i>) (&gt;= 0).  Typical value = 4,37. Default: 0.0
	:ki: Potential circuit gain coefficient (<i>Ki</i>) (&gt;= 0).  Typical value = 4,83. Default: 0.0
	:vbmax: Available exciter voltage limiter (<i>Vbmax</i>) (&gt; 0).  Typical value = 11,63. Default: 0.0
	:exclim: (<i>exclim</i>). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied to integrator output. Typical value = true. Default: False
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
	:vb1max: Available exciter voltage limiter (<i>Vb1max</i>) (&gt; 0).  Typical value = 11,63. Default: 0.0
	:vblim: Vb limiter indicator. true = exciter <i>Vbmax</i> limiter is active false = <i>Vb1max</i> is active.  Typical value = true. Default: False
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'vb1max': [cgmesProfile.DY.value, ],
						'vblim': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0, vrmax = 0.0, vrmin = 0.0, te = 0, kf = 0.0, tf = 0, kp = 0.0, ki = 0.0, vbmax = 0.0, exclim = False, ke = 0.0, vb1max = 0.0, vblim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.vbmax = vbmax
		self.exclim = exclim
		self.ke = ke
		self.vb1max = vb1max
		self.vblim = vblim
		
	def __str__(self):
		str = 'class=ExcDC3A1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
