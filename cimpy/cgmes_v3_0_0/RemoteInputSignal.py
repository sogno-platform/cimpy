from .IdentifiedObject import IdentifiedObject


class RemoteInputSignal(IdentifiedObject):
	'''
	Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

	:Terminal: Remote terminal with which this input signal is associated. Default: None
	:remoteSignalType: Type of input signal. Default: None
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal. Default: None
	:WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model using this remote input signal. Default: None
	:PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal. Default: None
	:UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal. Default: None
	:PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model using this remote input signal. Default: None
	:VoltageCompensatorDynamics: Voltage compensator model using this remote input signal. Default: None
	:WindPlantDynamics: The wind plant using the remote signal. Default: None
	:WindTurbineType3or4Dynamics: Wind turbine type 3 or type 4 models using this remote input signal. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'Terminal': [cgmesProfile.DY.value, ],
						'remoteSignalType': [cgmesProfile.DY.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2Dynamics': [cgmesProfile.DY.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.DY.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.DY.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.DY.value, ],
						'WindPlantDynamics': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminal = None, remoteSignalType = None, DiscontinuousExcitationControlDynamics = None, WindTurbineType1or2Dynamics = None, PowerSystemStabilizerDynamics = None, UnderexcitationLimiterDynamics = None, PFVArControllerType1Dynamics = None, VoltageCompensatorDynamics = None, WindPlantDynamics = None, WindTurbineType3or4Dynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminal = Terminal
		self.remoteSignalType = remoteSignalType
		self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
		self.WindTurbineType1or2Dynamics = WindTurbineType1or2Dynamics
		self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
		self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
		self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
		self.VoltageCompensatorDynamics = VoltageCompensatorDynamics
		self.WindPlantDynamics = WindPlantDynamics
		self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
		
	def __str__(self):
		str = 'class=RemoteInputSignal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
