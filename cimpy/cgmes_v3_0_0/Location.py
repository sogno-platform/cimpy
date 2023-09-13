from .IdentifiedObject import IdentifiedObject


class Location(IdentifiedObject):
	'''
	The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more position points (coordinates) in a given coordinate system.

	:CoordinateSystem: Coordinate system used to describe position points of this location. Default: None
	:mainAddress: Main address of the location. Default: 0.0
	:PowerSystemResources: All power system resources at this location. Default: None
	:PositionPoints: Sequence of position points describing this location, expressed in coordinate system `Location.CoordinateSystem`. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						'CoordinateSystem': [cgmesProfile.GL.value, ],
						'mainAddress': [cgmesProfile.GL.value, ],
						'PowerSystemResources': [cgmesProfile.GL.value, ],
						'PositionPoints': [cgmesProfile.GL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, CoordinateSystem = None, mainAddress = 0.0, PowerSystemResources = None, PositionPoints = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CoordinateSystem = CoordinateSystem
		self.mainAddress = mainAddress
		self.PowerSystemResources = PowerSystemResources
		self.PositionPoints = PositionPoints
		
	def __str__(self):
		str = 'class=Location\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
