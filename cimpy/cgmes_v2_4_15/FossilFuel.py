from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class FossilFuel(IdentifiedObject):
	'''
	The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   This a the specific fuels that the generating unit can consume.

	:fossilFuelType: The type of fossil fuel, such as coal, oil, or gas. Default: None
	:ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'fossilFuelType': [cgmesProfile.EQ.value, ],
						'ThermalGeneratingUnit': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, fossilFuelType = None, ThermalGeneratingUnit = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fossilFuelType = fossilFuelType
		self.ThermalGeneratingUnit = ThermalGeneratingUnit
		
	def __str__(self):
		str = 'class=FossilFuel\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
