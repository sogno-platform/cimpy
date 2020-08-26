from cimpy.output.IdentifiedObject import IdentifiedObject


class DiagramObject(IdentifiedObject):
	'''
	An object that defines one or more points in a given space. This object can be associated with anything that specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog values, breakers, disconnectors, power transformers, and transmission lines.

	:Diagram: A diagram object is part of a diagram. Default: 
	:drawingOrder: The drawing order of this element. The higher the number, the later the element is drawn in sequence. This is used to ensure that elements that overlap are rendered in the correct order. Default: 
	:isPolygon: Defines whether or not the diagram objects points define the boundaries of a polygon or the routing of a polyline. If this value is true then a receiving application should consider the first and last points to be connected. Default: 
	:offsetX: The offset in the X direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the horizontal centre of the icon.  -0.5 indicates it is offset by 50% to the left and 0.5 indicates an offset of 50% to the right. Default: 
	:offsetY: The offset in the Y direction. This is used for defining the offset from centre for rendering an icon (the default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0 indicating there is no offset from the vertical centre of the icon.  The offset direction is dependent on the orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50% on the vertical axis. Default: 
	:rotation: Sets the angle of rotation of the diagram object.  Zero degrees is pointing to the top of the diagram.  Rotation is clockwise. Default: 
	:IdentifiedObject: The diagram objects that are associated with the domain object. Default: 
	:DiagramObjectPoints: A diagram object can have 0 or more points to reflect its layout position, routing (for polylines) or boundary (for polygons). Default: 
	:VisibilityLayers: A diagram object can be part of multiple visibility layers. Default: 
	:DiagramObjectStyle: A diagram object has a style associated that provides a reference for the style used in the originating system. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'Diagram': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'drawingOrder': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'isPolygon': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'offsetX': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'offsetY': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'rotation': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'IdentifiedObject': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'DiagramObjectPoints': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'VisibilityLayers': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'DiagramObjectStyle': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Diagram = , drawingOrder = , isPolygon = , offsetX = , offsetY = , rotation = , IdentifiedObject = , DiagramObjectPoints = , VisibilityLayers = , DiagramObjectStyle = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Diagram = Diagram
		self.drawingOrder = drawingOrder
		self.isPolygon = isPolygon
		self.offsetX = offsetX
		self.offsetY = offsetY
		self.rotation = rotation
		self.IdentifiedObject = IdentifiedObject
		self.DiagramObjectPoints = DiagramObjectPoints
		self.VisibilityLayers = VisibilityLayers
		self.DiagramObjectStyle = DiagramObjectStyle
		
	def __str__(self):
		str = 'class=DiagramObject\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
