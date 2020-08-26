from cimpy.output.PowerSystemResource import PowerSystemResource


class RegulatingControl(PowerSystemResource):
	'''
	Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment. In case multiple equipment, possibly of different types, control same terminal there must be only one RegulatingControl at that terminal. The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow control  load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.

	:Terminal: The controls regulating this terminal. Default: 
	:RegulatingCondEq: The equipment that participates in this regulating control scheme. Default: 
	:mode: The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. Default: 
	:RegulationSchedule: Schedule for this Regulating regulating control. Default: 
	:discrete: The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap changers and shunt compensators. Default: 
	:enabled: The flag tells if regulation is enabled. Default: 
	:targetDeadband: This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating. The units of those appropriate for the mode. Default: 
	:targetValue: The target value specified for case input.   This value can be used for the target value without the use of schedules. The value has the units appropriate to the mode attribute. Default: 
	:targetValueUnitMultiplier: Specify the multiplier for used for the targetValue. Default: 
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'Terminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'RegulatingCondEq': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'mode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'RegulationSchedule': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'discrete': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'enabled': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'targetDeadband': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'targetValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'targetValueUnitMultiplier': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, Terminal = , RegulatingCondEq = , mode = , RegulationSchedule = , discrete = , enabled = , targetDeadband = , targetValue = , targetValueUnitMultiplier = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminal = Terminal
		self.RegulatingCondEq = RegulatingCondEq
		self.mode = mode
		self.RegulationSchedule = RegulationSchedule
		self.discrete = discrete
		self.enabled = enabled
		self.targetDeadband = targetDeadband
		self.targetValue = targetValue
		self.targetValueUnitMultiplier = targetValueUnitMultiplier
		
	def __str__(self):
		str = 'class=RegulatingControl\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
