from cimpy.cgmes_v2_4_15.PowerSystemResource import PowerSystemResource


class ConnectivityNodeContainer(PowerSystemResource):
	'''
	A base class for all objects that may contain connectivity nodes or topological nodes.

	:TopologicalNode: The topological nodes which belong to this connectivity node container. Default: []
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.TP.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, TopologicalNode = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=ConnectivityNodeContainer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
