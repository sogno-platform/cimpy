from cimpy.cgmes_v2_4_15.EquivalentEquipment import EquivalentEquipment


class EquivalentInjection(EquivalentEquipment):
	'''
	This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.

	:ReactiveCapabilityCurve: The equivalent injection using this reactive capability curve. Default: None
	:maxP: Maximum active power of the injection. Default: 0.0
	:maxQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0
	:minP: Minimum active power of the injection. Default: 0.0
	:minQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0
	:regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. Default: False
	:r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
	:regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. Default: False
	:regulationTarget: The target voltage for voltage regulation. Default: 0.0
	:p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
	:q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
		'''

	cgmesProfile = EquivalentEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'ReactiveCapabilityCurve': [cgmesProfile.EQ.value, ],
						'maxP': [cgmesProfile.EQ.value, ],
						'maxQ': [cgmesProfile.EQ.value, ],
						'minP': [cgmesProfile.EQ.value, ],
						'minQ': [cgmesProfile.EQ.value, ],
						'regulationCapability': [cgmesProfile.EQ.value, ],
						'r': [cgmesProfile.EQ.value, ],
						'r0': [cgmesProfile.EQ.value, ],
						'r2': [cgmesProfile.EQ.value, ],
						'x': [cgmesProfile.EQ.value, ],
						'x0': [cgmesProfile.EQ.value, ],
						'x2': [cgmesProfile.EQ.value, ],
						'regulationStatus': [cgmesProfile.SSH.value, ],
						'regulationTarget': [cgmesProfile.SSH.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EquivalentEquipment: \n' + EquivalentEquipment.__doc__ 

	def __init__(self, ReactiveCapabilityCurve = None, maxP = 0.0, maxQ = 0.0, minP = 0.0, minQ = 0.0, regulationCapability = False, r = 0.0, r0 = 0.0, r2 = 0.0, x = 0.0, x0 = 0.0, x2 = 0.0, regulationStatus = False, regulationTarget = 0.0, p = 0.0, q = 0.0,  *args, **kw_args):
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
