from .IdentifiedObject import IdentifiedObject


class Diagram(IdentifiedObject):
	'''
	The diagram being exchanged. The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation. The initial view related attributes can be used to specify an initial view with the x,y coordinates of the diagonal points.

	:orientation: Coordinate system orientation of the diagram. A positive orientation gives standard `right-hand` orientation, with negative orientation indicating a `left-hand` orientation. For 2D diagrams, a positive orientation will result in X values increasing from left to right and Y values increasing from bottom to top. A negative orientation gives the `left-hand` orientation (favoured by computer graphics displays) with X values increasing from left to right and Y values increasing from top to bottom. Default: None
	:x1InitialView: X coordinate of the first corner of the initial view. Default: 0.0
	:x2InitialView: X coordinate of the second corner of the initial view. Default: 0.0
	:y1InitialView: Y coordinate of the first corner of the initial view. Default: 0.0
	:y2InitialView: Y coordinate of the second corner of the initial view. Default: 0.0
	:DiagramElements: A diagram is made up of multiple diagram objects. Default: "list"
	:DiagramStyle: A Diagram may have a DiagramStyle. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, ],
						'orientation': [cgmesProfile.DL.value, ],
						'x1InitialView': [cgmesProfile.DL.value, ],
						'x2InitialView': [cgmesProfile.DL.value, ],
						'y1InitialView': [cgmesProfile.DL.value, ],
						'y2InitialView': [cgmesProfile.DL.value, ],
						'DiagramElements': [cgmesProfile.DL.value, ],
						'DiagramStyle': [cgmesProfile.DL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, orientation = None, x1InitialView = 0.0, x2InitialView = 0.0, y1InitialView = 0.0, y2InitialView = 0.0, DiagramElements = "list", DiagramStyle = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.orientation = orientation
		self.x1InitialView = x1InitialView
		self.x2InitialView = x2InitialView
		self.y1InitialView = y1InitialView
		self.y2InitialView = y2InitialView
		self.DiagramElements = DiagramElements
		self.DiagramStyle = DiagramStyle
		
	def __str__(self):
		str = 'class=Diagram\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
