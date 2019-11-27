from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class TransformerEnd(IdentifiedObject):
	'''
	A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because it associates to terminal but is not a specialization of ConductingEquipment.

	:BaseVoltage: Base voltage of the transformer end.  This is essential for PU calculation. Default: None
	:Terminal: Terminal of the power transformer to which this transformer end belongs. Default: None
	:PhaseTapChanger: Transformer end to which this phase tap changer belongs. Default: None
	:RatioTapChanger: Transformer end to which this ratio tap changer belongs. Default: None
	:endNumber: Number for this transformer end, corresponding to the end's order in the power transformer vector group or phase angle clock number.  Highest voltage winding should be 1.  Each end within a power transformer should have a unique subsequent end number.   Note the transformer end number need not match the terminal sequence number. Default: 0
	:rground: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. Default: 0.0
	:grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. Default: False
	:xground: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. Default: 0.0
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'BaseVoltage': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						'PhaseTapChanger': [cgmesProfile.EQ.value, ],
						'RatioTapChanger': [cgmesProfile.EQ.value, ],
						'endNumber': [cgmesProfile.EQ.value, ],
						'rground': [cgmesProfile.EQ.value, ],
						'grounded': [cgmesProfile.EQ.value, ],
						'xground': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, BaseVoltage = None, Terminal = None, PhaseTapChanger = None, RatioTapChanger = None, endNumber = 0, rground = 0.0, grounded = False, xground = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BaseVoltage = BaseVoltage
		self.Terminal = Terminal
		self.PhaseTapChanger = PhaseTapChanger
		self.RatioTapChanger = RatioTapChanger
		self.endNumber = endNumber
		self.rground = rground
		self.grounded = grounded
		self.xground = xground
		
	def __str__(self):
		str = 'class=TransformerEnd\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
