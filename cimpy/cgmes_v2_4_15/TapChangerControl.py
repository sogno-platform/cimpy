from cimpy.output.RegulatingControl import RegulatingControl


class TapChangerControl(RegulatingControl):
	'''
	Describes behavior specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

	:TapChanger: The regulating control scheme in which this tap changer participates. Default: 
		'''

	cgmesProfile = RegulatingControl.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'TapChanger': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingControl: \n' + RegulatingControl.__doc__ 

	def __init__(self, TapChanger = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TapChanger = TapChanger
		
	def __str__(self):
		str = 'class=TapChangerControl\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
