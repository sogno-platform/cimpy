from cimpy.cgmes_v2_4_15_flat.DCConductingEquipment import DCConductingEquipment


class DCShunt(DCConductingEquipment):
	'''
	A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

	:capacitance: Capacitance of the DC shunt. Default: 0.0
	:resistance: Resistance of the DC device. Default: 0.0
	:ratedUdc: Rated DC device voltage. Converter configuration data used in power flow. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'capacitance': [cgmesProfile.EQ.value, ],
						'resistance': [cgmesProfile.EQ.value, ],
						'ratedUdc': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, capacitance = 0.0, resistance = 0.0, ratedUdc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.capacitance = capacitance
		self.resistance = resistance
		self.ratedUdc = ratedUdc
		
	def __str__(self):
		str = 'class=DCShunt\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
