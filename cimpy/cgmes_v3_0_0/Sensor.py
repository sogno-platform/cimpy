from .AuxiliaryEquipment import AuxiliaryEquipment


class Sensor(AuxiliaryEquipment):
	'''
	This class describe devices that transform a measured quantity into signals that can be presented at displays, used in control or be recorded.

		'''

	cgmesProfile = AuxiliaryEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class AuxiliaryEquipment: \n' + AuxiliaryEquipment.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=Sensor\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
