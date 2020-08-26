from cimpy.output.PowerSystemResource import PowerSystemResource


class HydroPowerPlant(PowerSystemResource):
	'''
	A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

	:HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant. Default: 
	:hydroPlantStorageType: The type of hydro power plant water storage. Default: 
	:HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: 
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HydroGeneratingUnits': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'hydroPlantStorageType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HydroPumps': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, HydroGeneratingUnits = , hydroPlantStorageType = , HydroPumps = ,  *args, **kw_args):
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
