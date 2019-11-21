from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class RemoteInputSignal(IdentifiedObject):
	'''
	Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

	:Terminal: Remote terminal with which this input signal is associated. Default: None
	:remoteSignalType: Type of input signal. Default: None
	:PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model using this remote input signal. Default: None
	:UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal. Default: None
	:WindTurbineType1or2Dynamics: Wind generator Type 1 or Type 2 model using this remote input signal. Default: None
	:VoltageCompensatorDynamics: Voltage compensator model using this remote input signal. Default: None
	:PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal. Default: None
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal. Default: None
	:WindTurbineType3or4Dynamics: Remote input signal used by these wind turbine Type 3 or 4 models. Default: None
	:WindPlantDynamics: The remote signal with which this power plant is associated. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'Terminal': [cgmesProfile.DY.value, ],
						'remoteSignalType': [cgmesProfile.DY.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.DY.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2Dynamics': [cgmesProfile.DY.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.DY.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.DY.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.DY.value, ],
						'WindPlantDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminal = None, remoteSignalType = None, PFVArControllerType1Dynamics = None, UnderexcitationLimiterDynamics = None, WindTurbineType1or2Dynamics = None, VoltageCompensatorDynamics = None, PowerSystemStabilizerDynamics = None, DiscontinuousExcitationControlDynamics = None, WindTurbineType3or4Dynamics = None, WindPlantDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminal = Terminal
		self.remoteSignalType = remoteSignalType
		self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
		self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
		self.WindTurbineType1or2Dynamics = WindTurbineType1or2Dynamics
		self.VoltageCompensatorDynamics = VoltageCompensatorDynamics
		self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
		self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
		self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
		self.WindPlantDynamics = WindPlantDynamics
		
	def __str__(self):
		str = 'class=RemoteInputSignal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
