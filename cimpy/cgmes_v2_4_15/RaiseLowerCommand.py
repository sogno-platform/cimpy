from .AnalogControl import AnalogControl


class RaiseLowerCommand(AnalogControl):
	'''
	An analog control that increase or decrease a set point value with pulses.

	:ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name. Default: None
		'''

	cgmesProfile = AnalogControl.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ValueAliasSet': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class AnalogControl: \n' + AnalogControl.__doc__ 

	def __init__(self, ValueAliasSet = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ValueAliasSet = ValueAliasSet
		
	def __str__(self):
		str = 'class=RaiseLowerCommand\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
