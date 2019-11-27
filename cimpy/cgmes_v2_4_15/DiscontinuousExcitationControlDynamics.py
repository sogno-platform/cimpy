from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class DiscontinuousExcitationControlDynamics(DynamicsFunctionBlock):
	'''
	Discontinuous excitation control function block whose behaviour is described by reference to a standard model .

	:RemoteInputSignal: Remote input signal used by this discontinuous excitation control system model. Default: None
	:ExcitationSystemDynamics: Excitation system model with which this discontinuous excitation control model is associated. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = None, ExcitationSystemDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		
	def __str__(self):
		str = 'class=DiscontinuousExcitationControlDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
