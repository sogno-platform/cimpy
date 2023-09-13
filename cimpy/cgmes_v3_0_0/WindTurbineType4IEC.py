from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindTurbineType4IEC(WindTurbineType3or4IEC):
	'''
	Parent class supporting relationships to IEC wind turbines type 4 including their control models.

	:WindGenType3aIEC: Wind generator type 3A model associated with this wind turbine type 4 model. Default: None
		'''

	cgmesProfile = WindTurbineType3or4IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindGenType3aIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4IEC: \n' + WindTurbineType3or4IEC.__doc__ 

	def __init__(self, WindGenType3aIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindGenType3aIEC = WindGenType3aIEC
		
	def __str__(self):
		str = 'class=WindTurbineType4IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
