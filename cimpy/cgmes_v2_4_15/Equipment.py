from cimpy.cgmes_v2_4_15_flat.PowerSystemResource import PowerSystemResource


class Equipment(PowerSystemResource):
	'''
	The parts of a power system that are physical devices, electronic or mechanical.

	:aggregate: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be power transformers or synchronous machines operating in parallel modeled as a single aggregate power transformer or aggregate synchronous machine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program. Default: False
	:EquipmentContainer: Container of this equipment. Default: None
	:OperationalLimitSet: The operational limit sets associated with this equipment. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'aggregate': [cgmesProfile.EQ.value, ],
						'EquipmentContainer': [cgmesProfile.EQ.value, ],
						'OperationalLimitSet': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, aggregate = False, EquipmentContainer = None, OperationalLimitSet = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.aggregate = aggregate
		self.EquipmentContainer = EquipmentContainer
		self.OperationalLimitSet = OperationalLimitSet
		
	def __str__(self):
		str = 'class=Equipment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
