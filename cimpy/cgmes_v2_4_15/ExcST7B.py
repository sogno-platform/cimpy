from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST7B(ExcitationSystemDynamics):
	'''
	Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP) inputs.

	:kh: High-value gate feedback gain (Kh).  Typical Value = 1. Default: 
	:kia: Voltage regulator integral gain (Kia).  Typical Value = 1. Default: 
	:kl: Low-value gate feedback gain (Kl).  Typical Value = 1. Default: 
	:kpa: Voltage regulator proportional gain (Kpa).  Typical Value = 40. Default: 
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: 
	:tb: Regulator lag time constant (Tb).  Typical Value = 1. Default: 
	:tc: Regulator lead time constant (Tc).  Typical Value = 1. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 
	:tg: Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 1. Default: 
	:tia: Feedback time constant (Tia).  Typical Value = 3. Default: 
	:ts: Rectifier firing time constant (Ts).  Typical Value = 0. Default: 
	:uelin: UEL input selector (UELin). Typical Value = noUELinput. Default: 
	:vmax: Maximum voltage reference signal (Vmax).  Typical Value = 1.1. Default: 
	:vmin: Minimum voltage reference signal (Vmin).  Typical Value = 0.9. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.5. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kh': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpa': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'oelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ts': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kh = , kia = , kl = , kpa = , oelin = , tb = , tc = , tf = , tg = , tia = , ts = , uelin = , vmax = , vmin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kh = kh
		self.kia = kia
		self.kl = kl
		self.kpa = kpa
		self.oelin = oelin
		self.tb = tb
		self.tc = tc
		self.tf = tf
		self.tg = tg
		self.tia = tia
		self.ts = ts
		self.uelin = uelin
		self.vmax = vmax
		self.vmin = vmin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcST7B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
