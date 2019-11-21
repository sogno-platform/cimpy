from cimpy.cgmes_v2_4_15_flat.PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerLinear(PhaseTapChanger):
	'''
	Describes a tap changer with a linear relation between the tap step and the phase angle difference across the transformer. This is a mathematical model that is an approximation of a real phase tap changer. The phase angle is computed as stepPhaseShitfIncrement times the tap position. The secondary side voltage magnitude is the same as at the primary side.

	:stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. Default: 0.0
	:xMax: The reactance depend on the tap position according to a "u" shaped curve. The maximum reactance (xMax) appear at the low and high tap positions. Default: 0.0
	:xMin: The reactance depend on the tap position according to a "u" shaped curve. The minimum reactance (xMin) appear at the mid tap position. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'stepPhaseShiftIncrement': [cgmesProfile.EQ.value, ],
						'xMax': [cgmesProfile.EQ.value, ],
						'xMin': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PhaseTapChanger: \n' + PhaseTapChanger.__doc__ 

	def __init__(self, stepPhaseShiftIncrement = 0.0, xMax = 0.0, xMin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.stepPhaseShiftIncrement = stepPhaseShiftIncrement
		self.xMax = xMax
		self.xMin = xMin
		
	def __str__(self):
		str = 'class=PhaseTapChangerLinear\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
