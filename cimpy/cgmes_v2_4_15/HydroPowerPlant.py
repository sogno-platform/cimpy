from cimpy.cgmes_v2_4_15.PowerSystemResource import PowerSystemResource


class HydroPowerPlant(PowerSystemResource):
	'''
	A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

	:HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant. Default: "many"
	:hydroPlantStorageType: The type of hydro power plant water storage. Default: None
	:HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: "many"
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'HydroGeneratingUnits': [cgmesProfile.EQ.value, ],
						'hydroPlantStorageType': [cgmesProfile.EQ.value, ],
						'HydroPumps': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, HydroGeneratingUnits = "many", hydroPlantStorageType = None, HydroPumps = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.HydroGeneratingUnits = HydroGeneratingUnits
		self.hydroPlantStorageType = hydroPlantStorageType
		self.HydroPumps = HydroPumps
		
	def __str__(self):
		str = 'class=HydroPowerPlant\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
