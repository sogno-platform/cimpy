from .RotatingMachineDynamics import RotatingMachineDynamics


class AsynchronousMachineDynamics(RotatingMachineDynamics):
	'''
	Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant reactance form or equivalent circuit form <font color="#0f0f0f">or by definition of a user-defined model.</font> Parameter details: <ol> 	<li>Asynchronous machine parameters such as <i>Xl, Xs,</i> etc. are actually used as inductances in the model, but are commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some references use the symbol <i>L</i> instead of <i>X</i>.</li> </ol>

	:AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies. Default: None
	:TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model. Default: None
	:MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model. Default: None
	:WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model associated with this asynchronous machine model. Default: None
		'''

	cgmesProfile = RotatingMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'AsynchronousMachine': [cgmesProfile.DY.value, ],
						'TurbineGovernorDynamics': [cgmesProfile.DY.value, ],
						'MechanicalLoadDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2Dynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachineDynamics: \n' + RotatingMachineDynamics.__doc__ 

	def __init__(self, AsynchronousMachine = None, TurbineGovernorDynamics = None, MechanicalLoadDynamics = None, WindTurbineType1or2Dynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.AsynchronousMachine = AsynchronousMachine
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		self.MechanicalLoadDynamics = MechanicalLoadDynamics
		self.WindTurbineType1or2Dynamics = WindTurbineType1or2Dynamics
		
	def __str__(self):
		str = 'class=AsynchronousMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
