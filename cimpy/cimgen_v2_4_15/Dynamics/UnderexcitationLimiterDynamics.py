from cimpy.cimgen_v2_4_15.Dynamics.DynamicsFunctionBlock import DynamicsFunctionBlock


class UnderexcitationLimiterDynamics(DynamicsFunctionBlock):
	'''
	Underexcitation limiter function block whose behaviour is described by reference to a standard model

	:RemoteInputSignal: Remote input signal used by this underexcitation limiter model. Default: None
	:ExcitationSystemDynamics: Excitation system model with which this underexcitation limiter model is associated. Default: None
		'''

	

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = None, ExcitationSystemDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		
	def __str__(self):
		str = 'class=UnderexcitationLimiterDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
