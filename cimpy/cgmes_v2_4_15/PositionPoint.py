from  import Base


class PositionPoint(Base):
	'''
	Set of spatial coordinates that determine a point, defined in the coordinate system specified in 'Location.CoordinateSystem'. Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

	:Location: Location described by this position point. Default: 
	:sequenceNumber: Zero-relative sequence number of this point within a series of points. Default: 
	:xPosition: X axis position. Default: 
	:yPosition: Y axis position. Default: 
	:zPosition: (if applicable) Z axis position. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'Location': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'sequenceNumber': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'xPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'yPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						'zPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'GL'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, Location = , sequenceNumber = , xPosition = , yPosition = , zPosition = ,  ):
	
		self.Location = Location
		self.sequenceNumber = sequenceNumber
		self.xPosition = xPosition
		self.yPosition = yPosition
		self.zPosition = zPosition
		
	def __str__(self):
		str = 'class=PositionPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
