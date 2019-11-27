from cimpy.cgmes_v2_4_15.GeneratingUnit import GeneratingUnit


class HydroGeneratingUnit(GeneratingUnit):
	'''
	A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

	:energyConversionCapability: Energy conversion capability for generating. Default: None
	:HydroPowerPlant: The hydro generating unit belongs to a hydro power plant. Default: None
		'''

	cgmesProfile = GeneratingUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'energyConversionCapability': [cgmesProfile.EQ.value, ],
						'HydroPowerPlant': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self, energyConversionCapability = None, HydroPowerPlant = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.energyConversionCapability = energyConversionCapability
		self.HydroPowerPlant = HydroPowerPlant
		
	def __str__(self):
		str = 'class=HydroGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
