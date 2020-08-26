from cimpy.output.Control import Control


class AnalogControl(Control):
	'''
	An analog control used for supervisory control.

	:maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 
	:minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 
	:AnalogValue: The Control variable associated with the MeasurementValue. Default: 
		'''

	cgmesProfile = Control.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'AnalogValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Control: \n' + Control.__doc__ 

	def __init__(self, maxValue = , minValue = , AnalogValue = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.maxValue = maxValue
		self.minValue = minValue
		self.AnalogValue = AnalogValue
		
	def __str__(self):
		str = 'class=AnalogControl\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
