from cimpy.output.IdentifiedObject import IdentifiedObject


class DiagramStyle(IdentifiedObject):
	'''
	The diagram style refer to a style used by the originating system for a diagram.  A diagram style describes information such as schematic, geographic, bus-branch etc.

	:Diagram: A DiagramStyle can be used by many Diagrams. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'Diagram': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Diagram = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Diagram = Diagram
		
	def __str__(self):
		str = 'class=DiagramStyle\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
