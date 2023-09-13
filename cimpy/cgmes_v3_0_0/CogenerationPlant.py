from .PowerSystemResource import PowerSystemResource


class CogenerationPlant(PowerSystemResource):
	'''
	A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.

	:ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant. Default: "list"
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ThermalGeneratingUnits': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, ThermalGeneratingUnits = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ThermalGeneratingUnits = ThermalGeneratingUnits
		
	def __str__(self):
		str = 'class=CogenerationPlant\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
