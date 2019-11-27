from cimpy.cgmes_v2_4_15.RotatingMachineDynamics import RotatingMachineDynamics


class AsynchronousMachineDynamics(RotatingMachineDynamics):
	'''
	Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant reactance form or equivalent circuit form

	:AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies. Default: None
	:MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model. Default: None
	:WindTurbineType1or2Dynamics: Wind generator type 1 or 2 model associated with this asynchronous machine model. Default: None
	:TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model. Default: None
		'''

	cgmesProfile = RotatingMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'AsynchronousMachine': [cgmesProfile.DY.value, ],
						'MechanicalLoadDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2Dynamics': [cgmesProfile.DY.value, ],
						'TurbineGovernorDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachineDynamics: \n' + RotatingMachineDynamics.__doc__ 

	def __init__(self, AsynchronousMachine = None, MechanicalLoadDynamics = None, WindTurbineType1or2Dynamics = None, TurbineGovernorDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.AsynchronousMachine = AsynchronousMachine
		self.MechanicalLoadDynamics = MechanicalLoadDynamics
		self.WindTurbineType1or2Dynamics = WindTurbineType1or2Dynamics
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		
	def __str__(self):
		str = 'class=AsynchronousMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
