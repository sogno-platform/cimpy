from .PowerElectronicsUnit import PowerElectronicsUnit


class PhotoVoltaicUnit(PowerElectronicsUnit):
	'''
	A photovoltaic device or an aggregation of such devices.

		'''

	cgmesProfile = PowerElectronicsUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerElectronicsUnit: \n' + PowerElectronicsUnit.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=PhotoVoltaicUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
