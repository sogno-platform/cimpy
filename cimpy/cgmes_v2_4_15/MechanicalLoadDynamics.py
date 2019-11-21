from cimpy.cgmes_v2_4_15_flat.DynamicsFunctionBlock import DynamicsFunctionBlock


class MechanicalLoadDynamics(DynamicsFunctionBlock):
	'''
	Mechanical load function block whose behavior is described by reference to a standard model

	:SynchronousMachineDynamics: Synchronous machine model with which this mechanical load model is associated. Default: None
	:AsynchronousMachineDynamics: Asynchronous machine model with which this mechanical load model is associated. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = None, AsynchronousMachineDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachineDynamics = SynchronousMachineDynamics
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		
	def __str__(self):
		str = 'class=MechanicalLoadDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
