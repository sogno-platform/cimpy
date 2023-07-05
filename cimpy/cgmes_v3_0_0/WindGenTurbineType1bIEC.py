from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


class WindGenTurbineType1bIEC(WindTurbineType1or2IEC):
	'''
	Wind turbine IEC type 1B.  Reference: IEC 61400-27-1:2015, 5.5.2.3.

	:WindPitchContPowerIEC: Pitch control power model associated with this wind turbine type 1B model. Default: None
		'''

	cgmesProfile = WindTurbineType1or2IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindPitchContPowerIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType1or2IEC: \n' + WindTurbineType1or2IEC.__doc__ 

	def __init__(self, WindPitchContPowerIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindPitchContPowerIEC = WindPitchContPowerIEC
		
	def __str__(self):
		str = 'class=WindGenTurbineType1bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
