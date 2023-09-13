from .Equipment import Equipment


class AuxiliaryEquipment(Equipment):
	'''
	AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function. AuxiliaryEquipment is attached to primary equipment via an association with Terminal.

	:Terminal: The Terminal at the equipment where the AuxiliaryEquipment is attached. Default: None
		'''

	cgmesProfile = Equipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Equipment: \n' + Equipment.__doc__ 

	def __init__(self, Terminal = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminal = Terminal
		
	def __str__(self):
		str = 'class=AuxiliaryEquipment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
