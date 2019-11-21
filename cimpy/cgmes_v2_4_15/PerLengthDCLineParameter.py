from cimpy.cgmes_v2_4_15_flat.Base import Base


class PerLengthDCLineParameter(Base):
	'''
	

	:DCLineSegments: All line segments described by this set of per-length parameters. Default: []
	:capacitance: Capacitance per unit of length of the DC line segment; significant for cables only. Default: 0.0
	:inductance: Inductance per unit of length of the DC line segment. Default: 0.0
	:resistance: Resistance per length of the DC line segment. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'DCLineSegments': [cgmesProfile.EQ.value, ],
						'capacitance': [cgmesProfile.EQ.value, ],
						'inductance': [cgmesProfile.EQ.value, ],
						'resistance': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, DCLineSegments = [], capacitance = 0.0, inductance = 0.0, resistance = 0.0,  ):
	
		self.DCLineSegments = DCLineSegments
		self.capacitance = capacitance
		self.inductance = inductance
		self.resistance = resistance
		
	def __str__(self):
		str = 'class=PerLengthDCLineParameter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
