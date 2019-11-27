from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
	'''
	Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

	:RemoteInputSignal: Remote input signal used by this Power Factor or VAr controller Type I model. Default: None
	:ExcitationSystemDynamics: Excitation system model with which this Power Factor or VAr controller Type I model is associated. Default: None
	:VoltageAdjusterDynamics: Voltage adjuster model associated with this Power Factor or VA controller Type I model. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.DY.value, ],
						'VoltageAdjusterDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = None, ExcitationSystemDynamics = None, VoltageAdjusterDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		self.VoltageAdjusterDynamics = VoltageAdjusterDynamics
		
	def __str__(self):
		str = 'class=PFVArControllerType1Dynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
