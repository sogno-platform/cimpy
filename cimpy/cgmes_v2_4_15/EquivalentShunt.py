from cimpy.cgmes_v2_4_15_flat.EquivalentEquipment import EquivalentEquipment


class EquivalentShunt(EquivalentEquipment):
	'''
	The class represents equivalent shunts.

	:b: Positive sequence shunt susceptance. Default: 0.0
	:g: Positive sequence shunt conductance. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'b': [cgmesProfile.EQ.value, ],
						'g': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EquivalentEquipment: \n' + EquivalentEquipment.__doc__ 

	def __init__(self, b = 0.0, g = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.b = b
		self.g = g
		
	def __str__(self):
		str = 'class=EquivalentShunt\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
