from cimpy.cgmes_v2_4_15_flat.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
	'''
	Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control models.

	:WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or 4 model. Default: None
	:WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or 4 model. Default: None
	:WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or 4 model. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindContCurrLimIEC': [cgmesProfile.DY.value, ],
						'WIndContQIEC': [cgmesProfile.DY.value, ],
						'WindProtectionIEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4Dynamics: \n' + WindTurbineType3or4Dynamics.__doc__ 

	def __init__(self, WindContCurrLimIEC = None, WIndContQIEC = None, WindProtectionIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContCurrLimIEC = WindContCurrLimIEC
		self.WIndContQIEC = WIndContQIEC
		self.WindProtectionIEC = WindProtectionIEC
		
	def __str__(self):
		str = 'class=WindTurbineType3or4IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
