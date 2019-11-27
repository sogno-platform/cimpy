from cimpy.cgmes_v2_4_15.Base import Base


class DiagramObjectPoint(Base):
	'''
	A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.

	:DiagramObject: The diagram object with which the points are associated. Default: None
	:DiagramObjectGluePoint: A diagram object glue point is associated with 2 or more object points that are considered to be 'glued' together. Default: None
	:sequenceNumber: The sequence position of the point, used for defining the order of points for diagram objects acting as a polyline or polygon with more than one point. Default: 0
	:xPosition: The X coordinate of this point. Default: 0.0
	:yPosition: The Y coordinate of this point. Default: 0.0
	:zPosition: The Z coordinate of this point. Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DI.value, ],
						'DiagramObject': [cgmesProfile.DI.value, ],
						'DiagramObjectGluePoint': [cgmesProfile.DI.value, ],
						'sequenceNumber': [cgmesProfile.DI.value, ],
						'xPosition': [cgmesProfile.DI.value, ],
						'yPosition': [cgmesProfile.DI.value, ],
						'zPosition': [cgmesProfile.DI.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, DiagramObject = None, DiagramObjectGluePoint = None, sequenceNumber = 0, xPosition = 0.0, yPosition = 0.0, zPosition = 0.0,  ):
	
		self.DiagramObject = DiagramObject
		self.DiagramObjectGluePoint = DiagramObjectGluePoint
		self.sequenceNumber = sequenceNumber
		self.xPosition = xPosition
		self.yPosition = yPosition
		self.zPosition = zPosition
		
	def __str__(self):
		str = 'class=DiagramObjectPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
