from cimpy.cgmes_v2_4_15_flat.Base import Base


class DiagramObjectGluePoint(Base):
	'''
	This is used for grouping diagram object points from different diagram objects that are considered to be glued together in a diagram even if they are not at the exact same coordinates.

	:DiagramObjectPoints: The 'glue' point to which this point is associated. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.DI.value, ],
						'DiagramObjectPoints': [cgmesProfile.DI.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, DiagramObjectPoints = [],  ):
	
		self.DiagramObjectPoints = DiagramObjectPoints
		
	def __str__(self):
		str = 'class=DiagramObjectGluePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
