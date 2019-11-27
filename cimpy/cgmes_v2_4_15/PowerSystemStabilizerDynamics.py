from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
	'''
	Power system stabilizer function block whose behaviour is described by reference to a standard model

	:RemoteInputSignal: Remote input signal used by this power system stabilizer model. Default: []
	:ExcitationSystemDynamics: Excitation system model with which this power system stabilizer model is associated. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = [], ExcitationSystemDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		
	def __str__(self):
		str = 'class=PowerSystemStabilizerDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
