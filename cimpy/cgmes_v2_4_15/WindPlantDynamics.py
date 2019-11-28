from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class WindPlantDynamics(DynamicsFunctionBlock):
	'''
	Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant IEC and user defined wind plants including their control models.

	:RemoteInputSignal: The wind plant using the remote signal. Default: None
	:WindTurbineType3or4Dynamics: The wind turbine type 3 or 4 associated with this wind plant. Default: "many"
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = None, WindTurbineType3or4Dynamics = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
		
	def __str__(self):
		str = 'class=WindPlantDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
