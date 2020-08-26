from cimpy.output.LoadGroup import LoadGroup


class ConformLoadGroup(LoadGroup):
	'''
	A group of loads conforming to an allocation pattern.

	:EnergyConsumers: Conform loads assigned to this ConformLoadGroup. Default: 
	:ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup. Default: 
		'''

	cgmesProfile = LoadGroup.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'EnergyConsumers': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ConformLoadSchedules': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class LoadGroup: \n' + LoadGroup.__doc__ 

	def __init__(self, EnergyConsumers = , ConformLoadSchedules = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergyConsumers = EnergyConsumers
		self.ConformLoadSchedules = ConformLoadSchedules
		
	def __str__(self):
		str = 'class=ConformLoadGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
