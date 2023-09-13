from .DynamicsFunctionBlock import DynamicsFunctionBlock


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
	'''
	Power factor or VAr controller type 1 function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

	:RemoteInputSignal: Remote input signal used by this power factor or VAr controller type 1 model. Default: None
	:ExcitationSystemDynamics: Excitation system model with which this power actor or VAr controller type 1 model is associated. Default: None
	:VoltageAdjusterDynamics: Voltage adjuster model associated with this power factor or VAr controller type 1 model. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.DY.value, ],
						'VoltageAdjusterDynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

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
