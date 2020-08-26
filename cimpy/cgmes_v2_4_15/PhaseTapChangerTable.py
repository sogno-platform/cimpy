from cimpy.output.IdentifiedObject import IdentifiedObject


class PhaseTapChangerTable(IdentifiedObject):
	'''
	Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

	:PhaseTapChangerTablePoint: The points of this table. Default: 
	:PhaseTapChangerTabular: The phase tap changers to which this phase tap table applies. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'PhaseTapChangerTablePoint': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'PhaseTapChangerTabular': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, PhaseTapChangerTablePoint = , PhaseTapChangerTabular = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PhaseTapChangerTablePoint = PhaseTapChangerTablePoint
		self.PhaseTapChangerTabular = PhaseTapChangerTabular
		
	def __str__(self):
		str = 'class=PhaseTapChangerTable\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
