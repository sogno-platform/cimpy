from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcRQB(ExcitationSystemDynamics):
	'''
	Excitation system type RQB (four-loop regulator, r?gulateur quatre boucles, developed in France) primarily used in nuclear or thermal generating units. This excitation system shall be always used together with power system stabilizer type PssRQB.

	:ki0: Voltage reference input gain (<i>Ki0</i>).  Typical value = 12,7. Default: 0.0
	:ki1: Voltage input gain (<i>Ki1</i>).  Typical value = -16,8. Default: 0.0
	:te: Lead lag time constant (<i>TE</i>) (&gt;= 0).  Typical value = 0,22. Default: 0
	:tc: Lead lag time constant (<i>TC</i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:klir: OEL input gain (<i>KLIR</i>).  Typical value = 12,13. Default: 0.0
	:ucmin: Minimum voltage reference limit (<i>UCMIN</i>) (&lt; ExcRQB.ucmax).  Typical value = 0,9. Default: 0.0
	:ucmax: Maximum voltage reference limit (<i>UCMAX</i>) (&gt; ExcRQB.ucmin).  Typical value = 1,1. Default: 0.0
	:lus: Setpoint (<i>LUS</i>).  Typical value = 0,12. Default: 0.0
	:klus: Limiter gain (<i>KLUS</i>).  Typical value = 50. Default: 0.0
	:mesu: Voltage input time constant (<i>MESU</i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:t4m: Input time constant (<i>T4M</i>) (&gt;= 0).  Typical value = 5. Default: 0
	:lsat: Integrator limiter (<i>LSAT</i>).  Typical value = 5,73. Default: 0.0
	:tf: Exciter time constant (<i>TF</i>) (&gt;= 0).  Typical value = 0,01. Default: 0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ki0': [cgmesProfile.DY.value, ],
						'ki1': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'klir': [cgmesProfile.DY.value, ],
						'ucmin': [cgmesProfile.DY.value, ],
						'ucmax': [cgmesProfile.DY.value, ],
						'lus': [cgmesProfile.DY.value, ],
						'klus': [cgmesProfile.DY.value, ],
						'mesu': [cgmesProfile.DY.value, ],
						't4m': [cgmesProfile.DY.value, ],
						'lsat': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ki0 = 0.0, ki1 = 0.0, te = 0, tc = 0, klir = 0.0, ucmin = 0.0, ucmax = 0.0, lus = 0.0, klus = 0.0, mesu = 0, t4m = 0, lsat = 0.0, tf = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ki0 = ki0
		self.ki1 = ki1
		self.te = te
		self.tc = tc
		self.klir = klir
		self.ucmin = ucmin
		self.ucmax = ucmax
		self.lus = lus
		self.klus = klus
		self.mesu = mesu
		self.t4m = t4m
		self.lsat = lsat
		self.tf = tf
		
	def __str__(self):
		str = 'class=ExcRQB\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
