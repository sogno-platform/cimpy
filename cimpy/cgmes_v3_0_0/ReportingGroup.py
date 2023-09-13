from .IdentifiedObject import IdentifiedObject


class ReportingGroup(IdentifiedObject):
	'''
	A reporting group is used for various ad-hoc groupings used for reporting.

	:TopologicalNode: The topological nodes that belong to the reporting group. Default: "list"
	:BusNameMarker: The bus name markers that belong to this reporting group. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.TP.value, cgmesProfile.EQ.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						'BusNameMarker': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, TopologicalNode = "list", BusNameMarker = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TopologicalNode = TopologicalNode
		self.BusNameMarker = BusNameMarker
		
	def __str__(self):
		str = 'class=ReportingGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
