from cimpy.cgmes_v2_4_15_flat.EarthFaultCompensator import EarthFaultCompensator


class PetersenCoil(EarthFaultCompensator):
	'''
	A tunable impedance device normally used to offset line charging during single line faults in an ungrounded section of network.

	:mode: The mode of operation of the Petersen coil. Default: None
	:nominalU: The nominal voltage for which the coil is designed. Default: 0.0
	:offsetCurrent: The offset current that the Petersen coil controller is operating from the resonant point.  This is normally a fixed amount for which the controller is configured and could be positive or negative.  Typically 0 to 60 Amperes depending on voltage and resonance conditions. Default: 0.0
	:positionCurrent: The control current used to control the Petersen coil also known as the position current.  Typically in the range of 20-200mA. Default: 0.0
	:xGroundMax: The maximum reactance. Default: 0.0
	:xGroundMin: The minimum reactance. Default: 0.0
	:xGroundNominal: The nominal reactance.  This is the operating point (normally over compensation) that is defined based on the resonance point in the healthy network condition.  The impedance is calculated based on nominal voltage divided by position current. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'mode': [cgmesProfile.EQ.value, ],
						'nominalU': [cgmesProfile.EQ.value, ],
						'offsetCurrent': [cgmesProfile.EQ.value, ],
						'positionCurrent': [cgmesProfile.EQ.value, ],
						'xGroundMax': [cgmesProfile.EQ.value, ],
						'xGroundMin': [cgmesProfile.EQ.value, ],
						'xGroundNominal': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EarthFaultCompensator: \n' + EarthFaultCompensator.__doc__ 

	def __init__(self, mode = None, nominalU = 0.0, offsetCurrent = 0.0, positionCurrent = 0.0, xGroundMax = 0.0, xGroundMin = 0.0, xGroundNominal = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mode = mode
		self.nominalU = nominalU
		self.offsetCurrent = offsetCurrent
		self.positionCurrent = positionCurrent
		self.xGroundMax = xGroundMax
		self.xGroundMin = xGroundMin
		self.xGroundNominal = xGroundNominal
		
	def __str__(self):
		str = 'class=PetersenCoil\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
