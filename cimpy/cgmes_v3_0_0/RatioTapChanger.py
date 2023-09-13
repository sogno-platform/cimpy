from .TapChanger import TapChanger


class RatioTapChanger(TapChanger):
	'''
	A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.  Angle sign convention (general): Positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).

	:stepVoltageIncrement: Tap step increment, in per cent of rated voltage of the power transformer end, per step position. When the increment is negative, the voltage decreases when the tap step increases. Default: 0.0
	:RatioTapChangerTable: The tap ratio table for this ratio  tap changer. Default: None
	:TransformerEnd: Transformer end to which this ratio tap changer belongs. Default: None
		'''

	cgmesProfile = TapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'stepVoltageIncrement': [cgmesProfile.EQ.value, ],
						'RatioTapChangerTable': [cgmesProfile.EQ.value, ],
						'TransformerEnd': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TapChanger: \n' + TapChanger.__doc__ 

	def __init__(self, stepVoltageIncrement = 0.0, RatioTapChangerTable = None, TransformerEnd = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.stepVoltageIncrement = stepVoltageIncrement
		self.RatioTapChangerTable = RatioTapChangerTable
		self.TransformerEnd = TransformerEnd
		
	def __str__(self):
		str = 'class=RatioTapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
