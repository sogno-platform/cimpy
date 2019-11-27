from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
	'''
	Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant including their control models.

	:EnergySource: Energy Source (current source) with which this wind Type 3 or 4 dynamics model is asoociated. Default: None
	:RemoteInputSignal: Wind turbine Type 3 or 4 models using this remote input signal. Default: None
	:WindPlantDynamics: The wind plant with which the wind turbines type 3 or 4 are associated. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'EnergySource': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'WindPlantDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, EnergySource = None, RemoteInputSignal = None, WindPlantDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergySource = EnergySource
		self.RemoteInputSignal = RemoteInputSignal
		self.WindPlantDynamics = WindPlantDynamics
		
	def __str__(self):
		str = 'class=WindTurbineType3or4Dynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
