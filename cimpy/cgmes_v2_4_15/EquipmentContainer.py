from .ConnectivityNodeContainer import ConnectivityNodeContainer


class EquipmentContainer(ConnectivityNodeContainer):
	'''
	A modeling construct to provide a root class for containing equipment.

	:Equipments: Contained equipment. Default: "list"
		'''

	cgmesProfile = ConnectivityNodeContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.EQ_BD.value, ],
						'Equipments': [cgmesProfile.EQ.value, cgmesProfile.EQ_BD.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConnectivityNodeContainer: \n' + ConnectivityNodeContainer.__doc__ 

	def __init__(self, Equipments = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Equipments = Equipments
		
	def __str__(self):
		str = 'class=EquipmentContainer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
