from .DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
	'''
	Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant including their control models.

	:PowerElectronicsConnection: The power electronics connection associated with this wind turbine type 3 or type 4 dynamics model. Default: None
	:RemoteInputSignal: Remote input signal used by these wind turbine type 3 or type 4 models. Default: None
	:WindPlantDynamics: The wind plant with which the wind turbines type 3 or type 4 are associated. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'PowerElectronicsConnection': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'WindPlantDynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, PowerElectronicsConnection = None, RemoteInputSignal = None, WindPlantDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PowerElectronicsConnection = PowerElectronicsConnection
		self.RemoteInputSignal = RemoteInputSignal
		self.WindPlantDynamics = WindPlantDynamics
		
	def __str__(self):
		str = 'class=WindTurbineType3or4Dynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
