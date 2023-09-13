from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindTurbineType3IEC(WindTurbineType3or4IEC):
	'''
	Parent class supporting relationships to IEC wind turbines type 3 including their control models.

	:WindAeroOneDimIEC: Wind aerodynamic model associated with this wind generator type 3 model. Default: None
	:WindAeroTwoDimIEC: Wind aerodynamic model associated with this wind turbine type 3 model. Default: None
	:WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3. Default: None
	:WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model. Default: None
	:WindGenType3IEC: Wind generator type 3 model associated with this wind turbine type 3 model. Default: None
	:WindMechIEC: Wind mechanical model associated with this wind turbine type 3 model. Default: None
		'''

	cgmesProfile = WindTurbineType3or4IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindAeroOneDimIEC': [cgmesProfile.DY.value, ],
						'WindAeroTwoDimIEC': [cgmesProfile.DY.value, ],
						'WindContPitchAngleIEC': [cgmesProfile.DY.value, ],
						'WindContPType3IEC': [cgmesProfile.DY.value, ],
						'WindGenType3IEC': [cgmesProfile.DY.value, ],
						'WindMechIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4IEC: \n' + WindTurbineType3or4IEC.__doc__ 

	def __init__(self, WindAeroOneDimIEC = None, WindAeroTwoDimIEC = None, WindContPitchAngleIEC = None, WindContPType3IEC = None, WindGenType3IEC = None, WindMechIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindAeroOneDimIEC = WindAeroOneDimIEC
		self.WindAeroTwoDimIEC = WindAeroTwoDimIEC
		self.WindContPitchAngleIEC = WindContPitchAngleIEC
		self.WindContPType3IEC = WindContPType3IEC
		self.WindGenType3IEC = WindGenType3IEC
		self.WindMechIEC = WindMechIEC
		
	def __str__(self):
		str = 'class=WindTurbineType3IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
