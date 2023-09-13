from .RegulatingCondEq import RegulatingCondEq


class ShuntCompensator(RegulatingCondEq):
	'''
	A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor. A negative value for bPerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

	:sections: Shunt compensator sections in use. Starting value for steady state solution. The attribute shall be a positive value or zero. Non integer values are allowed to support continuous variables. The reasons for continuous value are to support study cases where no discrete shunt compensators has yet been designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for a continuous solution as input.  For LinearShuntConpensator the value shall be between zero and ShuntCompensator.maximumSections. At value zero the shunt compensator conductance and admittance is zero. Linear interpolation of conductance and admittance between the previous and next integer section is applied in case of non-integer values. For NonlinearShuntCompensator-s shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no interpolation between NonlinearShuntCompenstorPoint-s. Default: 0.0
	:aVRDelay: An automatic voltage regulation delay (AVRDelay) which is the time delay from a change in voltage to when the capacitor is allowed to change state. This filters out temporary changes in voltage. Default: 0
	:grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded. Default: False
	:maximumSections: The maximum number of sections that may be switched in. Default: 0
	:nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the voltage at which the capacitor is connected to the network. Default: 0.0
	:normalSections: The normal number of sections switched in. The value shall be between zero and ShuntCompensator.maximumSections. Default: 0
	:voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. Default: 0.0
	:SvShuntCompensatorSections: The state for the number of shunt compensator sections in service. Default: None
		'''

	cgmesProfile = RegulatingCondEq.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						'sections': [cgmesProfile.SSH.value, ],
						'aVRDelay': [cgmesProfile.EQ.value, ],
						'grounded': [cgmesProfile.EQ.value, ],
						'maximumSections': [cgmesProfile.EQ.value, ],
						'nomU': [cgmesProfile.EQ.value, ],
						'normalSections': [cgmesProfile.EQ.value, ],
						'voltageSensitivity': [cgmesProfile.EQ.value, ],
						'SvShuntCompensatorSections': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, sections = 0.0, aVRDelay = 0, grounded = False, maximumSections = 0, nomU = 0.0, normalSections = 0, voltageSensitivity = 0.0, SvShuntCompensatorSections = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.sections = sections
		self.aVRDelay = aVRDelay
		self.grounded = grounded
		self.maximumSections = maximumSections
		self.nomU = nomU
		self.normalSections = normalSections
		self.voltageSensitivity = voltageSensitivity
		self.SvShuntCompensatorSections = SvShuntCompensatorSections
		
	def __str__(self):
		str = 'class=ShuntCompensator\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
