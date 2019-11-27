from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class Diagram(IdentifiedObject):
	'''
	The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

	:DiagramStyle: A Diagram may have a DiagramStyle. Default: None
	:orientation: Coordinate system orientation of the diagram. Default: None
	:x1InitialView: X coordinate of the first corner of the initial view. Default: 0.0
	:x2InitialView: X coordinate of the second corner of the initial view. Default: 0.0
	:y1InitialView: Y coordinate of the first corner of the initial view. Default: 0.0
	:y2InitialView: Y coordinate of the second corner of the initial view. Default: 0.0
	:DiagramElements: A diagram is made up of multiple diagram objects. Default: []
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DI.value, ],
						'DiagramStyle': [cgmesProfile.DI.value, ],
						'orientation': [cgmesProfile.DI.value, ],
						'x1InitialView': [cgmesProfile.DI.value, ],
						'x2InitialView': [cgmesProfile.DI.value, ],
						'y1InitialView': [cgmesProfile.DI.value, ],
						'y2InitialView': [cgmesProfile.DI.value, ],
						'DiagramElements': [cgmesProfile.DI.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DiagramStyle = None, orientation = None, x1InitialView = 0.0, x2InitialView = 0.0, y1InitialView = 0.0, y2InitialView = 0.0, DiagramElements = [],  *args, **kw_args):
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
