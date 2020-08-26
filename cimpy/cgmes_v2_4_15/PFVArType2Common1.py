from cimpy.output.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


class PFVArType2Common1(PFVArControllerType2Dynamics):
	'''
	Power factor / Reactive power regulator. This model represents the power factor or reactive power controller such as the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and compares it with the operator's set point.

	:j: Selector (J). true = control mode for reactive power false = control mode for power factor. Default: 
	:kp: Proportional gain (Kp). Default: 
	:ki: Reset gain (Ki). Default: 
	:max: Output limit (max). Default: 
	:ref: Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This initialisation may override the value exchanged by this attribute to represent a plant operator`s change of the reference setting. Default: 
		'''

	cgmesProfile = PFVArControllerType2Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'j': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'max': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PFVArControllerType2Dynamics: \n' + PFVArControllerType2Dynamics.__doc__ 

	def __init__(self, j = , kp = , ki = , max = , ref = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.j = j
		self.kp = kp
		self.ki = ki
		self.max = max
		self.ref = ref
		
	def __str__(self):
		str = 'class=PFVArType2Common1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
