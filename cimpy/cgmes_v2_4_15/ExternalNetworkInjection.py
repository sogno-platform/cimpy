from cimpy.output.RegulatingCondEq import RegulatingCondEq


class ExternalNetworkInjection(RegulatingCondEq):
	'''
	This class represents external network and it is used for IEC 60909 calculations.

	:governorSCD: Power Frequency Bias. This is the change in power injection divided by the change in frequency and negated.  A positive value of the power frequency bias provides additional power injection upon a drop in frequency. Default: 
	:maxP: Maximum active power of the injection. Default: 
	:maxQ: Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 
	:minP: Minimum active power of the injection. Default: 
	:minQ: Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 
	:ikSecond: Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik`). Default: 
	:maxInitialSymShCCurrent: Maximum initial symmetrical short-circuit currents (Ik` max) in A (Ik` = Sk`/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 
	:maxR0ToX0Ratio: Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909 Default: 
	:maxR1ToX1Ratio: Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909 Default: 
	:maxZ0ToZ1Ratio: Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909 Default: 
	:minInitialSymShCCurrent: Minimum initial symmetrical short-circuit currents (Ik` min) in A (Ik` = Sk`/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 
	:minR0ToX0Ratio: Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik`). Used for short circuit data exchange according to IEC 6090 Default: 
	:minR1ToX1Ratio: Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909 Default: 
	:minZ0ToZ1Ratio: Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909 Default: 
	:voltageFactor: Voltage factor in pu, which was used to calculate short-circuit current Ik` and power Sk`. Default: 
	:referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 
	:p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
	:q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
		'''

	cgmesProfile = RegulatingCondEq.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'governorSCD': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxP': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxQ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minP': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minQ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ikSecond': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxInitialSymShCCurrent': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxR0ToX0Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxR1ToX1Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxZ0ToZ1Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minInitialSymShCCurrent': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minR0ToX0Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minR1ToX1Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minZ0ToZ1Ratio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'voltageFactor': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'referencePriority': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, governorSCD = , maxP = , maxQ = , minP = , minQ = , ikSecond = , maxInitialSymShCCurrent = , maxR0ToX0Ratio = , maxR1ToX1Ratio = , maxZ0ToZ1Ratio = , minInitialSymShCCurrent = , minR0ToX0Ratio = , minR1ToX1Ratio = , minZ0ToZ1Ratio = , voltageFactor = , referencePriority = , p = , q = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.governorSCD = governorSCD
		self.maxP = maxP
		self.maxQ = maxQ
		self.minP = minP
		self.minQ = minQ
		self.ikSecond = ikSecond
		self.maxInitialSymShCCurrent = maxInitialSymShCCurrent
		self.maxR0ToX0Ratio = maxR0ToX0Ratio
		self.maxR1ToX1Ratio = maxR1ToX1Ratio
		self.maxZ0ToZ1Ratio = maxZ0ToZ1Ratio
		self.minInitialSymShCCurrent = minInitialSymShCCurrent
		self.minR0ToX0Ratio = minR0ToX0Ratio
		self.minR1ToX1Ratio = minR1ToX1Ratio
		self.minZ0ToZ1Ratio = minZ0ToZ1Ratio
		self.voltageFactor = voltageFactor
		self.referencePriority = referencePriority
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=ExternalNetworkInjection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
