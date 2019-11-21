from cimpy.cgmes_v2_4_15_flat.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindGenTurbineType3IEC(WindTurbineType3or4IEC):
	'''
	Generator model for wind turbines of IEC type 3A and 3B.

	:WindAeroLinearIEC: Wind aerodynamic model associated with this wind generator type 3 model. Default: None
	:WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3. Default: None
	:WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model. Default: None
	:dipmax: Maximum active current ramp rate (di). It is project dependent parameter. Default: 0.0
	:diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 0.0
	:WindMechIEC: Wind mechanical model associated with this wind turbine Type 3 model. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindAeroLinearIEC': [cgmesProfile.DY.value, ],
						'WindContPitchAngleIEC': [cgmesProfile.DY.value, ],
						'WindContPType3IEC': [cgmesProfile.DY.value, ],
						'dipmax': [cgmesProfile.DY.value, ],
						'diqmax': [cgmesProfile.DY.value, ],
						'WindMechIEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4IEC: \n' + WindTurbineType3or4IEC.__doc__ 

	def __init__(self, WindAeroLinearIEC = None, WindContPitchAngleIEC = None, WindContPType3IEC = None, dipmax = 0.0, diqmax = 0.0, WindMechIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindAeroLinearIEC = WindAeroLinearIEC
		self.WindContPitchAngleIEC = WindContPitchAngleIEC
		self.WindContPType3IEC = WindContPType3IEC
		self.dipmax = dipmax
		self.diqmax = diqmax
		self.WindMechIEC = WindMechIEC
		
	def __str__(self):
		str = 'class=WindGenTurbineType3IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
