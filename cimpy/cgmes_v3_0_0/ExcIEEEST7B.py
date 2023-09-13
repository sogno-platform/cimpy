from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST7B(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type ST7B model. This model is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows the introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter.  The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from PSS) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2). Reference: IEEE 421.5-2005, 7.7.

	:kh: High-value gate feedback gain (<i>K</i><i><sub>H</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kia: Voltage regulator integral gain (<i>K</i><i><sub>IA</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kl: Low-value gate feedback gain (<i>K</i><i><sub>L</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kpa: Voltage regulator proportional gain (<i>K</i><i><sub>PA</sub></i>) (&gt; 0).  Typical value = 40. Default: 0.0
	:oelin: OEL input selector (<i>OELin</i>).  Typical value = noOELinput. Default: None
	:tb: Regulator lag time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tc: Regulator lead time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tg: Feedback time constant of inner loop field voltage regulator (<i>T</i><i><sub>G</sub></i>) (&gt;= 0). Typical value = 1. Default: 0
	:tia: Feedback time constant (<i>T</i><i><sub>IA</sub></i>) (&gt;= 0).  Typical value = 3. Default: 0
	:uelin: UEL input selector (<i>UELin</i>). Typical value = noUELinput. Default: None
	:vmax: Maximum voltage reference signal (<i>V</i><i><sub>MAX</sub></i>) (&gt; 0 and &gt; ExcIEEEST7B.vmin).  Typical value = 1,1. Default: 0.0
	:vmin: Minimum voltage reference signal (<i>V</i><i><sub>MIN</sub></i>) (&gt; 0 and &lt; ExcIEEEST7B.vmax).  Typical value = 0,9. Default: 0.0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -4,5. Default: 0.0
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
						'uelin': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kh = 0.0, kia = 0.0, kl = 0.0, kpa = 0.0, oelin = None, tb = 0, tc = 0, tf = 0, tg = 0, tia = 0, uelin = None, vmax = 0.0, vmin = 0.0, vrmax = 0.0, vrmin = 0.0,  *args, **kw_args):
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
