from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST7B(ExcitationSystemDynamics):
	'''
	Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP) inputs.

	:kh: High-value gate feedback gain (Kh).  Typical Value = 1. Default: 0.0
	:kia: Voltage regulator integral gain (Kia).  Typical Value = 1. Default: 0.0
	:kl: Low-value gate feedback gain (Kl).  Typical Value = 1. Default: 0.0
	:kpa: Voltage regulator proportional gain (Kpa).  Typical Value = 40. Default: 0.0
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: None
	:tb: Regulator lag time constant (Tb).  Typical Value = 1. Default: 0.0
	:tc: Regulator lead time constant (Tc).  Typical Value = 1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
	:tg: Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 1. Default: 0.0
	:tia: Feedback time constant (Tia).  Typical Value = 3. Default: 0.0
	:ts: Rectifier firing time constant (Ts).  Typical Value = 0. Default: 0.0
	:uelin: UEL input selector (UELin). Typical Value = noUELinput. Default: None
	:vmax: Maximum voltage reference signal (Vmax).  Typical Value = 1.1. Default: 0.0
	:vmin: Minimum voltage reference signal (Vmin).  Typical Value = 0.9. Default: 0.0
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.5. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kia': [cgmesProfile.DY.value, ],
						'kl': [cgmesProfile.DY.value, ],
						'kpa': [cgmesProfile.DY.value, ],
						'oelin': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'tia': [cgmesProfile.DY.value, ],
						'ts': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kh = 0.0, kia = 0.0, kl = 0.0, kpa = 0.0, oelin = None, tb = 0.0, tc = 0.0, tf = 0.0, tg = 0.0, tia = 0.0, ts = 0.0, uelin = None, vmax = 0.0, vmin = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kh = kh
		self.kia = kia
		self.kl = kl
		self.kpa = kpa
		self.oelin = oelin
		self.tb = tb
		self.tc = tc
		self.tf = tf
		self.tg = tg
		self.tia = tia
		self.ts = ts
		self.uelin = uelin
		self.vmax = vmax
		self.vmin = vmin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcST7B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
