from cimpy.cgmes_v2_4_15.EquipmentContainer import EquipmentContainer


class Line(EquipmentContainer):
	'''
	Contains equipment beyond a substation belonging to a power transmission line.

	:Region: The sub-geographical region of the line. Default: None
		'''

	cgmesProfile = EquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Region': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, Region = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Region = Region
		
	def __str__(self):
		str = 'class=Line\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
