from cimpy.cgmes_v2_4_15.Base import Base


class PositionPoint(Base):
	'''
	Set of spatial coordinates that determine a point, defined in the coordinate system specified in 'Location.CoordinateSystem'. Use a single position point instance to desribe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values).

	:Location: Location described by this position point. Default: None
	:sequenceNumber: Zero-relative sequence number of this point within a series of points. Default: 0
	:xPosition: X axis position. Default: ''
	:yPosition: Y axis position. Default: ''
	:zPosition: (if applicable) Z axis position. Default: ''
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						'Location': [cgmesProfile.GL.value, ],
						'sequenceNumber': [cgmesProfile.GL.value, ],
						'xPosition': [cgmesProfile.GL.value, ],
						'yPosition': [cgmesProfile.GL.value, ],
						'zPosition': [cgmesProfile.GL.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, Location = None, sequenceNumber = 0, xPosition = '', yPosition = '', zPosition = '',  ):
	
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
