from cimpy.cgmes_v2_4_15.LoadGroup import LoadGroup


class ConformLoadGroup(LoadGroup):
	'''
	A group of loads conforming to an allocation pattern.

	:EnergyConsumers: Conform loads assigned to this ConformLoadGroup. Default: "many"
	:ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup. Default: "many"
		'''

	cgmesProfile = LoadGroup.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'EnergyConsumers': [cgmesProfile.EQ.value, ],
						'ConformLoadSchedules': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class LoadGroup: \n' + LoadGroup.__doc__ 

	def __init__(self, EnergyConsumers = "many", ConformLoadSchedules = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergyConsumers = EnergyConsumers
		self.ConformLoadSchedules = ConformLoadSchedules
		
	def __str__(self):
		str = 'class=ConformLoadGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
