from cimpy.output.RegulatingCondEq import RegulatingCondEq


class ShuntCompensator(RegulatingCondEq):
	'''
	A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

	:aVRDelay: Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR). Default: 
	:grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded. Default: 
	:maximumSections: The maximum number of sections that may be switched in. Default: 
	:nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the voltage at which the capacitor is connected to the network. Default: 
	:normalSections: The normal number of sections switched in. Default: 
	:switchOnCount: The switch on count since the capacitor count was last reset or initialized. Default: 
	:switchOnDate: The date and time when the capacitor bank was last switched on. Default: 
	:voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. Default: 
	:sections: Shunt compensator sections in use. Starting value for steady state solution. Non integer values are allowed to support continuous variables. The reasons for continuous value are to support study cases where no discrete shunt compensators has yet been designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for a continuous solution as input. Default: 
	:SvShuntCompensatorSections: The state for the number of shunt compensator sections in service. Default: 
		'''

	cgmesProfile = RegulatingCondEq.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'aVRDelay': [cgmesProfile.EQ.value, ],
						'grounded': [cgmesProfile.EQ.value, ],
						'maximumSections': [cgmesProfile.EQ.value, ],
						'nomU': [cgmesProfile.EQ.value, ],
						'normalSections': [cgmesProfile.EQ.value, ],
						'switchOnCount': [cgmesProfile.EQ.value, ],
						'switchOnDate': [cgmesProfile.EQ.value, ],
						'voltageSensitivity': [cgmesProfile.EQ.value, ],
						'sections': [cgmesProfile.SSH.value, ],
						'SvShuntCompensatorSections': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, aVRDelay = , grounded = , maximumSections = , nomU = , normalSections = , switchOnCount = , switchOnDate = , voltageSensitivity = , sections = , SvShuntCompensatorSections = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.aVRDelay = aVRDelay
		self.grounded = grounded
		self.maximumSections = maximumSections
		self.nomU = nomU
		self.normalSections = normalSections
		self.switchOnCount = switchOnCount
		self.switchOnDate = switchOnDate
		self.voltageSensitivity = voltageSensitivity
		self.sections = sections
		self.SvShuntCompensatorSections = SvShuntCompensatorSections
		
	def __str__(self):
		str = 'class=ShuntCompensator\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
