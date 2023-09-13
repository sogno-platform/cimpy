from .AuxiliaryEquipment import AuxiliaryEquipment


class WaveTrap(AuxiliaryEquipment):
	'''
	Line traps are devices that impede high frequency power line carrier signals yet present a negligible impedance at the main power frequency.

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
		str = 'class=WaveTrap\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
