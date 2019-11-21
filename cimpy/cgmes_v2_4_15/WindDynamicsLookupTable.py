from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class WindDynamicsLookupTable(IdentifiedObject):
	'''
	The class models a look up table for the purpose of wind standard models.

	:WindContCurrLimIEC: The wind dynamics lookup table associated with this current control limitation model. Default: None
	:WindContPType3IEC: The wind dynamics lookup table associated with this P control type 3 model. Default: None
	:WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated. Default: None
	:input: Input value (x) for the lookup table function. Default: 0.0
	:lookupTableFunctionType: Type of the lookup table function. Default: None
	:output: Output value (y) for the lookup table function. Default: 0.0
	:sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function. Default: 0
	:WindPlantFreqPcontrolIEC: The wind dynamics lookup table associated with this frequency and active power wind plant model. Default: None
		'''

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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindContCurrLimIEC = None, WindContPType3IEC = None, WindContRotorRIEC = None, input = 0.0, lookupTableFunctionType = None, output = 0.0, sequence = 0, WindPlantFreqPcontrolIEC = None,  *args, **kw_args):
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
