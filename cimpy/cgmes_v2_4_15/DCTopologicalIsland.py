from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class DCTopologicalIsland(IdentifiedObject):
	'''
	An electrically connected subset of the network. DC topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

	:DCTopologicalNodes:  Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'DCTopologicalNodes': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTopologicalNodes = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTopologicalNodes = DCTopologicalNodes
		
	def __str__(self):
		str = 'class=DCTopologicalIsland\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
