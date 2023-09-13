from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST4B(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type ST4B model. This model is a variation of the type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential and compound source rectifier excitation systems are modelled.  The PI regulator blocks have non-windup limits that are represented. The voltage regulator of this model is typically implemented digitally. Reference: IEEE 421.5-2005, 7.4.

	:kpr: Voltage regulator proportional gain (<i>K</i><i><sub>PR</sub></i>).  Typical value = 10,75. Default: 0.0
	:kir: Voltage regulator integral gain (<i>K</i><i><sub>IR</sub></i>).  Typical value = 10,75. Default: 0.0
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -0,87. Default: 0.0
	:kpm: Voltage regulator proportional gain output (<i>K</i><i><sub>PM</sub></i>).  Typical value = 1. Default: 0.0
	:kim: Voltage regulator integral gain output (<i>K</i><i><sub>IM</sub></i>).  Typical value = 0. Default: 0.0
	:vmmax: Maximum inner loop output (<i>V</i><i><sub>MMax</sub></i>) (&gt; ExcIEEEST4B.vmmin).  Typical value = 99. Default: 0.0
	:vmmin: Minimum inner loop output (<i>V</i><i><sub>MMin</sub></i>) (&lt; ExcIEEEST4B.vmmax).  Typical value = -99. Default: 0.0
	:kg: Feedback gain constant of the inner loop field regulator (<i>K</i><i><sub>G</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:kp: Potential circuit gain coefficient (<i>K</i><i><sub>P</sub></i>) (&gt; 0).  Typical value = 9,3. Default: 0.0
	:thetap: Potential circuit phase angle (<i>thetap</i>).  Typical value = 0. Default: 0.0
	:ki: Potential circuit gain coefficient (<i>K</i><i><sub>I</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0). Typical value = 0,113. Default: 0.0
	:xl: Reactance associated with potential source (<i>X</i><i><sub>L</sub></i>) (&gt;= 0).  Typical value = 0,124. Default: 0.0
	:vbmax: Maximum excitation voltage (<i>V</i><i><sub>BMax</sub></i>) (&gt; 0).  Typical value = 11,63. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpr': [cgmesProfile.DY.value, ],
						'kir': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kpm': [cgmesProfile.DY.value, ],
						'kim': [cgmesProfile.DY.value, ],
						'vmmax': [cgmesProfile.DY.value, ],
						'vmmin': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'thetap': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'xl': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = 0.0, kir = 0.0, ta = 0, vrmax = 0.0, vrmin = 0.0, kpm = 0.0, kim = 0.0, vmmax = 0.0, vmmin = 0.0, kg = 0.0, kp = 0.0, thetap = 0.0, ki = 0.0, kc = 0.0, xl = 0.0, vbmax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpr = kpr
		self.kir = kir
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kpm = kpm
		self.kim = kim
		self.vmmax = vmmax
		self.vmmin = vmmin
		self.kg = kg
		self.kp = kp
		self.thetap = thetap
		self.ki = ki
		self.kc = kc
		self.xl = xl
		self.vbmax = vbmax
		
	def __str__(self):
		str = 'class=ExcIEEEST4B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
