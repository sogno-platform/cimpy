from cimpy.output.IdentifiedObject import IdentifiedObject


class Location(IdentifiedObject):
	'''
	The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.

	:CoordinateSystem: Coordinate system used to describe position points of this location. Default: 
	:PowerSystemResources: All power system resources at this location. Default: 
	:PositionPoints: Sequence of position points describing this location, expressed in coordinate system `Location.CoordinateSystem`. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'CoordinateSystem': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'PowerSystemResources': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'PositionPoints': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, CoordinateSystem = , PowerSystemResources = , PositionPoints = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CoordinateSystem = CoordinateSystem
		self.PowerSystemResources = PowerSystemResources
		self.PositionPoints = PositionPoints
		
	def __str__(self):
		str = 'class=Location\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
