from cimpy.cgmes_v2_4_15_flat.ConductingEquipment import ConductingEquipment


class Switch(ConductingEquipment):
	'''
	A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches.

	:normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen. Default: False
	:ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and construction. Default: 0.0
	:retained: Branch is retained in a bus branch model.  The flow through retained switches will normally be calculated in power flow. Default: False
	:open: The attribute tells if the switch is considered open when used as input to topology processing. Default: False
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'normalOpen': [cgmesProfile.EQ.value, ],
						'ratedCurrent': [cgmesProfile.EQ.value, ],
						'retained': [cgmesProfile.EQ.value, ],
						'open': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, normalOpen = False, ratedCurrent = 0.0, retained = False, open = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.normalOpen = normalOpen
		self.ratedCurrent = ratedCurrent
		self.retained = retained
		self.open = open
		
	def __str__(self):
		str = 'class=Switch\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
