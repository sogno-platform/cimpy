from cimpy.output.EnergyArea import EnergyArea


class SubLoadArea(EnergyArea):
	'''
	The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

	:LoadArea: The LoadArea where the SubLoadArea belongs. Default: 
	:LoadGroups: The Loadgroups in the SubLoadArea. Default: 
		'''

	cgmesProfile = EnergyArea.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'LoadArea': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'LoadGroups': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EnergyArea: \n' + EnergyArea.__doc__ 

	def __init__(self, LoadArea = , LoadGroups = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadArea = LoadArea
		self.LoadGroups = LoadGroups
		
	def __str__(self):
		str = 'class=SubLoadArea\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
