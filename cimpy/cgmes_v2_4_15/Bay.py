from .EquipmentContainer import EquipmentContainer


class Bay(EquipmentContainer):
	'''
	A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization of equipment.

	:VoltageLevel: The voltage level containing this bay. Default: None
		'''

	cgmesProfile = EquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'VoltageLevel': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, VoltageLevel = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.VoltageLevel = VoltageLevel
		
	def __str__(self):
		str = 'class=Bay\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
