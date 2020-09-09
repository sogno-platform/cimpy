from .Control import Control


class AccumulatorReset(Control):
	'''
	This command reset the counter value to zero.

	:AccumulatorValue: The accumulator value that is reset by the command. Default: None
		'''

	cgmesProfile = Control.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'AccumulatorValue': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Control: \n' + Control.__doc__ 

	def __init__(self, AccumulatorValue = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.AccumulatorValue = AccumulatorValue
		
	def __str__(self):
		str = 'class=AccumulatorReset\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
