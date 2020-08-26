from cimpy.output.IdentifiedObject import IdentifiedObject


class RemoteInputSignal(IdentifiedObject):
	'''
	Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

	:Terminal: Remote terminal with which this input signal is associated. Default: 
	:remoteSignalType: Type of input signal. Default: 
	:PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model using this remote input signal. Default: 
	:UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal. Default: 
	:WindTurbineType1or2Dynamics: Wind generator Type 1 or Type 2 model using this remote input signal. Default: 
	:VoltageCompensatorDynamics: Voltage compensator model using this remote input signal. Default: 
	:PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal. Default: 
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal. Default: 
	:WindTurbineType3or4Dynamics: Remote input signal used by these wind turbine Type 3 or 4 models. Default: 
	:WindPlantDynamics: The remote signal with which this power plant is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'Terminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'remoteSignalType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType1or2Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindPlantDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminal = , remoteSignalType = , PFVArControllerType1Dynamics = , UnderexcitationLimiterDynamics = , WindTurbineType1or2Dynamics = , VoltageCompensatorDynamics = , PowerSystemStabilizerDynamics = , DiscontinuousExcitationControlDynamics = , WindTurbineType3or4Dynamics = , WindPlantDynamics = ,  *args, **kw_args):
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
