from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssIEEE1A(PowerSystemStabilizerDynamics):
	'''
	IEEE 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input signal.  Reference: IEEE 1A 421.5-2005, 8.1.

	:inputSignalType: Type of input signal (rotorAngularFrequencyDeviation, generatorElectricalPower, or busFrequencyDeviation).  Typical value = rotorAngularFrequencyDeviation. Default: None
	:a1: PSS signal conditioning frequency filter constant (<i>A1</i>).  Typical value = 0,061. Default: 0.0
	:a2: PSS signal conditioning frequency filter constant (<i>A2</i>).  Typical value = 0,0017. Default: 0.0
	:t1: Lead/lag time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
	:t2: Lead/lag time constant (<i>T2</i>) (&gt;= 0).  Typical value = 0,03. Default: 0
	:t3: Lead/lag time constant (<i>T3</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
	:t4: Lead/lag time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0,03. Default: 0
	:t5: Washout time constant (<i>T5</i>) (&gt;= 0).  Typical value = 10. Default: 0
	:t6: Transducer time constant (<i>T6</i>) (&gt;= 0).  Typical value = 0,01. Default: 0
	:ks: Stabilizer gain (<i>Ks</i>).  Typical value = 5. Default: 0.0
	:vrmax: Maximum stabilizer output (<i>Vrmax</i>) (&gt; PssIEEE1A.vrmin).  Typical value = 0,05. Default: 0.0
	:vrmin: Minimum stabilizer output (<i>Vrmin</i>) (&lt; PssIEEE1A.vrmax).  Typical value = -0,05. Default: 0.0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'inputSignalType': [cgmesProfile.DY.value, ],
						'a1': [cgmesProfile.DY.value, ],
						'a2': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignalType = None, a1 = 0.0, a2 = 0.0, t1 = 0, t2 = 0, t3 = 0, t4 = 0, t5 = 0, t6 = 0, ks = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignalType = inputSignalType
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.ks = ks
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=PssIEEE1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
