from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class ReportingGroup(IdentifiedObject):
	'''
	A reporting group is used for various ad-hoc groupings used for reporting.

	:BusNameMarker: The reporting group to which this bus name marker belongs. Default: []
	:TopologicalNode: The reporting group to which the topological node belongs. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.TP.value, ],
						'BusNameMarker': [cgmesProfile.EQ.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, BusNameMarker = [], TopologicalNode = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BusNameMarker = BusNameMarker
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=ReportingGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
