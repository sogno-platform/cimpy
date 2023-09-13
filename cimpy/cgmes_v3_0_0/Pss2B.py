from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss2B(PowerSystemStabilizerDynamics):
	'''
	Modified IEEE PSS2B.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).

	:vsi1max: Input signal #1 maximum limit (<i>Vsi1max</i>) (&gt; Pss2B.vsi1min).  Typical value = 2. Default: 0.0
	:vsi1min: Input signal #1 minimum limit (<i>Vsi1min</i>) (&lt; Pss2B.vsi1max).  Typical value = -2. Default: 0.0
	:tw1: First washout on signal #1 (<i>T</i><i><sub>w1</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:tw2: Second washout on signal #1 (<i>T</i><i><sub>w2</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:vsi2max: Input signal #2 maximum limit (<i>Vsi2max</i>) (&gt; Pss2B.vsi2min).  Typical value = 2. Default: 0.0
	:vsi2min: Input signal #2 minimum limit (<i>Vsi2min</i>) (&lt; Pss2B.vsi2max).  Typical value = -2. Default: 0.0
	:tw3: First washout on signal #2 (<i>T</i><i><sub>w3</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:tw4: Second washout on signal #2 (<i>T</i><i><sub>w4</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t1: Lead/lag time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 0,12. Default: 0
	:t2: Lead/lag time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:t3: Lead/lag time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 0,3. Default: 0
	:t4: Lead/lag time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:t6: Time constant on signal #1 (<i>T</i><i><sub>6</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t7: Time constant on signal #2 (<i>T</i><i><sub>7</sub></i>) (&gt;= 0).  Typical value = 2. Default: 0
	:t8: Lead of ramp tracking filter (<i>T</i><i><sub>8</sub></i>) (&gt;= 0).  Typical value = 0,2. Default: 0
	:t9: Lag of ramp tracking filter (<i>T</i><i><sub>9</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:t10: Lead/lag time constant (<i>T</i><i><sub>10</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t11: Lead/lag time constant (<i>T</i><i><sub>11</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ks1: Stabilizer gain (<i>Ks1</i>).  Typical value = 12. Default: 0.0
	:ks2: Gain on signal #2 (<i>Ks2</i>).  Typical value = 0,2. Default: 0.0
	:ks3: Gain on signal #2 input before ramp-tracking filter (<i>Ks3</i>).  Typical value = 1. Default: 0.0
	:ks4: Gain on signal #2 input after ramp-tracking filter (<i>Ks4</i>).  Typical value = 1. Default: 0.0
	:n: Order of ramp tracking filter (<i>n</i>).  Typical value = 1. Default: 0
	:m: Denominator order of ramp tracking filter (<i>m</i>).  Typical value = 5. Default: 0
	:vstmax: Stabilizer output maximum limit (<i>Vstmax</i>) (&gt; Pss2B.vstmin).  Typical value = 0,1. Default: 0.0
	:vstmin: Stabilizer output minimum limit (<i>Vstmin</i>) (&lt; Pss2B.vstmax).  Typical value = -0,1. Default: 0.0
	:a: Numerator constant (<i>a</i>).  Typical value = 1. Default: 0.0
	:ta: Lead constant (<i>T</i><i><sub>a</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tb: Lag time constant (<i>T</i><i><sub>b</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
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
						'ks4': [cgmesProfile.DY.value, ],
						'n': [cgmesProfile.DY.value, ],
						'm': [cgmesProfile.DY.value, ],
						'vstmax': [cgmesProfile.DY.value, ],
						'vstmin': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, vsi1max = 0.0, vsi1min = 0.0, tw1 = 0, tw2 = 0, vsi2max = 0.0, vsi2min = 0.0, tw3 = 0, tw4 = 0, t1 = 0, t2 = 0, t3 = 0, t4 = 0, t6 = 0, t7 = 0, t8 = 0, t9 = 0, t10 = 0, t11 = 0, ks1 = 0.0, ks2 = 0.0, ks3 = 0.0, ks4 = 0.0, n = 0, m = 0, vstmax = 0.0, vstmin = 0.0, a = 0.0, ta = 0, tb = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
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
		self.ks4 = ks4
		self.n = n
		self.m = m
		self.vstmax = vstmax
		self.vstmin = vstmin
		self.a = a
		self.ta = ta
		self.tb = tb
		
	def __str__(self):
		str = 'class=Pss2B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
