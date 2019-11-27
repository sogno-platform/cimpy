from cimpy.cgmes_v2_4_15.DCConductingEquipment import DCConductingEquipment


class DCLineSegment(DCConductingEquipment):
	'''
	A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

	:capacitance: Capacitance of the DC line segment. Significant for cables only. Default: 0.0
	:inductance: Inductance of the DC line segment. Neglectable compared with DCSeriesDevice used for smoothing. Default: 0.0
	:resistance: Resistance of the DC line segment. Default: 0.0
	:length: Segment length for calculating line section capabilities. Default: 0.0
	:PerLengthParameter: Set of per-length parameters for this line segment. Default: None
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'capacitance': [cgmesProfile.EQ.value, ],
						'inductance': [cgmesProfile.EQ.value, ],
						'resistance': [cgmesProfile.EQ.value, ],
						'length': [cgmesProfile.EQ.value, ],
						'PerLengthParameter': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, capacitance = 0.0, inductance = 0.0, resistance = 0.0, length = 0.0, PerLengthParameter = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.capacitance = capacitance
		self.inductance = inductance
		self.resistance = resistance
		self.length = length
		self.PerLengthParameter = PerLengthParameter
		
	def __str__(self):
		str = 'class=DCLineSegment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
