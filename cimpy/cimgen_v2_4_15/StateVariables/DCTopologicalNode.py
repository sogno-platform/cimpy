from cimpy.cimgen_v2_4_15.Equipment.IdentifiedObject import IdentifiedObject


class DCTopologicalNode(IdentifiedObject):
	'''
	DC bus.

	:DCTopologicalIsland:  Default: None
		'''

	

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTopologicalIsland = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTopologicalIsland = DCTopologicalIsland
		
	def __str__(self):
		str = 'class=DCTopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
