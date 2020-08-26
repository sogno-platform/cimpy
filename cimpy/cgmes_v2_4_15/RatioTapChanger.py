from cimpy.output.TapChanger import TapChanger


class RatioTapChanger(TapChanger):
	'''
	A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.

	:tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Default: 
	:stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position. Default: 
	:RatioTapChangerTable: The ratio tap changer of this tap ratio table. Default: 
	:TransformerEnd: Ratio tap changer associated with this transformer end. Default: 
		'''

	cgmesProfile = TapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'tculControlMode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'stepVoltageIncrement': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'RatioTapChangerTable': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'TransformerEnd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TapChanger: \n' + TapChanger.__doc__ 

	def __init__(self, tculControlMode = , stepVoltageIncrement = , RatioTapChangerTable = , TransformerEnd = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tculControlMode = tculControlMode
		self.stepVoltageIncrement = stepVoltageIncrement
		self.RatioTapChangerTable = RatioTapChangerTable
		self.TransformerEnd = TransformerEnd
		
	def __str__(self):
		str = 'class=RatioTapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
