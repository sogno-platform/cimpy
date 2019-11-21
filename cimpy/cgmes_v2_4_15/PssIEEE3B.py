from cimpy.cgmes_v2_4_15_flat.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssIEEE3B(PowerSystemStabilizerDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.  Reference: IEEE 3B 421.5-2005 Section 8.3.

	:inputSignal1Type: Type of input signal #1.  Typical Value = generatorElectricalPower. Default: None
	:inputSignal2Type: Type of input signal #2.  Typical Value = rotorSpeed. Default: None
	:t1: Transducer time constant (T1).  Typical Value = 0.012. Default: 0.0
	:t2: Transducer time constant (T2).  Typical Value = 0.012. Default: 0.0
	:tw1: Washout time constant (Tw1).  Typical Value = 0.3. Default: 0.0
	:tw2: Washout time constant (Tw2).  Typical Value = 0.3. Default: 0.0
	:tw3: Washout time constant (Tw3).  Typical Value = 0.6. Default: 0.0
	:ks1: Gain on signal # 1 (Ks1).  Typical Value = -0.602. Default: 0.0
	:ks2: Gain on signal # 2 (Ks2).  Typical Value = 30.12. Default: 0.0
	:a1: Notch filter parameter (A1).  Typical Value = 0.359. Default: 0.0
	:a2: Notch filter parameter (A2).  Typical Value = 0.586. Default: 0.0
	:a3: Notch filter parameter (A3).  Typical Value = 0.429. Default: 0.0
	:a4: Notch filter parameter (A4).  Typical Value = 0.564. Default: 0.0
	:a5: Notch filter parameter (A5).  Typical Value = 0.001. Default: 0.0
	:a6: Notch filter parameter (A6).  Typical Value = 0. Default: 0.0
	:a7: Notch filter parameter (A7).  Typical Value = 0.031. Default: 0.0
	:a8: Notch filter parameter (A8).  Typical Value = 0. Default: 0.0
	:vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0
	:vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'inputSignal1Type': [cgmesProfile.DY.value, ],
						'inputSignal2Type': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'tw1': [cgmesProfile.DY.value, ],
						'tw2': [cgmesProfile.DY.value, ],
						'tw3': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						'ks2': [cgmesProfile.DY.value, ],
						'a1': [cgmesProfile.DY.value, ],
						'a2': [cgmesProfile.DY.value, ],
						'a3': [cgmesProfile.DY.value, ],
						'a4': [cgmesProfile.DY.value, ],
						'a5': [cgmesProfile.DY.value, ],
						'a6': [cgmesProfile.DY.value, ],
						'a7': [cgmesProfile.DY.value, ],
						'a8': [cgmesProfile.DY.value, ],
						'vstmax': [cgmesProfile.DY.value, ],
						'vstmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = None, inputSignal2Type = None, t1 = 0.0, t2 = 0.0, tw1 = 0.0, tw2 = 0.0, tw3 = 0.0, ks1 = 0.0, ks2 = 0.0, a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, a6 = 0.0, a7 = 0.0, a8 = 0.0, vstmax = 0.0, vstmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.t1 = t1
		self.t2 = t2
		self.tw1 = tw1
		self.tw2 = tw2
		self.tw3 = tw3
		self.ks1 = ks1
		self.ks2 = ks2
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		self.a6 = a6
		self.a7 = a7
		self.a8 = a8
		self.vstmax = vstmax
		self.vstmin = vstmin
		
	def __str__(self):
		str = 'class=PssIEEE3B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
