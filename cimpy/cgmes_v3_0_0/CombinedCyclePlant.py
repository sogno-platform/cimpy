from .PowerSystemResource import PowerSystemResource


class CombinedCyclePlant(PowerSystemResource):
	'''
	A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency.

	:ThermalGeneratingUnits: A thermal generating unit may be a member of a combined cycle plant. Default: "list"
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
		str = 'class=CombinedCyclePlant\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
