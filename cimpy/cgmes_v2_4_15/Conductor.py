from cimpy.cgmes_v2_4_15.ConductingEquipment import ConductingEquipment


class Conductor(ConductingEquipment):
	'''
	Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.

	:length: Segment length for calculating line section capabilities Default: 0.0
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'length': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, length = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.length = length
		
	def __str__(self):
		str = 'class=Conductor\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
