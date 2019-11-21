from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST7B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST7B model. This model is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter.  The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).  Reference: IEEE Standard 421.5-2005 Section 7.7.

	:kh: High-value gate feedback gain (K).  Typical Value 1. Default: 0.0
	:kia: Voltage regulator integral gain (K).  Typical Value = 1. Default: 0.0
	:kl: Low-value gate feedback gain (K).  Typical Value 1. Default: 0.0
	:kpa: Voltage regulator proportional gain (K).  Typical Value = 40. Default: 0.0
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: None
	:tb: Regulator lag time constant (T).  Typical Value 1. Default: 0.0
	:tc: Regulator lead time constant (T).  Typical Value 1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (T).  Typical Value 1. Default: 0.0
	:tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value 1. Default: 0.0
	:tia: Feedback time constant (T).  Typical Value = 3. Default: 0.0
	:uelin: UEL input selector (UELin). Typical Value = noUELinput. Default: None
	:vmax: Maximum voltage reference signal (V).  Typical Value = 1.1. Default: 0.0
	:vmin: Minimum voltage reference signal (V).  Typical Value = 0.9. Default: 0.0
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -4.5. Default: 0.0
		'''

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
						'uelin': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kh = 0.0, kia = 0.0, kl = 0.0, kpa = 0.0, oelin = None, tb = 0.0, tc = 0.0, tf = 0.0, tg = 0.0, tia = 0.0, uelin = None, vmax = 0.0, vmin = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
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
		self.uelin = uelin
		self.vmax = vmax
		self.vmin = vmin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST7B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
