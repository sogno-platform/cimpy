from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcHU(ExcitationSystemDynamics):
	'''
	Hungarian Excitation System Model, with built-in voltage transducer.

	:tr: Filter time constant (Tr). If a voltage compensator is used in conjunction with this excitation system model, Tr should be set to 0.  Typical Value = 0.01. Default: 
	:te: Major loop PI tag integration time constant (Te).  Typical Value = 0.154. Default: 
	:imin: Major loop PI tag output signal lower limit (Imin).  Typical Value = 0.1. Default: 
	:imax: Major loop PI tag output signal upper limit (Imax).  Typical Value = 2.19. Default: 
	:ae: Major loop PI tag gain factor (Ae).  Typical Value = 3. Default: 
	:emin: Field voltage control signal lower limit on AVR base (Emin).  Typical Value = -0.866. Default: 
	:emax: Field voltage control signal upper limit on AVR base (Emax).  Typical Value = 0.996. Default: 
	:ki: Current base conversion constant (Ki).  Typical Value = 0.21428. Default: 
	:ai: Minor loop PI tag gain factor (Ai).  Typical Value = 22. Default: 
	:ti: Minor loop PI control tag integration time constant (Ti).  Typical Value = 0.01333. Default: 
	:atr: AVR constant (Atr).  Typical Value = 2.19. Default: 
	:ke: Voltage base conversion constant (Ke).  Typical Value = 4.666. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'imin': [cgmesProfile.DY.value, ],
						'imax': [cgmesProfile.DY.value, ],
						'ae': [cgmesProfile.DY.value, ],
						'emin': [cgmesProfile.DY.value, ],
						'emax': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'ai': [cgmesProfile.DY.value, ],
						'ti': [cgmesProfile.DY.value, ],
						'atr': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tr = , te = , imin = , imax = , ae = , emin = , emax = , ki = , ai = , ti = , atr = , ke = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tr = tr
		self.te = te
		self.imin = imin
		self.imax = imax
		self.ae = ae
		self.emin = emin
		self.emax = emax
		self.ki = ki
		self.ai = ai
		self.ti = ti
		self.atr = atr
		self.ke = ke
		
	def __str__(self):
		str = 'class=ExcHU\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
