from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcELIN1(ExcitationSystemDynamics):
	'''
	Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  A power system stabilizer with power input is included in the model.

	:tfi: Current transducer time constant (Tfi).  Typical Value = 0. Default: 
	:tnu: Controller reset time constant (Tnu).  Typical Value = 2. Default: 
	:vpu: Voltage controller proportional gain (Vpu).  Typical Value = 34.5. Default: 
	:vpi: Current controller gain (Vpi).  Typical Value = 12.45. Default: 
	:vpnf: Controller follow up gain (Vpnf).  Typical Value = 2. Default: 
	:dpnf: Controller follow up dead band (Dpnf).  Typical Value = 0. Default: 
	:tsw: Stabilizer parameters (Tsw).  Typical Value = 3. Default: 
	:efmin: Minimum open circuit excitation voltage (Efmin).  Typical Value = -5. Default: 
	:efmax: Maximum open circuit excitation voltage (Efmax).  Typical Value = 5. Default: 
	:xe: Excitation transformer effective reactance (Xe) (>=0).  Xe represents the regulation of the transformer/rectifier unit.  Typical Value = 0.06. Default: 
	:ks1: Stabilizer Gain 1 (Ks1).  Typical Value = 0. Default: 
	:ks2: Stabilizer Gain 2 (Ks2).  Typical Value = 0. Default: 
	:ts1: Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1. Default: 
	:ts2: Stabilizer Filter Time Constant (Ts2).  Typical Value = 1. Default: 
	:smax: Stabilizer Limit Output (smax).  Typical Value = 0.1. Default: 
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

	def __init__(self, tfi = , tnu = , vpu = , vpi = , vpnf = , dpnf = , tsw = , efmin = , efmax = , xe = , ks1 = , ks2 = , ts1 = , ts2 = , smax = ,  *args, **kw_args):
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
