from cimpy.cgmes_v2_4_15.DynamicsFunctionBlock import DynamicsFunctionBlock


class VoltageAdjusterDynamics(DynamicsFunctionBlock):
	'''
	Voltage adjuster function block whose behaviour is described by reference to a standard model

	:PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model with which this voltage adjuster is associated. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, PFVArControllerType1Dynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
		
	def __str__(self):
		str = 'class=VoltageAdjusterDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
