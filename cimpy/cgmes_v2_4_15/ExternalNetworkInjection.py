from cimpy.cgmes_v2_4_15_flat.RegulatingCondEq import RegulatingCondEq


class ExternalNetworkInjection(RegulatingCondEq):
	'''
	This class represents external network and it is used for IEC 60909 calculations.

	:governorSCD: Power Frequency Bias. This is the change in power injection divided by the change in frequency and negated.  A positive value of the power frequency bias provides additional power injection upon a drop in frequency. Default: 0.0
	:maxP: Maximum active power of the injection. Default: 0.0
	:maxQ: Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 0.0
	:minP: Minimum active power of the injection. Default: 0.0
	:minQ: Not for short circuit modelling; It is used for modelling of infeed for load flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used Default: 0.0
	:ikSecond: Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik"). Default: False
	:maxInitialSymShCCurrent: Maximum initial symmetrical short-circuit currents (Ik" max) in A (Ik" = Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:maxR0ToX0Ratio: Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:maxR1ToX1Ratio: Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:maxZ0ToZ1Ratio: Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:minInitialSymShCCurrent: Minimum initial symmetrical short-circuit currents (Ik" min) in A (Ik" = Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:minR0ToX0Ratio: Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik"). Used for short circuit data exchange according to IEC 6090 Default: 0.0
	:minR1ToX1Ratio: Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:minZ0ToZ1Ratio: Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909 Default: 0.0
	:voltageFactor: Voltage factor in pu, which was used to calculate short-circuit current Ik" and power Sk". Default: 0.0
	:referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0
	:p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
	:q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'governorSCD': [cgmesProfile.EQ.value, ],
						'maxP': [cgmesProfile.EQ.value, ],
						'maxQ': [cgmesProfile.EQ.value, ],
						'minP': [cgmesProfile.EQ.value, ],
						'minQ': [cgmesProfile.EQ.value, ],
						'ikSecond': [cgmesProfile.EQ.value, ],
						'maxInitialSymShCCurrent': [cgmesProfile.EQ.value, ],
						'maxR0ToX0Ratio': [cgmesProfile.EQ.value, ],
						'maxR1ToX1Ratio': [cgmesProfile.EQ.value, ],
						'maxZ0ToZ1Ratio': [cgmesProfile.EQ.value, ],
						'minInitialSymShCCurrent': [cgmesProfile.EQ.value, ],
						'minR0ToX0Ratio': [cgmesProfile.EQ.value, ],
						'minR1ToX1Ratio': [cgmesProfile.EQ.value, ],
						'minZ0ToZ1Ratio': [cgmesProfile.EQ.value, ],
						'voltageFactor': [cgmesProfile.EQ.value, ],
						'referencePriority': [cgmesProfile.SSH.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, governorSCD = 0.0, maxP = 0.0, maxQ = 0.0, minP = 0.0, minQ = 0.0, ikSecond = False, maxInitialSymShCCurrent = 0.0, maxR0ToX0Ratio = 0.0, maxR1ToX1Ratio = 0.0, maxZ0ToZ1Ratio = 0.0, minInitialSymShCCurrent = 0.0, minR0ToX0Ratio = 0.0, minR1ToX1Ratio = 0.0, minZ0ToZ1Ratio = 0.0, voltageFactor = 0.0, referencePriority = 0, p = 0.0, q = 0.0,  *args, **kw_args):
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
