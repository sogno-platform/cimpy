from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class Diagram(IdentifiedObject):
	'''
	The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

	:DiagramStyle: A Diagram may have a DiagramStyle. Default: 
	:orientation: Coordinate system orientation of the diagram. Default: 
	:x1InitialView: X coordinate of the first corner of the initial view. Default: 
	:x2InitialView: X coordinate of the second corner of the initial view. Default: 
	:y1InitialView: Y coordinate of the first corner of the initial view. Default: 
	:y2InitialView: Y coordinate of the second corner of the initial view. Default: 
	:DiagramElements: A diagram is made up of multiple diagram objects. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, ],
						'DiagramStyle': [cgmesProfile.DL.value, ],
						'orientation': [cgmesProfile.DL.value, ],
						'x1InitialView': [cgmesProfile.DL.value, ],
						'x2InitialView': [cgmesProfile.DL.value, ],
						'y1InitialView': [cgmesProfile.DL.value, ],
						'y2InitialView': [cgmesProfile.DL.value, ],
						'DiagramElements': [cgmesProfile.DL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DiagramStyle = , orientation = , x1InitialView = , x2InitialView = , y1InitialView = , y2InitialView = , DiagramElements = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DiagramStyle = DiagramStyle
		self.orientation = orientation
		self.x1InitialView = x1InitialView
		self.x2InitialView = x2InitialView
		self.y1InitialView = y1InitialView
		self.y2InitialView = y2InitialView
		self.DiagramElements = DiagramElements
		
	def __str__(self):
		str = 'class=Diagram\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
