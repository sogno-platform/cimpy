from cimpy.cgmes_v2_4_15.LoadDynamics import LoadDynamics


class LoadComposite(LoadDynamics):
	'''
	This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

	:epvs: Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7. Default: 0.0
	:epfs: Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5. Default: 0.0
	:eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2. Default: 0.0
	:eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0. Default: 0.0
	:epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7. Default: 0.0
	:epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5. Default: 0.0
	:eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2. Default: 0.0
	:eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0. Default: 0.0
	:lfrac: Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8. Default: 0.0
	:h: Inertia constant (H).  Typical Value = 2.5. Default: 0.0
	:pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.5. Default: 0.0
		'''

	cgmesProfile = LoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'epvs': [cgmesProfile.DY.value, ],
						'epfs': [cgmesProfile.DY.value, ],
						'eqvs': [cgmesProfile.DY.value, ],
						'eqfs': [cgmesProfile.DY.value, ],
						'epvd': [cgmesProfile.DY.value, ],
						'epfd': [cgmesProfile.DY.value, ],
						'eqvd': [cgmesProfile.DY.value, ],
						'eqfd': [cgmesProfile.DY.value, ],
						'lfrac': [cgmesProfile.DY.value, ],
						'h': [cgmesProfile.DY.value, ],
						'pfrac': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, epvs = 0.0, epfs = 0.0, eqvs = 0.0, eqfs = 0.0, epvd = 0.0, epfd = 0.0, eqvd = 0.0, eqfd = 0.0, lfrac = 0.0, h = 0.0, pfrac = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.epvs = epvs
		self.epfs = epfs
		self.eqvs = eqvs
		self.eqfs = eqfs
		self.epvd = epvd
		self.epfd = epfd
		self.eqvd = eqvd
		self.eqfd = eqfd
		self.lfrac = lfrac
		self.h = h
		self.pfrac = pfrac
		
	def __str__(self):
		str = 'class=LoadComposite\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
