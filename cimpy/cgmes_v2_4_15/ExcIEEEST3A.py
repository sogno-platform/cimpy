from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST3A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in model Type ST3A which is represented by ExcIEEEST3A.   Reference: IEEE Standard 421.5-2005 Section 7.3.

	:vimax: Maximum voltage regulator input limit (V).  Typical Value = 0.2. Default: 
	:vimin: Minimum voltage regulator input limit (V).  Typical Value = -0.2. Default: 
	:ka: Voltage regulator gain (K). This is parameter K in the IEEE Std. Typical Value = 200. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tb: Voltage regulator time constant (T).  Typical Value = 10. Default: 
	:tc: Voltage regulator time constant (T).  Typical Value = 1. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 10. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -10. Default: 
	:km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 7.93. Default: 
	:tm: Forward time constant of inner loop field regulator (T).  Typical Value = 0.4. Default: 
	:vmmax: Maximum inner loop output (V).  Typical Value = 1. Default: 
	:vmmin: Minimum inner loop output (V).  Typical Value = 0. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 
	:kp: Potential circuit gain coefficient (K).  Typical Value = 6.15. Default: 
	:thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 
	:ki: Potential circuit gain coefficient (K).  Typical Value = 0. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.2. Default: 
	:xl: Reactance associated with potential source (X).  Typical Value = 0.081. Default: 
	:vbmax: Maximum excitation voltage (V).  Typical Value = 6.9. Default: 
	:vgmax: Maximum inner loop feedback voltage (V).  Typical Value = 5.8. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vimax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vimin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'km': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'thetap': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vbmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vgmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = , vimin = , ka = , ta = , tb = , tc = , vrmax = , vrmin = , km = , tm = , vmmax = , vmmin = , kg = , kp = , thetap = , ki = , kc = , xl = , vbmax = , vgmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vimax = vimax
		self.vimin = vimin
		self.ka = ka
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.km = km
		self.tm = tm
		self.vmmax = vmmax
		self.vmmin = vmmin
		self.kg = kg
		self.kp = kp
		self.thetap = thetap
		self.ki = ki
		self.kc = kc
		self.xl = xl
		self.vbmax = vbmax
		self.vgmax = vgmax
		
	def __str__(self):
		str = 'class=ExcIEEEST3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
