from .Sensor import Sensor


class CurrentTransformer(Sensor):
	'''
	Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.

		'''

	cgmesProfile = Sensor.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Sensor: \n' + Sensor.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=CurrentTransformer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
