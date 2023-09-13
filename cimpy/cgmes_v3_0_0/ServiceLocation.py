from .WorkLocation import WorkLocation


class ServiceLocation(WorkLocation):
	'''
	A real estate location, commonly referred to as premises.

		'''

	cgmesProfile = WorkLocation.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WorkLocation: \n' + WorkLocation.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=ServiceLocation\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
