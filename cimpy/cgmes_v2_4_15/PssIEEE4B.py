from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssIEEE4B(PowerSystemStabilizerDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-, intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.  Reference: IEEE 4B 421.5-2005 Section 8.4.

	:bwh1: Notch filter 1 (high-frequency band): Three dB bandwidth (B). Default: 
	:bwh2: Notch filter 2 (high-frequency band): Three dB bandwidth (B). Default: 
	:bwl1: Notch filter 1 (low-frequency band): Three dB bandwidth (B). Default: 
	:bwl2: Notch filter 2 (low-frequency band): Three dB bandwidth (B). Default: 
	:kh: High band gain (K).  Typical Value = 120. Default: 
	:kh1: High band differential filter gain (K).  Typical Value = 66. Default: 
	:kh11: High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:kh17: High band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:kh2: High band differential filter gain (K).  Typical Value = 66. Default: 
	:ki: Intermediate band gain (K).  Typical Value = 30. Default: 
	:ki1: Intermediate band differential filter gain (K).  Typical Value = 66. Default: 
	:ki11: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:ki17: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:ki2: Intermediate band differential filter gain (K).  Typical Value = 66. Default: 
	:kl: Low band gain (K).  Typical Value = 7.5. Default: 
	:kl1: Low band differential filter gain (K).  Typical Value = 66. Default: 
	:kl11: Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:kl17: Low band first lead-lag blocks coefficient (K).  Typical Value = 1. Default: 
	:kl2: Low band differential filter gain (K).  Typical Value = 66. Default: 
	:omeganh1: Notch filter 1 (high-frequency band): filter frequency (omega). Default: 
	:omeganh2: Notch filter 2 (high-frequency band): filter frequency (omega). Default: 
	:omeganl1: Notch filter 1 (low-frequency band): filter frequency (omega). Default: 
	:omeganl2: Notch filter 2 (low-frequency band): filter frequency (omega). Default: 
	:th1: High band time constant (T).  Typical Value = 0.01513. Default: 
	:th10: High band time constant (T).  Typical Value = 0. Default: 
	:th11: High band time constant (T).  Typical Value = 0. Default: 
	:th12: High band time constant (T).  Typical Value = 0. Default: 
	:th2: High band time constant (T).  Typical Value = 0.01816. Default: 
	:th3: High band time constant (T).  Typical Value = 0. Default: 
	:th4: High band time constant (T).  Typical Value = 0. Default: 
	:th5: High band time constant (T).  Typical Value = 0. Default: 
	:th6: High band time constant (T).  Typical Value = 0. Default: 
	:th7: High band time constant (T).  Typical Value = 0.01816. Default: 
	:th8: High band time constant (T).  Typical Value = 0.02179. Default: 
	:th9: High band time constant (T).  Typical Value = 0. Default: 
	:ti1: Intermediate band time constant (T).  Typical Value = 0.173. Default: 
	:ti10: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti11: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti12: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti2: Intermediate band time constant (T).  Typical Value = 0.2075. Default: 
	:ti3: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti4: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti5: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti6: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:ti7: Intermediate band time constant (T).  Typical Value = 0.2075. Default: 
	:ti8: Intermediate band time constant (T).  Typical Value = 0.2491. Default: 
	:ti9: Intermediate band time constant (T).  Typical Value = 0. Default: 
	:tl1: Low band time constant (T).  Typical Value = 1.73. Default: 
	:tl10: Low band time constant (T).  Typical Value = 0. Default: 
	:tl11: Low band time constant (T).  Typical Value = 0. Default: 
	:tl12: Low band time constant (T).  Typical Value = 0. Default: 
	:tl2: Low band time constant (T).  Typical Value = 2.075. Default: 
	:tl3: Low band time constant (T).  Typical Value = 0. Default: 
	:tl4: Low band time constant (T).  Typical Value = 0. Default: 
	:tl5: Low band time constant (T).  Typical Value = 0. Default: 
	:tl6: Low band time constant (T).  Typical Value = 0. Default: 
	:tl7: Low band time constant (T).  Typical Value = 2.075. Default: 
	:tl8: Low band time constant (T).  Typical Value = 2.491. Default: 
	:tl9: Low band time constant (T).  Typical Value = 0. Default: 
	:vhmax: High band output maximum limit (V).  Typical Value = 0.6. Default: 
	:vhmin: High band output minimum limit (V).  Typical Value = -0.6. Default: 
	:vimax: Intermediate band output maximum limit (V).  Typical Value = 0.6. Default: 
	:vimin: Intermediate band output minimum limit (V).  Typical Value = -0.6. Default: 
	:vlmax: Low band output maximum limit (V).  Typical Value = 0.075. Default: 
	:vlmin: Low band output minimum limit (V).  Typical Value = -0.075. Default: 
	:vstmax: PSS output maximum limit (V).  Typical Value = 0.15. Default: 
	:vstmin: PSS output minimum limit (V).  Typical Value = -0.15. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'bwh1': [cgmesProfile.DY.value, ],
						'bwh2': [cgmesProfile.DY.value, ],
						'bwl1': [cgmesProfile.DY.value, ],
						'bwl2': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kh1': [cgmesProfile.DY.value, ],
						'kh11': [cgmesProfile.DY.value, ],
						'kh17': [cgmesProfile.DY.value, ],
						'kh2': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'ki1': [cgmesProfile.DY.value, ],
						'ki11': [cgmesProfile.DY.value, ],
						'ki17': [cgmesProfile.DY.value, ],
						'ki2': [cgmesProfile.DY.value, ],
						'kl': [cgmesProfile.DY.value, ],
						'kl1': [cgmesProfile.DY.value, ],
						'kl11': [cgmesProfile.DY.value, ],
						'kl17': [cgmesProfile.DY.value, ],
						'kl2': [cgmesProfile.DY.value, ],
						'omeganh1': [cgmesProfile.DY.value, ],
						'omeganh2': [cgmesProfile.DY.value, ],
						'omeganl1': [cgmesProfile.DY.value, ],
						'omeganl2': [cgmesProfile.DY.value, ],
						'th1': [cgmesProfile.DY.value, ],
						'th10': [cgmesProfile.DY.value, ],
						'th11': [cgmesProfile.DY.value, ],
						'th12': [cgmesProfile.DY.value, ],
						'th2': [cgmesProfile.DY.value, ],
						'th3': [cgmesProfile.DY.value, ],
						'th4': [cgmesProfile.DY.value, ],
						'th5': [cgmesProfile.DY.value, ],
						'th6': [cgmesProfile.DY.value, ],
						'th7': [cgmesProfile.DY.value, ],
						'th8': [cgmesProfile.DY.value, ],
						'th9': [cgmesProfile.DY.value, ],
						'ti1': [cgmesProfile.DY.value, ],
						'ti10': [cgmesProfile.DY.value, ],
						'ti11': [cgmesProfile.DY.value, ],
						'ti12': [cgmesProfile.DY.value, ],
						'ti2': [cgmesProfile.DY.value, ],
						'ti3': [cgmesProfile.DY.value, ],
						'ti4': [cgmesProfile.DY.value, ],
						'ti5': [cgmesProfile.DY.value, ],
						'ti6': [cgmesProfile.DY.value, ],
						'ti7': [cgmesProfile.DY.value, ],
						'ti8': [cgmesProfile.DY.value, ],
						'ti9': [cgmesProfile.DY.value, ],
						'tl1': [cgmesProfile.DY.value, ],
						'tl10': [cgmesProfile.DY.value, ],
						'tl11': [cgmesProfile.DY.value, ],
						'tl12': [cgmesProfile.DY.value, ],
						'tl2': [cgmesProfile.DY.value, ],
						'tl3': [cgmesProfile.DY.value, ],
						'tl4': [cgmesProfile.DY.value, ],
						'tl5': [cgmesProfile.DY.value, ],
						'tl6': [cgmesProfile.DY.value, ],
						'tl7': [cgmesProfile.DY.value, ],
						'tl8': [cgmesProfile.DY.value, ],
						'tl9': [cgmesProfile.DY.value, ],
						'vhmax': [cgmesProfile.DY.value, ],
						'vhmin': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'vlmax': [cgmesProfile.DY.value, ],
						'vlmin': [cgmesProfile.DY.value, ],
						'vstmax': [cgmesProfile.DY.value, ],
						'vstmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, bwh1 = , bwh2 = , bwl1 = , bwl2 = , kh = , kh1 = , kh11 = , kh17 = , kh2 = , ki = , ki1 = , ki11 = , ki17 = , ki2 = , kl = , kl1 = , kl11 = , kl17 = , kl2 = , omeganh1 = , omeganh2 = , omeganl1 = , omeganl2 = , th1 = , th10 = , th11 = , th12 = , th2 = , th3 = , th4 = , th5 = , th6 = , th7 = , th8 = , th9 = , ti1 = , ti10 = , ti11 = , ti12 = , ti2 = , ti3 = , ti4 = , ti5 = , ti6 = , ti7 = , ti8 = , ti9 = , tl1 = , tl10 = , tl11 = , tl12 = , tl2 = , tl3 = , tl4 = , tl5 = , tl6 = , tl7 = , tl8 = , tl9 = , vhmax = , vhmin = , vimax = , vimin = , vlmax = , vlmin = , vstmax = , vstmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bwh1 = bwh1
		self.bwh2 = bwh2
		self.bwl1 = bwl1
		self.bwl2 = bwl2
		self.kh = kh
		self.kh1 = kh1
		self.kh11 = kh11
		self.kh17 = kh17
		self.kh2 = kh2
		self.ki = ki
		self.ki1 = ki1
		self.ki11 = ki11
		self.ki17 = ki17
		self.ki2 = ki2
		self.kl = kl
		self.kl1 = kl1
		self.kl11 = kl11
		self.kl17 = kl17
		self.kl2 = kl2
		self.omeganh1 = omeganh1
		self.omeganh2 = omeganh2
		self.omeganl1 = omeganl1
		self.omeganl2 = omeganl2
		self.th1 = th1
		self.th10 = th10
		self.th11 = th11
		self.th12 = th12
		self.th2 = th2
		self.th3 = th3
		self.th4 = th4
		self.th5 = th5
		self.th6 = th6
		self.th7 = th7
		self.th8 = th8
		self.th9 = th9
		self.ti1 = ti1
		self.ti10 = ti10
		self.ti11 = ti11
		self.ti12 = ti12
		self.ti2 = ti2
		self.ti3 = ti3
		self.ti4 = ti4
		self.ti5 = ti5
		self.ti6 = ti6
		self.ti7 = ti7
		self.ti8 = ti8
		self.ti9 = ti9
		self.tl1 = tl1
		self.tl10 = tl10
		self.tl11 = tl11
		self.tl12 = tl12
		self.tl2 = tl2
		self.tl3 = tl3
		self.tl4 = tl4
		self.tl5 = tl5
		self.tl6 = tl6
		self.tl7 = tl7
		self.tl8 = tl8
		self.tl9 = tl9
		self.vhmax = vhmax
		self.vhmin = vhmin
		self.vimax = vimax
		self.vimin = vimin
		self.vlmax = vlmax
		self.vlmin = vlmin
		self.vstmax = vstmax
		self.vstmin = vstmin
		
	def __str__(self):
		str = 'class=PssIEEE4B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
