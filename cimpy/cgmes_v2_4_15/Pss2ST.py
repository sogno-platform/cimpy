from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss2ST(PowerSystemStabilizerDynamics):
	'''
	PTI Microprocessor-Based Stabilizer type 1.

	:inputSignal1Type: Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation. Default: None
	:inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None
	:k1: Gain (K1). Default: 0.0
	:k2: Gain (K2). Default: 0.0
	:t1: Time constant (T1). Default: 0.0
	:t2: Time constant (T2). Default: 0.0
	:t3: Time constant (T3). Default: 0.0
	:t4: Time constant (T4). Default: 0.0
	:t5: Time constant (T5). Default: 0.0
	:t6: Time constant (T6). Default: 0.0
	:t7: Time constant (T7). Default: 0.0
	:t8: Time constant (T8). Default: 0.0
	:t9: Time constant (T9). Default: 0.0
	:t10: Time constant (T10). Default: 0.0
	:lsmax: Limiter (Lsmax). Default: 0.0
	:lsmin: Limiter (Lsmin). Default: 0.0
	:vcu: Cutoff limiter (Vcu). Default: 0.0
	:vcl: Cutoff limiter (Vcl). Default: 0.0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'inputSignal1Type': [cgmesProfile.DY.value, ],
						'inputSignal2Type': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						't7': [cgmesProfile.DY.value, ],
						't8': [cgmesProfile.DY.value, ],
						't9': [cgmesProfile.DY.value, ],
						't10': [cgmesProfile.DY.value, ],
						'lsmax': [cgmesProfile.DY.value, ],
						'lsmin': [cgmesProfile.DY.value, ],
						'vcu': [cgmesProfile.DY.value, ],
						'vcl': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = None, inputSignal2Type = None, k1 = 0.0, k2 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, t9 = 0.0, t10 = 0.0, lsmax = 0.0, lsmin = 0.0, vcu = 0.0, vcl = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.k1 = k1
		self.k2 = k2
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t9 = t9
		self.t10 = t10
		self.lsmax = lsmax
		self.lsmin = lsmin
		self.vcu = vcu
		self.vcl = vcl
		
	def __str__(self):
		str = 'class=Pss2ST\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
