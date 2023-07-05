from .AuxiliaryEquipment import AuxiliaryEquipment


class SurgeArrester(AuxiliaryEquipment):
	'''
	Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage transients caused by lightning or switching activity.

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
		str = 'class=SurgeArrester\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
