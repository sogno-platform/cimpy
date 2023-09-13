from .Base import Base


class SvSwitch(Base):
	'''
	State variable for switch.

	:open: The attribute tells if the computed state of the switch is considered open. Default: False
	:Switch: The switch associated with the switch state. Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'open': [cgmesProfile.SV.value, ],
						'Switch': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, open = False, Switch = None,  ):
	
		self.open = open
		self.Switch = Switch
		
	def __str__(self):
		str = 'class=SvSwitch\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
