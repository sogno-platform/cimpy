from cimpy.output.PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerNonLinear(PhaseTapChanger):
	'''
	The non-linear phase tap changer describes the non-linear behavior of a phase tap changer. This is a base class for the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in the IEC 61970-301 document.

	:voltageStepIncrement: The voltage step increment on the out of phase winding specified in percent of nominal voltage of the transformer end. Default: 
	:xMax: The reactance depend on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appear at the low and high tap positions. Default: 
	:xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear at the mid tap position. Default: 
		'''

	cgmesProfile = PhaseTapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'voltageStepIncrement': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'xMax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'xMin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PhaseTapChanger: \n' + PhaseTapChanger.__doc__ 

	def __init__(self, voltageStepIncrement = , xMax = , xMin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.voltageStepIncrement = voltageStepIncrement
		self.xMax = xMax
		self.xMin = xMin
		
	def __str__(self):
		str = 'class=PhaseTapChangerNonLinear\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
