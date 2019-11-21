from cimpy.cgmes_v2_4_15_flat.ConductingEquipment import ConductingEquipment


class Ground(ConductingEquipment):
	'''
	A point where the system is grounded used for connecting conducting equipment to ground. The power system model can have any number of grounds.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=Ground\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
