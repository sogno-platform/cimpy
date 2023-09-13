from .Sensor import Sensor


class PostLineSensor(Sensor):
	'''
	A sensor used mainly in overhead distribution networks as the source of both current and voltage measurements.

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
		str = 'class=PostLineSensor\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
