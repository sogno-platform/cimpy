from .GeneratingUnit import GeneratingUnit


class ThermalGeneratingUnit(GeneratingUnit):
	'''
	A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

	:CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant. Default: None
	:CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant. Default: None
	:CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant. Default: None
	:FossilFuels: A thermal generating unit may have one or more fossil fuels. Default: "list"
		'''

	cgmesProfile = GeneratingUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'CAESPlant': [cgmesProfile.EQ.value, ],
						'CogenerationPlant': [cgmesProfile.EQ.value, ],
						'CombinedCyclePlant': [cgmesProfile.EQ.value, ],
						'FossilFuels': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self, CAESPlant = None, CogenerationPlant = None, CombinedCyclePlant = None, FossilFuels = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CAESPlant = CAESPlant
		self.CogenerationPlant = CogenerationPlant
		self.CombinedCyclePlant = CombinedCyclePlant
		self.FossilFuels = FossilFuels
		
	def __str__(self):
		str = 'class=ThermalGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
