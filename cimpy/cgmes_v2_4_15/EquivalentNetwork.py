from cimpy.cgmes_v2_4_15.ConnectivityNodeContainer import ConnectivityNodeContainer


class EquivalentNetwork(ConnectivityNodeContainer):
	'''
	A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.

	:EquivalentEquipments: The equivalent where the reduced model belongs. Default: []
		'''

	cgmesProfile = ConnectivityNodeContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'EquivalentEquipments': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConnectivityNodeContainer: \n' + ConnectivityNodeContainer.__doc__ 

	def __init__(self, EquivalentEquipments = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EquivalentEquipments = EquivalentEquipments
		
	def __str__(self):
		str = 'class=EquivalentNetwork\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
