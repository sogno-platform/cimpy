from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
	'''
	Turbine load controller function block whose behavior is described by reference to a standard model

	:TurbineGovernorDynamics: Turbine-governor controlled by this turbine load controller. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'TurbineGovernorDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, TurbineGovernorDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		
	def __str__(self):
		str = 'class=TurbineLoadControllerDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
