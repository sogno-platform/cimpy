from .PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerNonLinear(PhaseTapChanger):
	'''
	The non-linear phase tap changer describes the non-linear behaviour of a phase tap changer. This is a base class for the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in IEC 61970-301.

	:voltageStepIncrement: The voltage step increment on the out of phase winding (the PowerTransformerEnd where the TapChanger is located) specified in percent of rated voltage of the PowerTransformerEnd. A positive value means a positive voltage variation from the Terminal at the PowerTransformerEnd, where the TapChanger is located, into the transformer. When the increment is negative, the voltage decreases when the tap step increases. Default: 0.0
	:xMax: The reactance depends on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appears at the low and high tap positions. Depending on the `u` curve the attribute can be either higher or lower than PowerTransformerEnd.x. Default: 0.0
	:xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear at the mid tap position.   PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used. Default: 0.0
		'''

	cgmesProfile = PhaseTapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'voltageStepIncrement': [cgmesProfile.EQ.value, ],
						'xMax': [cgmesProfile.EQ.value, ],
						'xMin': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PhaseTapChanger: \n' + PhaseTapChanger.__doc__ 

	def __init__(self, voltageStepIncrement = 0.0, xMax = 0.0, xMin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.voltageStepIncrement = voltageStepIncrement
		self.xMax = xMax
		self.xMin = xMin
		
	def __str__(self):
		str = 'class=PhaseTapChangerNonLinear\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
