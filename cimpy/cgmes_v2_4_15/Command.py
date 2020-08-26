from cimpy.output.Control import Control


class Command(Control):
	'''
	A Command is a discrete control used for supervisory control.

	:normalValue: Normal value for Control.value e.g. used for percentage scaling. Default: 
	:value: The value representing the actuator output. Default: 
	:DiscreteValue: The Control variable associated with the MeasurementValue. Default: 
	:ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name. Default: 
		'''

	cgmesProfile = Control.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'normalValue': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'DiscreteValue': [cgmesProfile.EQ.value, ],
						'ValueAliasSet': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Control: \n' + Control.__doc__ 

	def __init__(self, normalValue = , value = , DiscreteValue = , ValueAliasSet = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.normalValue = normalValue
		self.value = value
		self.DiscreteValue = DiscreteValue
		self.ValueAliasSet = ValueAliasSet
		
	def __str__(self):
		str = 'class=Command\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
