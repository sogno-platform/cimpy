from .ConductingEquipment import ConductingEquipment


class Switch(ConductingEquipment):
	'''
	A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant.

	:open: The attribute tells if the switch is considered open when used as input to topology processing. Default: False
	:locked: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows: <ul> 	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li> 	<li>locked=false and Switch.open=true. The resulting state is open;</li> 	<li>locked=false and Switch.open=false. The resulting state is closed.</li> </ul> Default: False
	:normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen. Default: False
	:ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and construction. The attribute shall be a positive value. Default: 0.0
	:retained: Branch is retained in the topological solution.  The flow through retained switches will normally be calculated in power flow. Default: False
	:SwitchSchedules: A Switch can be associated with SwitchSchedules. Default: "list"
	:SvSwitch: The switch state associated with the switch. Default: "list"
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SV.value, ],
						'open': [cgmesProfile.SSH.value, ],
						'locked': [cgmesProfile.SSH.value, ],
						'normalOpen': [cgmesProfile.EQ.value, ],
						'ratedCurrent': [cgmesProfile.EQ.value, ],
						'retained': [cgmesProfile.EQ.value, ],
						'SwitchSchedules': [cgmesProfile.EQ.value, ],
						'SvSwitch': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, open = False, locked = False, normalOpen = False, ratedCurrent = 0.0, retained = False, SwitchSchedules = "list", SvSwitch = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.open = open
		self.locked = locked
		self.normalOpen = normalOpen
		self.ratedCurrent = ratedCurrent
		self.retained = retained
		self.SwitchSchedules = SwitchSchedules
		self.SvSwitch = SvSwitch
		
	def __str__(self):
		str = 'class=Switch\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
