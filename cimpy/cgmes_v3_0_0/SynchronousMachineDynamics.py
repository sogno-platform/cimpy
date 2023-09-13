from .RotatingMachineDynamics import RotatingMachineDynamics


class SynchronousMachineDynamics(RotatingMachineDynamics):
	'''
	Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms: - simplified (or classical), where a group of generators or motors is not modelled in detail; - detailed, in equivalent circuit form; - detailed, in time constant reactance form; or <font color="#0f0f0f">- by definition of a user-defined model.</font> <font color="#0f0f0f">It is a common practice to represent small generators by a negative load rather than by a dynamic generator model when performing dynamics simulations. In this case, a SynchronousMachine in the static model is not represented by anything in the dynamics model, instead it is treated as an ordinary load.</font> <font color="#0f0f0f">Parameter details:</font> <ol> 	<li><font color="#0f0f0f">Synchronous machine parameters such as <i>Xl, Xd, Xp</i> etc. are actually used as inductances in the models,</font> but are commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some references use the symbol <i>L</i> instead of <i>X</i>.</li> </ol>

	:SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies. Default: None
	:CrossCompoundTurbineGovernorDyanmics: The cross-compound turbine governor with which this high-pressure synchronous machine is associated. Default: None
	:CrossCompoundTurbineGovernorDynamics: The cross-compound turbine governor with which this low-pressure synchronous machine is associated. Default: None
	:MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model. Default: None
	:ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model. Default: None
	:TurbineGovernorDynamics: Turbine-governor model associated with this synchronous machine model. Multiplicity of greater than one is intended to support hydro units that have multiple turbines on one generator. Default: "list"
	:GenICompensationForGenJ: Compensation of voltage compensator`s generator for current flow out of this  generator. Default: "list"
		'''

	cgmesProfile = RotatingMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'SynchronousMachine': [cgmesProfile.DY.value, ],
						'CrossCompoundTurbineGovernorDyanmics': [cgmesProfile.DY.value, ],
						'CrossCompoundTurbineGovernorDynamics': [cgmesProfile.DY.value, ],
						'MechanicalLoadDynamics': [cgmesProfile.DY.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.DY.value, ],
						'TurbineGovernorDynamics': [cgmesProfile.DY.value, ],
						'GenICompensationForGenJ': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachineDynamics: \n' + RotatingMachineDynamics.__doc__ 

	def __init__(self, SynchronousMachine = None, CrossCompoundTurbineGovernorDyanmics = None, CrossCompoundTurbineGovernorDynamics = None, MechanicalLoadDynamics = None, ExcitationSystemDynamics = None, TurbineGovernorDynamics = "list", GenICompensationForGenJ = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachine = SynchronousMachine
		self.CrossCompoundTurbineGovernorDyanmics = CrossCompoundTurbineGovernorDyanmics
		self.CrossCompoundTurbineGovernorDynamics = CrossCompoundTurbineGovernorDynamics
		self.MechanicalLoadDynamics = MechanicalLoadDynamics
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		self.GenICompensationForGenJ = GenICompensationForGenJ
		
	def __str__(self):
		str = 'class=SynchronousMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
