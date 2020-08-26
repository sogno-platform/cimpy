from cimpy.cgmes_v2_4_15.EarthFaultCompensator import EarthFaultCompensator


class PetersenCoil(EarthFaultCompensator):
	'''
	A tunable impedance device normally used to offset line charging during single line faults in an ungrounded section of network.

	:mode: The mode of operation of the Petersen coil. Default: 
	:nominalU: The nominal voltage for which the coil is designed. Default: 
	:offsetCurrent: The offset current that the Petersen coil controller is operating from the resonant point.  This is normally a fixed amount for which the controller is configured and could be positive or negative.  Typically 0 to 60 Amperes depending on voltage and resonance conditions. Default: 
	:positionCurrent: The control current used to control the Petersen coil also known as the position current.  Typically in the range of 20-200mA. Default: 
	:xGroundMax: The maximum reactance. Default: 
	:xGroundMin: The minimum reactance. Default: 
	:xGroundNominal: The nominal reactance.  This is the operating point (normally over compensation) that is defined based on the resonance point in the healthy network condition.  The impedance is calculated based on nominal voltage divided by position current. Default: 
		'''

	cgmesProfile = EarthFaultCompensator.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'mode': [cgmesProfile.EQ.value, ],
						'nominalU': [cgmesProfile.EQ.value, ],
						'offsetCurrent': [cgmesProfile.EQ.value, ],
						'positionCurrent': [cgmesProfile.EQ.value, ],
						'xGroundMax': [cgmesProfile.EQ.value, ],
						'xGroundMin': [cgmesProfile.EQ.value, ],
						'xGroundNominal': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EarthFaultCompensator: \n' + EarthFaultCompensator.__doc__ 

	def __init__(self, mode = , nominalU = , offsetCurrent = , positionCurrent = , xGroundMax = , xGroundMin = , xGroundNominal = ,  *args, **kw_args):
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
