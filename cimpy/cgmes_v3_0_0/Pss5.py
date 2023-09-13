from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss5(PowerSystemStabilizerDynamics):
	'''
	Detailed Italian PSS.

	:kpe: Electric power input gain (<i>K</i><i><sub>PE</sub></i>).  Typical value = 0,3. Default: 0.0
	:kf: Frequency/shaft speed input gain (<i>K</i><i><sub>F</sub></i>).  Typical value = 5. Default: 0.0
	:isfreq: Selector for frequency/shaft speed input (<i>isFreq</i>). true = speed (same meaning as InputSignaKind.rotorSpeed) false = frequency (same meaning as InputSignalKind.busFrequency). Typical value = true (same meaning as InputSignalKind.rotorSpeed). Default: False
	:kpss: PSS gain (<i>K</i><i><sub>PSS</sub></i>).  Typical value = 1. Default: 0.0
	:ctw2: Selector for second washout enabling (<i>C</i><i><sub>TW2</sub></i>). true = second washout filter is bypassed false = second washout filter in use. Typical value = true. Default: False
	:tw1: First washout (<i>T</i><i><sub>W1</sub></i>) (&gt;= 0).  Typical value = 3,5. Default: 0
	:tw2: Second washout (<i>T</i><i><sub>W2</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tl1: Lead/lag time constant (<i>T</i><i><sub>L1</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tl2: Lead/lag time constant (<i>T</i><i><sub>L2</sub></i>) (&gt;= 0).  If = 0, both blocks are bypassed.  Typical value = 0. Default: 0
	:tl3: Lead/lag time constant (<i>T</i><i><sub>L3</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tl4: Lead/lag time constant (T<sub>L4</sub>) (&gt;= 0).  If = 0, both blocks are bypassed.  Typical value = 0. Default: 0
	:vsmn: Stabilizer output maximum limit (<i>V</i><i><sub>SMN</sub></i>).  Typical value = -0,1. Default: 0.0
	:vsmx: Stabilizer output minimum limit (<i>V</i><i><sub>SMX</sub></i>).  Typical value = 0,1. Default: 0.0
	:tpe: Electric power filter time constant (<i>T</i><i><sub>PE</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
	:pmin: Minimum power PSS enabling (<i>Pmin</i>).  Typical value = 0,25. Default: 0.0
	:deadband: Stabilizer output deadband (<i>DEADBAND</i>).  Typical value = 0. Default: 0.0
	:vadat: <font color=`#0f0f0f`>Signal selector (<i>V</i><i><sub>adAtt</sub></i>).</font> <font color=`#0f0f0f`>true = closed (generator power is greater than <i>Pmin</i>)</font> <font color=`#0f0f0f`>false = open (<i>Pe</i> is smaller than <i>Pmin</i>).</font> <font color=`#0f0f0f`>Typical value = true.</font> Default: False
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpe': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'isfreq': [cgmesProfile.DY.value, ],
						'kpss': [cgmesProfile.DY.value, ],
						'ctw2': [cgmesProfile.DY.value, ],
						'tw1': [cgmesProfile.DY.value, ],
						'tw2': [cgmesProfile.DY.value, ],
						'tl1': [cgmesProfile.DY.value, ],
						'tl2': [cgmesProfile.DY.value, ],
						'tl3': [cgmesProfile.DY.value, ],
						'tl4': [cgmesProfile.DY.value, ],
						'vsmn': [cgmesProfile.DY.value, ],
						'vsmx': [cgmesProfile.DY.value, ],
						'tpe': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'deadband': [cgmesProfile.DY.value, ],
						'vadat': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, kpe = 0.0, kf = 0.0, isfreq = False, kpss = 0.0, ctw2 = False, tw1 = 0, tw2 = 0, tl1 = 0, tl2 = 0, tl3 = 0, tl4 = 0, vsmn = 0.0, vsmx = 0.0, tpe = 0, pmin = 0.0, deadband = 0.0, vadat = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpe = kpe
		self.kf = kf
		self.isfreq = isfreq
		self.kpss = kpss
		self.ctw2 = ctw2
		self.tw1 = tw1
		self.tw2 = tw2
		self.tl1 = tl1
		self.tl2 = tl2
		self.tl3 = tl3
		self.tl4 = tl4
		self.vsmn = vsmn
		self.vsmx = vsmx
		self.tpe = tpe
		self.pmin = pmin
		self.deadband = deadband
		self.vadat = vadat
		
	def __str__(self):
		str = 'class=Pss5\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
