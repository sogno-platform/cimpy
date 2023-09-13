from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcELIN1(ExcitationSystemDynamics):
	'''
	Static PI transformer fed excitation system ELIN (VATECH) - simplified model.  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  A power system stabilizer with power input is included in the model.

	:tfi: Current transducer time constant (<i>Tfi</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tnu: Controller reset time constant (<i>Tnu</i>) (&gt;= 0).  Typical value = 2. Default: 0
	:vpu: Voltage controller proportional gain (<i>Vpu</i>).  Typical value = 34,5. Default: 0.0
	:vpi: Current controller gain (<i>Vpi</i>).  Typical value = 12,45. Default: 0.0
	:vpnf: Controller follow up gain (<i>Vpnf</i>).  Typical value = 2. Default: 0.0
	:dpnf: Controller follow up deadband (<i>Dpnf</i>).  Typical value = 0. Default: 0.0
	:tsw: Stabilizer parameters (<i>Tsw</i>) (&gt;= 0).  Typical value = 3. Default: 0
	:efmin: Minimum open circuit excitation voltage (<i>Efmin</i>) (&lt; ExcELIN1.efmax).  Typical value = -5. Default: 0.0
	:efmax: Maximum open circuit excitation voltage (<i>Efmax</i>) (&gt; ExcELIN1.efmin).  Typical value = 5. Default: 0.0
	:xe: Excitation transformer effective reactance (<i>Xe</i>) (&gt;= 0).  <i>Xe</i> represents the regulation of the transformer/rectifier unit.  Typical value = 0,06. Default: 0.0
	:ks1: Stabilizer gain 1 (<i>Ks1</i>).  Typical value = 0. Default: 0.0
	:ks2: Stabilizer gain 2 (<i>Ks2</i>).  Typical value = 0. Default: 0.0
	:ts1: Stabilizer phase lag time constant (<i>Ts1</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:ts2: Stabilizer filter time constant (<i>Ts2</i>) (&gt;= 0).  Typical value = 1. Default: 0
	:smax: Stabilizer limit output (<i>smax</i>).  Typical value = 0,1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tfi': [cgmesProfile.DY.value, ],
						'tnu': [cgmesProfile.DY.value, ],
						'vpu': [cgmesProfile.DY.value, ],
						'vpi': [cgmesProfile.DY.value, ],
						'vpnf': [cgmesProfile.DY.value, ],
						'dpnf': [cgmesProfile.DY.value, ],
						'tsw': [cgmesProfile.DY.value, ],
						'efmin': [cgmesProfile.DY.value, ],
						'efmax': [cgmesProfile.DY.value, ],
						'xe': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						'ks2': [cgmesProfile.DY.value, ],
						'ts1': [cgmesProfile.DY.value, ],
						'ts2': [cgmesProfile.DY.value, ],
						'smax': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tfi = 0, tnu = 0, vpu = 0.0, vpi = 0.0, vpnf = 0.0, dpnf = 0.0, tsw = 0, efmin = 0.0, efmax = 0.0, xe = 0.0, ks1 = 0.0, ks2 = 0.0, ts1 = 0, ts2 = 0, smax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tfi = tfi
		self.tnu = tnu
		self.vpu = vpu
		self.vpi = vpi
		self.vpnf = vpnf
		self.dpnf = dpnf
		self.tsw = tsw
		self.efmin = efmin
		self.efmax = efmax
		self.xe = xe
		self.ks1 = ks1
		self.ks2 = ks2
		self.ts1 = ts1
		self.ts2 = ts2
		self.smax = smax
		
	def __str__(self):
		str = 'class=ExcELIN1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
