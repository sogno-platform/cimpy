from .ConductingEquipment import ConductingEquipment


class EquivalentEquipment(ConductingEquipment):
	'''
	The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.

	:EquivalentNetwork: The equivalent where the reduced model belongs. Default: None
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, ],
						'EquivalentNetwork': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, EquivalentNetwork = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EquivalentNetwork = EquivalentNetwork
		
	def __str__(self):
		str = 'class=EquivalentEquipment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
