from cimpy.output.TapChangerTablePoint import TapChangerTablePoint


class PhaseTapChangerTablePoint(TapChangerTablePoint):
	'''
	Describes each tap step in the phase tap changer tabular curve.

	:PhaseTapChangerTable: The table of this point. Default: 
	:angle: The angle difference in degrees. Default: 
		'''

	cgmesProfile = TapChangerTablePoint.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'PhaseTapChangerTable': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'angle': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TapChangerTablePoint: \n' + TapChangerTablePoint.__doc__ 

	def __init__(self, PhaseTapChangerTable = , angle = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PhaseTapChangerTable = PhaseTapChangerTable
		self.angle = angle
		
	def __str__(self):
		str = 'class=PhaseTapChangerTablePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
