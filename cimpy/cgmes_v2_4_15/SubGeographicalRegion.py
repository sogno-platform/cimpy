from cimpy.output.IdentifiedObject import IdentifiedObject


class SubGeographicalRegion(IdentifiedObject):
	'''
	A subset of a geographical region of a power system network model.

	:DCLines:  Default: 
	:Region: The geographical region to which this sub-geographical region is within. Default: 
	:Lines: The lines within the sub-geographical region. Default: 
	:Substations: The substations in this sub-geographical region. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'DCLines': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Region': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'Lines': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'Substations': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCLines = , Region = , Lines = , Substations = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCLines = DCLines
		self.Region = Region
		self.Lines = Lines
		self.Substations = Substations
		
	def __str__(self):
		str = 'class=SubGeographicalRegion\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
