from .PowerSystemResource import PowerSystemResource


class WindPowerPlant(PowerSystemResource):
	'''
	Wind power plant.

	:WindGeneratingUnits: A wind generating unit or units may be a member of a wind power plant. Default: "list"
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'WindGeneratingUnits': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, WindGeneratingUnits = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindGeneratingUnits = WindGeneratingUnits
		
	def __str__(self):
		str = 'class=WindPowerPlant\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
