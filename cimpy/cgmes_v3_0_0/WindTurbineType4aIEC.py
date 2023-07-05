from .WindTurbineType4IEC import WindTurbineType4IEC


class WindTurbineType4aIEC(WindTurbineType4IEC):
	'''
	Wind turbine IEC type 4A. Reference: IEC 61400-27-1:2015, 5.5.5.2.

	:WindContPType4aIEC: Wind control P type 4A model associated with this wind turbine type 4A model. Default: None
	:WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4A model. Default: None
		'''

	cgmesProfile = WindTurbineType4IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindContPType4aIEC': [cgmesProfile.DY.value, ],
						'WindGenType4IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType4IEC: \n' + WindTurbineType4IEC.__doc__ 

	def __init__(self, WindContPType4aIEC = None, WindGenType4IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContPType4aIEC = WindContPType4aIEC
		self.WindGenType4IEC = WindGenType4IEC
		
	def __str__(self):
		str = 'class=WindTurbineType4aIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
