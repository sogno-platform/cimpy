from cimpy.cgmes_v2_4_15.Base import Base


class TieFlow(Base):
	'''
	A flow specification in terms of location and direction for a control area.

	:Terminal: The terminal to which this tie flow belongs. Default: None
	:ControlArea: The control area of the tie flows. Default: None
	:positiveFlowIn: True if the flow into the terminal (load convention) is also flow into the control area.  For example, this attribute should be true if using the tie line terminal further away from the control area. For example to represent a tie to a shunt component (like a load or generator) in another area, this is the near end of a branch and this attribute would be specified as false. Default: False
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						'ControlArea': [cgmesProfile.EQ.value, ],
						'positiveFlowIn': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, Terminal = None, ControlArea = None, positiveFlowIn = False,  ):
	
		self.Terminal = Terminal
		self.ControlArea = ControlArea
		self.positiveFlowIn = positiveFlowIn
		
	def __str__(self):
		str = 'class=TieFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
