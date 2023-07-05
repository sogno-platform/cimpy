from .DynamicsFunctionBlock import DynamicsFunctionBlock


class TurbineGovernorDynamics(DynamicsFunctionBlock):
	'''
	Turbine-governor function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

	:SynchronousMachineDynamics: Synchronous machine model with which this turbine-governor model is associated. TurbineGovernorDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics. Default: None
	:AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated. TurbineGovernorDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics. Default: None
	:TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'TurbineLoadControllerDynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = None, AsynchronousMachineDynamics = None, TurbineLoadControllerDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachineDynamics = SynchronousMachineDynamics
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		self.TurbineLoadControllerDynamics = TurbineLoadControllerDynamics
		
	def __str__(self):
		str = 'class=TurbineGovernorDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
