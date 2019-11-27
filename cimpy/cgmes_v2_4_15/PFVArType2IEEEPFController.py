from cimpy.cgmes_v2_4_15.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


class PFVArType2IEEEPFController(PFVArControllerType2Dynamics):
	'''
	The class represents IEEE PF Controller Type 2 which is a summing point type controller and makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller. The voltage regulator forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section 11.4.

	:pfref: Power factor reference (). Default: 0.0
	:vref: Voltage regulator reference (). Default: 0.0
	:vclmt: Maximum output of the pf controller ().  Typical Value = 0.1. Default: 0.0
	:kp: Proportional gain of the pf controller ().  Typical Value = 1. Default: 0.0
	:ki: Integral gain of the pf controller ().  Typical Value = 1. Default: 0.0
	:vs: Generator sensing voltage (). Default: 0.0
	:exlon: Overexcitation or under excitation flag () true = 1 (not in the overexcitation or underexcitation state, integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral action is disabled to allow the limiter to play its role). Default: False
		'''

	cgmesProfile = PFVArControllerType2Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'pfref': [cgmesProfile.DY.value, ],
						'vref': [cgmesProfile.DY.value, ],
						'vclmt': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'vs': [cgmesProfile.DY.value, ],
						'exlon': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PFVArControllerType2Dynamics: \n' + PFVArControllerType2Dynamics.__doc__ 

	def __init__(self, pfref = 0.0, vref = 0.0, vclmt = 0.0, kp = 0.0, ki = 0.0, vs = 0.0, exlon = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.pfref = pfref
		self.vref = vref
		self.vclmt = vclmt
		self.kp = kp
		self.ki = ki
		self.vs = vs
		self.exlon = exlon
		
	def __str__(self):
		str = 'class=PFVArType2IEEEPFController\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
