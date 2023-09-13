from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST6B(ExcitationSystemDynamics):
	'''
	Modified IEEE ST6B static excitation system with PID controller and optional inner feedback loop.

	:ilr: Exciter output current limit reference (<i>Ilr</i>) (&gt; 0).  Typical value = 4,164. Default: 0.0
	:k1: Selector (<i>K1</i>). true = feedback is from <i>Ifd</i> false = feedback is not from <i>Ifd</i>. Typical value = true. Default: False
	:kcl: Exciter output current limit adjustment (<i>Kcl</i>) (&gt; 0).  Typical value = 1,0577. Default: 0.0
	:kff: Pre-control gain constant of the inner loop field regulator (<i>Kff</i>).  Typical value = 1. Default: 0.0
	:kg: Feedback gain constant of the inner loop field regulator (<i>Kg</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kia: Voltage regulator integral gain (<i>Kia</i>) (&gt; 0).  Typical value = 45,094. Default: 0.0
	:klr: Exciter output current limit adjustment (<i>Kcl</i>) (&gt; 0).  Typical value = 17,33. Default: 0.0
	:km: Forward gain constant of the inner loop field regulator (<i>Km</i>).  Typical value = 1. Default: 0.0
	:kpa: Voltage regulator proportional gain (<i>Kpa</i>) (&gt; 0).  Typical value = 18,038. Default: 0.0
	:kvd: Voltage regulator derivative gain (<i>Kvd</i>).  Typical value = 0. Default: 0.0
	:oelin: OEL input selector (<i>OELin</i>).  Typical value = noOELinput (corresponds to <i>OELin</i> = 0 on diagram). Default: None
	:tg: Feedback time constant of inner loop field voltage regulator (<i>Tg</i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:ts: Rectifier firing time constant (<i>Ts</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tvd: Voltage regulator derivative gain (<i>Tvd</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:vamax: Maximum voltage regulator output (<i>Vamax</i>) (&gt; 0).  Typical value = 4,81. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>Vamin</i>) (&lt; 0).  Typical value = -3,85. Default: 0.0
	:vilim: Selector (<i>Vilim</i>). true = <i>Vimin</i>-<i>Vimax</i> limiter is active false = <i>Vimin</i>-<i>Vimax</i> limiter is not active. Typical value = true. Default: False
	:vimax: Maximum voltage regulator input limit (<i>Vimax</i>) (&gt; ExcST6B.vimin).  Typical value = 10. Default: 0.0
	:vimin: Minimum voltage regulator input limit (<i>Vimin</i>) (&lt; ExcST6B.vimax).  Typical value = -10. Default: 0.0
	:vmult: Selector (<i>vmult</i>). true = multiply regulator output by terminal voltage false = do not multiply regulator output by terminal voltage.  Typical value = true. Default: False
	:vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 4,81. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0).  Typical value = -3,85. Default: 0.0
	:xc: Excitation source reactance (<i>Xc</i>).  Typical value = 0,05. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'kcl': [cgmesProfile.DY.value, ],
						'kff': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kia': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'kpa': [cgmesProfile.DY.value, ],
						'kvd': [cgmesProfile.DY.value, ],
						'oelin': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'ts': [cgmesProfile.DY.value, ],
						'tvd': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vilim': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'vmult': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'xc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = 0.0, k1 = False, kcl = 0.0, kff = 0.0, kg = 0.0, kia = 0.0, klr = 0.0, km = 0.0, kpa = 0.0, kvd = 0.0, oelin = None, tg = 0, ts = 0, tvd = 0, vamax = 0.0, vamin = 0.0, vilim = False, vimax = 0.0, vimin = 0.0, vmult = False, vrmax = 0.0, vrmin = 0.0, xc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.k1 = k1
		self.kcl = kcl
		self.kff = kff
		self.kg = kg
		self.kia = kia
		self.klr = klr
		self.km = km
		self.kpa = kpa
		self.kvd = kvd
		self.oelin = oelin
		self.tg = tg
		self.ts = ts
		self.tvd = tvd
		self.vamax = vamax
		self.vamin = vamin
		self.vilim = vilim
		self.vimax = vimax
		self.vimin = vimin
		self.vmult = vmult
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.xc = xc
		
	def __str__(self):
		str = 'class=ExcST6B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
