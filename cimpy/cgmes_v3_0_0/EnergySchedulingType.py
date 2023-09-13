from .IdentifiedObject import IdentifiedObject


class EnergySchedulingType(IdentifiedObject):
	'''
	Used to define the type of generation for scheduling purposes.

	:EnergySource: Energy Source of a particular Energy Scheduling Type. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'EnergySource': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, EnergySource = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergySource = EnergySource
		
	def __str__(self):
		str = 'class=EnergySchedulingType\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
