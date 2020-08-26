from cimpy.output.PowerSystemResource import PowerSystemResource


class TapChanger(PowerSystemResource):
	'''
	Mechanism for changing transformer winding tap positions.

	:highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 
	:lowStep: Lowest possible tap step position, retard from neutral Default: 
	:ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. Default: 
	:neutralStep: The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 
	:neutralU: Voltage at which the winding operates at the neutral tap setting. Default: 
	:normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 
	:TapChangerControl: The tap changers that participates in this regulating tap control scheme. Default: 
	:TapSchedules: A TapSchedule is associated with a TapChanger. Default: 
	:controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: 
	:step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 
	:SvTapStep: The tap step state associated with the tap changer. Default: 
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'highStep': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'lowStep': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ltcFlag': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'neutralStep': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'neutralU': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'normalStep': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'TapChangerControl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'TapSchedules': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'controlEnabled': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'step': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'SvTapStep': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, highStep = , lowStep = , ltcFlag = , neutralStep = , neutralU = , normalStep = , TapChangerControl = , TapSchedules = , controlEnabled = , step = , SvTapStep = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.highStep = highStep
		self.lowStep = lowStep
		self.ltcFlag = ltcFlag
		self.neutralStep = neutralStep
		self.neutralU = neutralU
		self.normalStep = normalStep
		self.TapChangerControl = TapChangerControl
		self.TapSchedules = TapSchedules
		self.controlEnabled = controlEnabled
		self.step = step
		self.SvTapStep = SvTapStep
		
	def __str__(self):
		str = 'class=TapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
