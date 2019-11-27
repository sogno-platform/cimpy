from cimpy.cgmes_v2_4_15.Base import Base


class SvStatus(Base):
	'''
	State variable for status.

	:ConductingEquipment: The conducting equipment associated with the status state variable. Default: None
	:inService: The in service status as a result of topology processing. Default: False
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'ConductingEquipment': [cgmesProfile.SV.value, ],
						'inService': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, ConductingEquipment = None, inService = False,  ):
	
		self.ConductingEquipment = ConductingEquipment
		self.inService = inService
		
	def __str__(self):
		str = 'class=SvStatus\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
