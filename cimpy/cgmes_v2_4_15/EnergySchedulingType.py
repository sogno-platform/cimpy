from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class EnergySchedulingType(IdentifiedObject):
	'''
	Used to define the type of generation for scheduling purposes.

	:EnergySource: Energy Scheduling Type of an Energy Source Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'EnergySource': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, EnergySource = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergySource = EnergySource
		
	def __str__(self):
		str = 'class=EnergySchedulingType\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
