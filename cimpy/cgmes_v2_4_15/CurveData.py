from  import Base


class CurveData(Base):
	'''
	Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific class  can be used to specify the x and y axis values along with their specific data types.

	:Curve: The point data values that define this curve. Default: 
	:xvalue: The data value of the X-axis variable,  depending on the X-axis units. Default: 
	:y1value: The data value of the  first Y-axis variable, depending on the Y-axis units. Default: 
	:y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Curve': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'xvalue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'y1value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'y2value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, Curve = , xvalue = , y1value = , y2value = ,  ):
	
		self.Curve = Curve
		self.xvalue = xvalue
		self.y1value = y1value
		self.y2value = y2value
		
	def __str__(self):
		str = 'class=CurveData\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
