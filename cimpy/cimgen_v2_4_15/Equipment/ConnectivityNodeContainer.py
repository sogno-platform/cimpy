from cimpy.cimgen_v2_4_15.Equipment.PowerSystemResource import PowerSystemResource


class ConnectivityNodeContainer(PowerSystemResource):
	'''
	A base class for all objects that may contain connectivity nodes or topological nodes.

	:TopologicalNode: The topological nodes which belong to this connectivity node container. Default: []
		'''

	reference_dict = { 'TopologyVersion': ['TopologicalNode', ],
					 } 

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
