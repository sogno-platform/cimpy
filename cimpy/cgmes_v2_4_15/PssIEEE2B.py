from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssIEEE2B(PowerSystemStabilizerDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.  Reference: IEEE 2B 421.5-2005 Section 8.2.

	:inputSignal1Type: Type of input signal #1.  Typical Value = rotorSpeed. Default: None
	:inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None
	:vsi1max: Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 0.0
	:vsi1min: Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 0.0
	:tw1: First washout on signal #1 (Tw1).  Typical Value = 2. Default: 0.0
	:tw2: Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 0.0
	:vsi2max: Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 0.0
	:vsi2min: Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 0.0
	:tw3: First washout on signal #2 (Tw3).  Typical Value = 2. Default: 0.0
	:tw4: Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 0.0
	:t1: Lead/lag time constant (T1).  Typical Value = 0.12. Default: 0.0
	:t2: Lead/lag time constant (T2).  Typical Value = 0.02. Default: 0.0
	:t3: Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0.0
	:t4: Lead/lag time constant (T4).  Typical Value = 0.02. Default: 0.0
	:t6: Time constant on signal #1 (T6).  Typical Value = 0. Default: 0.0
	:t7: Time constant on signal #2 (T7).  Typical Value = 2. Default: 0.0
	:t8: Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 0.0
	:t9: Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 0.0
	:t10: Lead/lag time constant (T10).  Typical Value = 0. Default: 0.0
	:t11: Lead/lag time constant (T11).  Typical Value = 0. Default: 0.0
	:ks1: Stabilizer gain (Ks1).  Typical Value = 12. Default: 0.0
	:ks2: Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 0.0
	:ks3: Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 0.0
	:n: Order of ramp tracking filter (N).  Typical Value = 1. Default: 0
	:m: Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 0
	:vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0
	:vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'inputSignal1Type': [cgmesProfile.DY.value, ],
						'inputSignal2Type': [cgmesProfile.DY.value, ],
						'vsi1max': [cgmesProfile.DY.value, ],
						'vsi1min': [cgmesProfile.DY.value, ],
						'tw1': [cgmesProfile.DY.value, ],
						'tw2': [cgmesProfile.DY.value, ],
						'vsi2max': [cgmesProfile.DY.value, ],
						'vsi2min': [cgmesProfile.DY.value, ],
						'tw3': [cgmesProfile.DY.value, ],
						'tw4': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						't7': [cgmesProfile.DY.value, ],
						't8': [cgmesProfile.DY.value, ],
						't9': [cgmesProfile.DY.value, ],
						't10': [cgmesProfile.DY.value, ],
						't11': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						'ks2': [cgmesProfile.DY.value, ],
						'ks3': [cgmesProfile.DY.value, ],
						'n': [cgmesProfile.DY.value, ],
						'm': [cgmesProfile.DY.value, ],
						'vstmax': [cgmesProfile.DY.value, ],
						'vstmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = None, inputSignal2Type = None, vsi1max = 0.0, vsi1min = 0.0, tw1 = 0.0, tw2 = 0.0, vsi2max = 0.0, vsi2min = 0.0, tw3 = 0.0, tw4 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, t9 = 0.0, t10 = 0.0, t11 = 0.0, ks1 = 0.0, ks2 = 0.0, ks3 = 0.0, n = 0, m = 0, vstmax = 0.0, vstmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.vsi1max = vsi1max
		self.vsi1min = vsi1min
		self.tw1 = tw1
		self.tw2 = tw2
		self.vsi2max = vsi2max
		self.vsi2min = vsi2min
		self.tw3 = tw3
		self.tw4 = tw4
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t9 = t9
		self.t10 = t10
		self.t11 = t11
		self.ks1 = ks1
		self.ks2 = ks2
		self.ks3 = ks3
		self.n = n
		self.m = m
		self.vstmax = vstmax
		self.vstmin = vstmin
		
	def __str__(self):
		str = 'class=PssIEEE2B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
