from cimpy.output.ACDCTerminal import ACDCTerminal


class Terminal(ACDCTerminal):
	'''
	An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

	:ConverterDCSides: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer. Default: 
	:ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: 
	:phases: Represents the normal network phasing condition. If the attribute is missing three phases (ABC or ABCN) shall be assumed. Default: 
	:RegulatingControl: The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node (bus in bus-branch model) or a connectivity node (detailed switch model).  Sometimes it is useful to model regulation at a terminal of a bus bar object since the bus bar can be present in both a bus-branch model or a model with switch detail. Default: 
	:TieFlow: The control area tie flows to which this terminal associates. Default: 
	:TransformerEnd: All transformer ends connected at this terminal. Default: 
	:ConnectivityNode: Terminals interconnected with zero impedance at a this connectivity node. Default: 
	:HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch. Default: 
	:HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch. Default: 
	:SvPowerFlow: The power flow state variable associated with the terminal. Default: 
	:RemoteInputSignal: Input signal coming from this terminal. Default: 
	:TopologicalNode: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: 
		'''

	cgmesProfile = ACDCTerminal.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'ConverterDCSides': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ConductingEquipment': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'phases': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'RegulatingControl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'TieFlow': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'TransformerEnd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ConnectivityNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HasFirstMutualCoupling': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HasSecondMutualCoupling': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'SvPowerFlow': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'RemoteInputSignal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'TopologicalNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCTerminal: \n' + ACDCTerminal.__doc__ 

	def __init__(self, ConverterDCSides = , ConductingEquipment = , phases = , RegulatingControl = , TieFlow = , TransformerEnd = , ConnectivityNode = , HasFirstMutualCoupling = , HasSecondMutualCoupling = , SvPowerFlow = , RemoteInputSignal = , TopologicalNode = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ConverterDCSides = ConverterDCSides
		self.ConductingEquipment = ConductingEquipment
		self.phases = phases
		self.RegulatingControl = RegulatingControl
		self.TieFlow = TieFlow
		self.TransformerEnd = TransformerEnd
		self.ConnectivityNode = ConnectivityNode
		self.HasFirstMutualCoupling = HasFirstMutualCoupling
		self.HasSecondMutualCoupling = HasSecondMutualCoupling
		self.SvPowerFlow = SvPowerFlow
		self.RemoteInputSignal = RemoteInputSignal
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=Terminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
