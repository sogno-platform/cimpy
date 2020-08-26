from cimpy.output.IdentifiedObject import IdentifiedObject


class WindPitchContEmulIEC(IdentifiedObject):
	'''
	Pitch control emulator model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.1.

	:WindGenTurbineType2IEC: Wind turbine type 2 model with which this Pitch control emulator model is associated. Default: 
	:kdroop: Power error gain (). It is case dependent parameter. Default: 
	:kipce: Pitch control emulator integral constant (). It is type dependent parameter. Default: 
	:komegaaero: Aerodynamic power change vs. omegachange (). It is case dependent parameter. Default: 
	:kppce: Pitch control emulator proportional constant (). It is type dependent parameter. Default: 
	:omegaref: Rotor speed in initial steady state (omega). It is case dependent parameter. Default: 
	:pimax: Maximum steady state power (). It is case dependent parameter. Default: 
	:pimin: Minimum steady state power (). It is case dependent parameter. Default: 
	:t1: First time constant in pitch control lag (). It is type dependent parameter. Default: 
	:t2: Second time constant in pitch control lag (). It is type dependent parameter. Default: 
	:tpe: Time constant in generator air gap power lag (). It is type dependent parameter. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindGenTurbineType2IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kdroop': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kipce': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'komegaaero': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kppce': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'omegaref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pimax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pimin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpe': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindGenTurbineType2IEC = , kdroop = , kipce = , komegaaero = , kppce = , omegaref = , pimax = , pimin = , t1 = , t2 = , tpe = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
		self.kdroop = kdroop
		self.kipce = kipce
		self.komegaaero = komegaaero
		self.kppce = kppce
		self.omegaref = omegaref
		self.pimax = pimax
		self.pimin = pimin
		self.t1 = t1
		self.t2 = t2
		self.tpe = tpe
		
	def __str__(self):
		str = 'class=WindPitchContEmulIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
