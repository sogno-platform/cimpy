from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC3A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type DC3A model. This model represents represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties.  These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.   Reference: IEEE Standard 421.5-2005 Section 5.3.

	:trh: Rheostat travel time (T).  Typical Value = 20. Default: 0.0
	:kv: Fast raise/lower contact setting (K).  Typical Value = 0.05. Default: 0.0
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator output (V).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5. Default: 0.0
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 0.05. Default: 0.0
	:efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.375. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.267. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.15. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.068. Default: 0.0
	:exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'trh': [cgmesProfile.DY.value, ],
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
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, trh = 0.0, kv = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0.0, ke = 0.0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, exclim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.trh = trh
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
		
	def __str__(self):
		str = 'class=ExcIEEEDC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
