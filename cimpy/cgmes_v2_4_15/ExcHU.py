from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcHU(ExcitationSystemDynamics):
	'''
	Hungarian Excitation System Model, with built-in voltage transducer.

	:tr: Filter time constant (Tr). If a voltage compensator is used in conjunction with this excitation system model, Tr should be set to 0.  Typical Value = 0.01. Default: 0.0
	:te: Major loop PI tag integration time constant (Te).  Typical Value = 0.154. Default: 0.0
	:imin: Major loop PI tag output signal lower limit (Imin).  Typical Value = 0.1. Default: 0.0
	:imax: Major loop PI tag output signal upper limit (Imax).  Typical Value = 2.19. Default: 0.0
	:ae: Major loop PI tag gain factor (Ae).  Typical Value = 3. Default: 0.0
	:emin: Field voltage control signal lower limit on AVR base (Emin).  Typical Value = -0.866. Default: 0.0
	:emax: Field voltage control signal upper limit on AVR base (Emax).  Typical Value = 0.996. Default: 0.0
	:ki: Current base conversion constant (Ki).  Typical Value = 0.21428. Default: 0.0
	:ai: Minor loop PI tag gain factor (Ai).  Typical Value = 22. Default: 0.0
	:ti: Minor loop PI control tag integration time constant (Ti).  Typical Value = 0.01333. Default: 0.0
	:atr: AVR constant (Atr).  Typical Value = 2.19. Default: 0.0
	:ke: Voltage base conversion constant (Ke).  Typical Value = 4.666. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tr = 0.0, te = 0.0, imin = 0.0, imax = 0.0, ae = 0.0, emin = 0.0, emax = 0.0, ki = 0.0, ai = 0.0, ti = 0.0, atr = 0.0, ke = 0.0,  *args, **kw_args):
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
