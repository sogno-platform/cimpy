from cimpy.output.EquivalentEquipment import EquivalentEquipment


class EquivalentInjection(EquivalentEquipment):
	'''
	This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.

	:ReactiveCapabilityCurve: The equivalent injection using this reactive capability curve. Default: 
	:maxP: Maximum active power of the injection. Default: 
	:maxQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 
	:minP: Minimum active power of the injection. Default: 
	:minQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 
	:regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. Default: 
	:r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 
	:regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. Default: 
	:regulationTarget: The target voltage for voltage regulation. Default: 
	:p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
	:q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
		'''

	cgmesProfile = EquivalentEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'ReactiveCapabilityCurve': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxP': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxQ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minP': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minQ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'regulationCapability': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'regulationStatus': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'regulationTarget': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EquivalentEquipment: \n' + EquivalentEquipment.__doc__ 

	def __init__(self, ReactiveCapabilityCurve = , maxP = , maxQ = , minP = , minQ = , regulationCapability = , r = , r0 = , r2 = , x = , x0 = , x2 = , regulationStatus = , regulationTarget = , p = , q = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ReactiveCapabilityCurve = ReactiveCapabilityCurve
		self.maxP = maxP
		self.maxQ = maxQ
		self.minP = minP
		self.minQ = minQ
		self.regulationCapability = regulationCapability
		self.r = r
		self.r0 = r0
		self.r2 = r2
		self.x = x
		self.x0 = x0
		self.x2 = x2
		self.regulationStatus = regulationStatus
		self.regulationTarget = regulationTarget
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=EquivalentInjection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
