from cimpy.cimgen_v2_4_15.Base import Base


class TopologicalNode(Base):
	'''
	For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses".

	:SvInjection: The topological node associated with the flow injection state variable. Default: None
	:SvVoltage: The topological node associated with the voltage state. Default: None
	:AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None
	:TopologicalIsland: A topological node belongs to a topological island. Default: None
		'''

	

	

	def __init__(self, SvInjection = None, SvVoltage = None, AngleRefTopologicalIsland = None, TopologicalIsland = None,  ):
	
		self.SvInjection = SvInjection
		self.SvVoltage = SvVoltage
		self.AngleRefTopologicalIsland = AngleRefTopologicalIsland
		self.TopologicalIsland = TopologicalIsland
		
	def __str__(self):
		str = 'class=TopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
