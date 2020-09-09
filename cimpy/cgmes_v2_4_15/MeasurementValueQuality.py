from .Quality61850 import Quality61850


class MeasurementValueQuality(Quality61850):
	'''
	Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.

	:MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
		'''

	cgmesProfile = Quality61850.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'MeasurementValue': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Quality61850: \n' + Quality61850.__doc__ 

	def __init__(self, MeasurementValue = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.MeasurementValue = MeasurementValue
		
	def __str__(self):
		str = 'class=MeasurementValueQuality\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
