from cimpy.output.RotatingMachineDynamics import RotatingMachineDynamics


class SynchronousMachineDynamics(RotatingMachineDynamics):
	'''
	Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms:

	:SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies. Default: 
	:TurbineGovernorDynamics: Synchronous machine model with which this turbine-governor model is associated. Default: 
	:ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model. Default: 
	:MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model. Default: 
	:GenICompensationForGenJ: Compensation of voltage compensator`s generator for current flow out of this  generator. Default: 
		'''

	cgmesProfile = RotatingMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'SynchronousMachine': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'TurbineGovernorDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'MechanicalLoadDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'GenICompensationForGenJ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachineDynamics: \n' + RotatingMachineDynamics.__doc__ 

	def __init__(self, SynchronousMachine = , TurbineGovernorDynamics = , ExcitationSystemDynamics = , MechanicalLoadDynamics = , GenICompensationForGenJ = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachine = SynchronousMachine
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		self.MechanicalLoadDynamics = MechanicalLoadDynamics
		self.GenICompensationForGenJ = GenICompensationForGenJ
		
	def __str__(self):
		str = 'class=SynchronousMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
