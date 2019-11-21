from cimpy.cgmes_v2_4_15_flat.DCEquipmentContainer import DCEquipmentContainer


class DCLine(DCEquipmentContainer):
	'''
	Overhead lines and/or cables connecting two or more HVDC substations.

	:Region:  Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Region': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCEquipmentContainer: \n' + DCEquipmentContainer.__doc__ 

	def __init__(self, Region = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Region = Region
		
	def __str__(self):
		str = 'class=DCLine\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
