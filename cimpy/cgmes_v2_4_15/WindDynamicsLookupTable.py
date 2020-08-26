from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class WindDynamicsLookupTable(IdentifiedObject):
	'''
	The class models a look up table for the purpose of wind standard models.

	:WindContCurrLimIEC: The wind dynamics lookup table associated with this current control limitation model. Default: 
	:WindContPType3IEC: The wind dynamics lookup table associated with this P control type 3 model. Default: 
	:WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated. Default: 
	:input: Input value (x) for the lookup table function. Default: 
	:lookupTableFunctionType: Type of the lookup table function. Default: 
	:output: Output value (y) for the lookup table function. Default: 
	:sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function. Default: 
	:WindPlantFreqPcontrolIEC: The wind dynamics lookup table associated with this frequency and active power wind plant model. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindContCurrLimIEC': [cgmesProfile.DY.value, ],
						'WindContPType3IEC': [cgmesProfile.DY.value, ],
						'WindContRotorRIEC': [cgmesProfile.DY.value, ],
						'input': [cgmesProfile.DY.value, ],
						'lookupTableFunctionType': [cgmesProfile.DY.value, ],
						'output': [cgmesProfile.DY.value, ],
						'sequence': [cgmesProfile.DY.value, ],
						'WindPlantFreqPcontrolIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindContCurrLimIEC = , WindContPType3IEC = , WindContRotorRIEC = , input = , lookupTableFunctionType = , output = , sequence = , WindPlantFreqPcontrolIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContCurrLimIEC = WindContCurrLimIEC
		self.WindContPType3IEC = WindContPType3IEC
		self.WindContRotorRIEC = WindContRotorRIEC
		self.input = input
		self.lookupTableFunctionType = lookupTableFunctionType
		self.output = output
		self.sequence = sequence
		self.WindPlantFreqPcontrolIEC = WindPlantFreqPcontrolIEC
		
	def __str__(self):
		str = 'class=WindDynamicsLookupTable\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
