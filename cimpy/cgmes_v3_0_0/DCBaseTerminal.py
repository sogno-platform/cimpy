from .ACDCTerminal import ACDCTerminal


class DCBaseTerminal(ACDCTerminal):
	'''
	An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model requires that DC connections are distinct from AC connections.

	:DCTopologicalNode: See association end Terminal.TopologicalNode. Default: None
	:DCNode: The DC connectivity node to which this DC base terminal connects with zero impedance. Default: None
		'''

	cgmesProfile = ACDCTerminal.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.TP.value, cgmesProfile.EQ.value, ],
						'DCTopologicalNode': [cgmesProfile.TP.value, ],
						'DCNode': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCTerminal: \n' + ACDCTerminal.__doc__ 

	def __init__(self, DCTopologicalNode = None, DCNode = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTopologicalNode = DCTopologicalNode
		self.DCNode = DCNode
		
	def __str__(self):
		str = 'class=DCBaseTerminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
