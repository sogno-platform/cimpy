from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcELIN2(ExcitationSystemDynamics):
	'''
	Detailed excitation system ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

	:k1: Voltage regulator input gain (<i>K1</i>).  Typical value = 0. Default: 0.0
	:k1ec: Voltage regulator input limit (<i>K1ec</i>).  Typical value = 2. Default: 0.0
	:kd1: Voltage controller derivative gain (<i>Kd1</i>).  Typical value = 34,5. Default: 0.0
	:tb1: Voltage controller derivative washout time constant (<i>Tb1</i>) (&gt;= 0).  Typical value = 12,45. Default: 0
	:pid1max: Controller follow up gain (<i>PID1max</i>).  Typical value = 2. Default: 0.0
	:ti1: Controller follow up deadband (<i>Ti1</i>).  Typical value = 0. Default: 0.0
	:iefmax2: Minimum open circuit excitation voltage (<i>I</i><i><sub>efmax2</sub></i>).  Typical value = -5. Default: 0.0
	:k2: Gain (<i>K2</i>).  Typical value = 5. Default: 0.0
	:ketb: Gain (<i>Ketb</i>).  Typical value = 0,06. Default: 0.0
	:upmax: Limiter (<i>Upmax</i>) (&gt; ExcELIN2.upmin).  Typical value = 3. Default: 0.0
	:upmin: Limiter (<i>Upmin</i>) (&lt; ExcELIN2.upmax).  Typical value = 0. Default: 0.0
	:te: Time constant (<i>Te</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:xp: Excitation transformer effective reactance (<i>Xp</i>).  Typical value = 1. Default: 0.0
	:te2: Time Constant (<i>T</i><i><sub>e2</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:ke2: Gain (<i>Ke2</i>).  Typical value = 0,1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve</i><i><sub>1</sub></i>) (&gt; 0).  Typical value = 3. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>1</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve</i><i><sub>2</sub></i>) (&gt; 0).  Typical value = 0. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>2</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:tr4: Time constant (<i>T</i><i><sub>r4</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:k3: Gain (<i>K3</i>).  Typical value = 0,1. Default: 0.0
	:ti3: Time constant (<i>T</i><i><sub>i3</sub></i>) (&gt;= 0).  Typical value = 3. Default: 0
	:k4: Gain (<i>K4</i>).  Typical value = 0. Default: 0.0
	:ti4: Time constant (<i>T</i><i><sub>i4</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:iefmax: Limiter (<i>I</i><i><sub>efmax</sub></i>) (&gt; ExcELIN2.iefmin).  Typical value = 1. Default: 0.0
	:iefmin: Limiter (<i>I</i><i><sub>efmin</sub></i>) (&lt; ExcELIN2.iefmax).  Typical value = 1. Default: 0.0
	:efdbas: Gain (<i>Efdbas</i>).  Typical value = 0,1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k1ec': [cgmesProfile.DY.value, ],
						'kd1': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'pid1max': [cgmesProfile.DY.value, ],
						'ti1': [cgmesProfile.DY.value, ],
						'iefmax2': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'ketb': [cgmesProfile.DY.value, ],
						'upmax': [cgmesProfile.DY.value, ],
						'upmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'xp': [cgmesProfile.DY.value, ],
						'te2': [cgmesProfile.DY.value, ],
						'ke2': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'tr4': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'ti3': [cgmesProfile.DY.value, ],
						'k4': [cgmesProfile.DY.value, ],
						'ti4': [cgmesProfile.DY.value, ],
						'iefmax': [cgmesProfile.DY.value, ],
						'iefmin': [cgmesProfile.DY.value, ],
						'efdbas': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = 0.0, k1ec = 0.0, kd1 = 0.0, tb1 = 0, pid1max = 0.0, ti1 = 0.0, iefmax2 = 0.0, k2 = 0.0, ketb = 0.0, upmax = 0.0, upmin = 0.0, te = 0, xp = 0.0, te2 = 0, ke2 = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0, tr4 = 0, k3 = 0.0, ti3 = 0, k4 = 0.0, ti4 = 0, iefmax = 0.0, iefmin = 0.0, efdbas = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.k1ec = k1ec
		self.kd1 = kd1
		self.tb1 = tb1
		self.pid1max = pid1max
		self.ti1 = ti1
		self.iefmax2 = iefmax2
		self.k2 = k2
		self.ketb = ketb
		self.upmax = upmax
		self.upmin = upmin
		self.te = te
		self.xp = xp
		self.te2 = te2
		self.ke2 = ke2
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.tr4 = tr4
		self.k3 = k3
		self.ti3 = ti3
		self.k4 = k4
		self.ti4 = ti4
		self.iefmax = iefmax
		self.iefmin = iefmin
		self.efdbas = efdbas
		
	def __str__(self):
		str = 'class=ExcELIN2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
