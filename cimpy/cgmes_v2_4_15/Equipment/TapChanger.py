from cimpy.cgmes_v2_4_15.Equipment.PowerSystemResource import PowerSystemResource


class TapChanger(PowerSystemResource):
	'''
	Mechanism for changing transformer winding tap positions.

	:highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0.0
	:lowStep: Lowest possible tap step position, retard from neutral Default: 0.0
	:ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. Default: False
	:neutralStep: The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0
	:neutralU: Voltage at which the winding operates at the neutral tap setting. Default: 0.0
	:normalStep: The tap step position used in &quot;normal&quot; network operation for this winding. For a &quot;Fixed&quot; tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0
	:TapChangerControl: The tap changers that participates in this regulating tap control scheme. Default: None
	:SvTapStep: The tap step state associated with the tap changer. Default: None
	:controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
	:step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0
		'''

	reference_dict = { 'StateVariablesVersion': ['SvTapStep', ],
					'SteadyStateHypothesisVersion': ['controlEnabled','step', ],
					 } 

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, highStep = 0.0, lowStep = 0.0, ltcFlag = False, neutralStep = 0.0, neutralU = 0.0, normalStep = 0.0, TapChangerControl = None, SvTapStep = None, controlEnabled = False, step = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.highStep = highStep
		self.lowStep = lowStep
		self.ltcFlag = ltcFlag
		self.neutralStep = neutralStep
		self.neutralU = neutralU
		self.normalStep = normalStep
		self.TapChangerControl = TapChangerControl
		self.SvTapStep = SvTapStep
		self.controlEnabled = controlEnabled
		self.step = step
		
	def __str__(self):
		str = 'class=TapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
