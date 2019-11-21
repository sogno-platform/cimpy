from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC3A(ExcitationSystemDynamics):
	'''
	This is modified IEEE DC3A direct current commutator exciters with speed input, and death band.  DC old type 4.

	:trh: Rheostat travel time (Trh).  Typical Value = 20. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
	:kr: Death band (Kr).  If Kr is not zero, the voltage regulator input changes at a constant rate if Verr > Kr or Verr < -Kr as per the IEEE (1968) Type 4 model. If Kr is zero, the error signal drives the voltage regulator continuously as per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models.  Typical Value = 0. Default: 0.0
	:kv: Fast raise/lower contact setting (Kv).  Typical Value = 0.05. Default: 0.0
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83. Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
	:efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 2.6. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.1. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 3.45. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]).  Typical Value = 0.35. Default: 0.0
	:exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero not applied to integrator output. Typical Value = true. Default: False
	:edfmax: Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99. Default: 0.0
	:efdmin: Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99. Default: 0.0
	:efdlim: (Efdlim). true = exciter output limiter is active false = exciter output limiter not active. Typical Value = true. Default: False
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'trh': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'kr': [cgmesProfile.DY.value, ],
						'kv': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						'edfmax': [cgmesProfile.DY.value, ],
						'efdmin': [cgmesProfile.DY.value, ],
						'efdlim': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, trh = 0.0, ks = 0.0, kr = 0.0, kv = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0.0, ke = 0.0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, exclim = False, edfmax = 0.0, efdmin = 0.0, efdlim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.trh = trh
		self.ks = ks
		self.kr = kr
		self.kv = kv
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.ke = ke
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.exclim = exclim
		self.edfmax = edfmax
		self.efdmin = efdmin
		self.efdlim = efdlim
		
	def __str__(self):
		str = 'class=ExcDC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
