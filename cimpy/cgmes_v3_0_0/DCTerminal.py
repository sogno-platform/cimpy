from .DCBaseTerminal import DCBaseTerminal


class DCTerminal(DCBaseTerminal):
	'''
	An electrical connection point to generic DC conducting equipment.

	:DCConductingEquipment: An DC  terminal belong to a DC conducting equipment. Default: None
		'''

	cgmesProfile = DCBaseTerminal.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.TP.value, cgmesProfile.EQ.value, ],
						'DCConductingEquipment': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

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
