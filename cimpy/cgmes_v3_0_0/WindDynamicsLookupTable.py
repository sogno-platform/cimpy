from .IdentifiedObject import IdentifiedObject


class WindDynamicsLookupTable(IdentifiedObject):
	'''
	Look up table for the purpose of wind standard models.

	:WindContCurrLimIEC: The current control limitation model with which this wind dynamics lookup table is associated. Default: None
	:WindContPType3IEC: The P control type 3 model with which this wind dynamics lookup table is associated. Default: None
	:WindContQPQULimIEC: The QP and QU limitation model with which this wind dynamics lookup table is associated. Default: None
	:WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated. Default: None
	:input: Input value (<i>x</i>) for the lookup table function. Default: 0.0
	:lookupTableFunctionType: Type of the lookup table function. Default: None
	:output: Output value (<i>y</i>) for the lookup table function. Default: 0.0
	:sequence: Sequence numbers of the pairs of the input (<i>x</i>) and the output (<i>y</i>) of the lookup table function. Default: 0
	:WindPlantFreqPcontrolIEC: The frequency and active power wind plant control model with which this wind dynamics lookup table is associated. Default: None
	:WindProtectionIEC: The grid protection model with which this wind dynamics lookup table is associated. Default: None
	:WindPlantReactiveControlIEC: The voltage and reactive power wind plant control model with which this wind dynamics lookup table is associated. Default: None
	:WindGenType3bIEC: The generator type 3B model with which this wind dynamics lookup table is associated. Default: None
	:WindPitchContPowerIEC: The pitch control power model with which this wind dynamics lookup table is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindContCurrLimIEC': [cgmesProfile.DY.value, ],
						'WindContPType3IEC': [cgmesProfile.DY.value, ],
						'WindContQPQULimIEC': [cgmesProfile.DY.value, ],
						'WindContRotorRIEC': [cgmesProfile.DY.value, ],
						'input': [cgmesProfile.DY.value, ],
						'lookupTableFunctionType': [cgmesProfile.DY.value, ],
						'output': [cgmesProfile.DY.value, ],
						'sequence': [cgmesProfile.DY.value, ],
						'WindPlantFreqPcontrolIEC': [cgmesProfile.DY.value, ],
						'WindProtectionIEC': [cgmesProfile.DY.value, ],
						'WindPlantReactiveControlIEC': [cgmesProfile.DY.value, ],
						'WindGenType3bIEC': [cgmesProfile.DY.value, ],
						'WindPitchContPowerIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindContCurrLimIEC = None, WindContPType3IEC = None, WindContQPQULimIEC = None, WindContRotorRIEC = None, input = 0.0, lookupTableFunctionType = None, output = 0.0, sequence = 0, WindPlantFreqPcontrolIEC = None, WindProtectionIEC = None, WindPlantReactiveControlIEC = None, WindGenType3bIEC = None, WindPitchContPowerIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContCurrLimIEC = WindContCurrLimIEC
		self.WindContPType3IEC = WindContPType3IEC
		self.WindContQPQULimIEC = WindContQPQULimIEC
		self.WindContRotorRIEC = WindContRotorRIEC
		self.input = input
		self.lookupTableFunctionType = lookupTableFunctionType
		self.output = output
		self.sequence = sequence
		self.WindPlantFreqPcontrolIEC = WindPlantFreqPcontrolIEC
		self.WindProtectionIEC = WindProtectionIEC
		self.WindPlantReactiveControlIEC = WindPlantReactiveControlIEC
		self.WindGenType3bIEC = WindGenType3bIEC
		self.WindPitchContPowerIEC = WindPitchContPowerIEC
		
	def __str__(self):
		str = 'class=WindDynamicsLookupTable\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
