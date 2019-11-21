from cimpy.cgmes_v2_4_15_flat.DCBaseTerminal import DCBaseTerminal


class ACDCConverterDCTerminal(DCBaseTerminal):
	'''
	A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC side.

	:DCConductingEquipment:  Default: None
	:polarity: Represents the normal network polarity condition. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.TP.value, ],
						'DCConductingEquipment': [cgmesProfile.EQ.value, ],
						'polarity': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DCBaseTerminal: \n' + DCBaseTerminal.__doc__ 

	def __init__(self, DCConductingEquipment = None, polarity = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCConductingEquipment = DCConductingEquipment
		self.polarity = polarity
		
	def __str__(self):
		str = 'class=ACDCConverterDCTerminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
