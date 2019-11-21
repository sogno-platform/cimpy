from cimpy.cgmes_v2_4_15_flat.DCBaseTerminal import DCBaseTerminal


class DCTerminal(DCBaseTerminal):
	'''
	An electrical connection point to generic DC conducting equipment.

	:DCConductingEquipment:  Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.TP.value, ],
						'DCConductingEquipment': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCBaseTerminal: \n' + DCBaseTerminal.__doc__ 

	def __init__(self, DCConductingEquipment = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCConductingEquipment = DCConductingEquipment
		
	def __str__(self):
		str = 'class=DCTerminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
