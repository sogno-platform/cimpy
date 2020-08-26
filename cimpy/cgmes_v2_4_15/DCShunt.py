from cimpy.output.DCConductingEquipment import DCConductingEquipment


class DCShunt(DCConductingEquipment):
	'''
	A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

	:capacitance: Capacitance of the DC shunt. Default: 
	:resistance: Resistance of the DC device. Default: 
	:ratedUdc: Rated DC device voltage. Converter configuration data used in power flow. Default: 
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'capacitance': [cgmesProfile.EQ.value, ],
						'resistance': [cgmesProfile.EQ.value, ],
						'ratedUdc': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, capacitance = , resistance = , ratedUdc = ,  *args, **kw_args):
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
