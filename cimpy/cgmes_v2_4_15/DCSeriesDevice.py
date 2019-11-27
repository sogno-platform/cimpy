from cimpy.cgmes_v2_4_15.DCConductingEquipment import DCConductingEquipment


class DCSeriesDevice(DCConductingEquipment):
	'''
	A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and short circuit studies.

	:inductance: Inductance of the device. Default: 0.0
	:resistance: Resistance of the DC device. Default: 0.0
	:ratedUdc: Rated DC device voltage. Converter configuration data used in power flow. Default: 0.0
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'inductance': [cgmesProfile.EQ.value, ],
						'resistance': [cgmesProfile.EQ.value, ],
						'ratedUdc': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, inductance = 0.0, resistance = 0.0, ratedUdc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inductance = inductance
		self.resistance = resistance
		self.ratedUdc = ratedUdc
		
	def __str__(self):
		str = 'class=DCSeriesDevice\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
