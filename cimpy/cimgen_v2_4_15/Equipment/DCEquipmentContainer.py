from cimpy.cimgen_v2_4_15.Equipment.EquipmentContainer import EquipmentContainer


class DCEquipmentContainer(EquipmentContainer):
	'''
	A modeling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNodes. Hence it can contain both AC and DC equipment.

	:DCNodes:  Default: []
	:DCTopologicalNode:  Default: []
		'''

	reference_dict = { 'TopologyVersion': ['DCTopologicalNode', ],
					 } 

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, DCNodes = [], DCTopologicalNode = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCNodes = DCNodes
		self.DCTopologicalNode = DCTopologicalNode
		
	def __str__(self):
		str = 'class=DCEquipmentContainer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
