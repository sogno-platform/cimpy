from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcNI(ExcitationSystemDynamics):
	'''
	Bus or solid fed SCR (silicon-controlled rectifier) bridge excitation system model type NI (NVE).

	:busFedSelector: Fed by selector (<i>BusFedSelector</i>).  true = bus fed (switch is closed) false = solid fed (switch is open). Typical value = true. Default: False
	:tr: Time constant (<i>Tr</i>) (&gt;= 0). Typical value = 0,02. Default: 0
	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 210. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vrmax: Maximum voltage regulator ouput (<i>Vrmax</i>) (&gt; ExcNI.vrmin). Typical value = 5,0. Default: 0.0
	:vrmin: Minimum voltage regulator ouput (<i>Vrmin</i>) (&lt; ExcNI.vrmax). Typical value = -2,0. Default: 0.0
	:kf: Excitation control system stabilizer gain (<i>Kf</i>) (&gt; 0).  Typical value 0,01. Default: 0.0
	:tf2: Excitation control system stabilizer time constant (<i>Tf2</i>) (&gt; 0). Typical value = 0,1. Default: 0
	:tf1: Excitation control system stabilizer time constant (<i>Tf1</i>) (&gt; 0). Typical value = 1,0. Default: 0
	:r: <i>rc</i> / <i>rfd</i> (<i>R</i>) (&gt;= 0).  0 means exciter has negative current capability &gt; 0 means exciter does not have negative current capability.   Typical value = 5. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'busFedSelector': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, busFedSelector = False, tr = 0, ka = 0.0, ta = 0, vrmax = 0.0, vrmin = 0.0, kf = 0.0, tf2 = 0, tf1 = 0, r = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.busFedSelector = busFedSelector
		self.tr = tr
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kf = kf
		self.tf2 = tf2
		self.tf1 = tf1
		self.r = r
		
	def __str__(self):
		str = 'class=ExcNI\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
