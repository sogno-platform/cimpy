from .ACDCTerminal import ACDCTerminal


class Terminal(ACDCTerminal):
	'''
	An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

	:ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: None
	:RemoteInputSignal: Input signal coming from this terminal. Default: "list"
	:TopologicalNode: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unnecessary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: None
	:ConverterDCSides: All converters` DC sides linked to this point of common coupling terminal. Default: "list"
	:AuxiliaryEquipment: The auxiliary equipment connected to the terminal. Default: "list"
	:ConnectivityNode: The connectivity node to which this terminal connects with zero impedance. Default: None
	:RegulatingControl: The controls regulating this terminal. Default: "list"
	:phases: Represents the normal network phasing condition. If the attribute is missing, three phases (ABC) shall be assumed, except for terminals of grounding classes (specializations of EarthFaultCompensator, GroundDisconnector, and Ground) which will be assumed to be N. Therefore, phase code ABCN is explicitly declared when needed, e.g. for star point grounding equipment. The phase code on terminals connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two terminals shall be consistent. Default: None
	:TransformerEnd: All transformer ends connected at this terminal. Default: "list"
	:TieFlow: The control area tie flows to which this terminal associates. Default: "list"
	:HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch. Default: "list"
	:HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch. Default: "list"
	:SvPowerFlow: The power flow state variable associated with the terminal. Default: None
		'''

	cgmesProfile = ACDCTerminal.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.TP.value, cgmesProfile.OP.value, cgmesProfile.EQ.value, cgmesProfile.EQBD.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						'ConductingEquipment': [cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'RemoteInputSignal': [cgmesProfile.DY.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						'ConverterDCSides': [cgmesProfile.EQ.value, ],
						'AuxiliaryEquipment': [cgmesProfile.EQ.value, ],
						'ConnectivityNode': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'RegulatingControl': [cgmesProfile.EQ.value, ],
						'phases': [cgmesProfile.EQ.value, ],
						'TransformerEnd': [cgmesProfile.EQ.value, ],
						'TieFlow': [cgmesProfile.EQ.value, ],
						'HasSecondMutualCoupling': [cgmesProfile.SC.value, ],
						'HasFirstMutualCoupling': [cgmesProfile.SC.value, ],
						'SvPowerFlow': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCTerminal: \n' + ACDCTerminal.__doc__ 

	def __init__(self, ConductingEquipment = None, RemoteInputSignal = "list", TopologicalNode = None, ConverterDCSides = "list", AuxiliaryEquipment = "list", ConnectivityNode = None, RegulatingControl = "list", phases = None, TransformerEnd = "list", TieFlow = "list", HasSecondMutualCoupling = "list", HasFirstMutualCoupling = "list", SvPowerFlow = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ConductingEquipment = ConductingEquipment
		self.RemoteInputSignal = RemoteInputSignal
		self.TopologicalNode = TopologicalNode
		self.ConverterDCSides = ConverterDCSides
		self.AuxiliaryEquipment = AuxiliaryEquipment
		self.ConnectivityNode = ConnectivityNode
		self.RegulatingControl = RegulatingControl
		self.phases = phases
		self.TransformerEnd = TransformerEnd
		self.TieFlow = TieFlow
		self.HasSecondMutualCoupling = HasSecondMutualCoupling
		self.HasFirstMutualCoupling = HasFirstMutualCoupling
		self.SvPowerFlow = SvPowerFlow
		
	def __str__(self):
		str = 'class=Terminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
