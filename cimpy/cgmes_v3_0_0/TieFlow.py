from .IdentifiedObject import IdentifiedObject


class TieFlow(IdentifiedObject):
	'''
	Defines the structure (in terms of location and direction) of the net interchange constraint for a control area. This constraint may be used by either AGC or power flow.

	:ControlArea: The control area of the tie flows. Default: None
	:Terminal: The terminal to which this tie flow belongs. Default: None
	:positiveFlowIn: Specifies the sign of the tie flow associated with a control area. True if positive flow into the terminal (load convention) is also positive flow into the control area.  See the description of ControlArea for further explanation of how TieFlow.positiveFlowIn is used. Default: False
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ControlArea': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						'positiveFlowIn': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, ControlArea = None, Terminal = None, positiveFlowIn = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ControlArea = ControlArea
		self.Terminal = Terminal
		self.positiveFlowIn = positiveFlowIn
		
	def __str__(self):
		str = 'class=TieFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
