from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class DCNode(IdentifiedObject):
	'''
	DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

	:DCTerminals:  Default: "many"
	:DCEquipmentContainer:  Default: None
	:DCTopologicalNode: See association end TopologicalNode.ConnectivityNodes. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.TP.value, ],
						'DCTerminals': [cgmesProfile.EQ.value, ],
						'DCEquipmentContainer': [cgmesProfile.EQ.value, ],
						'DCTopologicalNode': [cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTerminals = "many", DCEquipmentContainer = None, DCTopologicalNode = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTerminals = DCTerminals
		self.DCEquipmentContainer = DCEquipmentContainer
		self.DCTopologicalNode = DCTopologicalNode
		
	def __str__(self):
		str = 'class=DCNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
