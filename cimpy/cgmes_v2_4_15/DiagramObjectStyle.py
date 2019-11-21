from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class DiagramObjectStyle(IdentifiedObject):
	'''
	A reference to a style used by the originating system for a diagram object.  A diagram object style describes information such as line thickness, shape such as circle or rectangle etc, and color.

	:StyledObjects: A style can be assigned to multiple diagram objects. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.DI.value, ],
						'StyledObjects': [cgmesProfile.DI.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, StyledObjects = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.StyledObjects = StyledObjects
		
	def __str__(self):
		str = 'class=DiagramObjectStyle\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
