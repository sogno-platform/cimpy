from .ConductingEquipment import ConductingEquipment


class Clamp(ConductingEquipment):
	'''
	A Clamp is a galvanic connection at a line segment where other equipment is connected. A Clamp does not cut the line segment.  A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode. Any other ConductingEquipment can be connected to the Clamp ConnectivityNode.

	:ACLineSegment: The line segment to which the clamp is connected. Default: None
	:lengthFromTerminal1: The length to the place where the clamp is located starting from side one of the line segment, i.e. the line segment terminal with sequence number equal to 1. Default: 0.0
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ACLineSegment': [cgmesProfile.EQ.value, ],
						'lengthFromTerminal1': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, ACLineSegment = None, lengthFromTerminal1 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ACLineSegment = ACLineSegment
		self.lengthFromTerminal1 = lengthFromTerminal1
		
	def __str__(self):
		str = 'class=Clamp\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
