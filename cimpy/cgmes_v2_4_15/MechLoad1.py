from cimpy.output.MechanicalLoadDynamics import MechanicalLoadDynamics


class MechLoad1(MechanicalLoadDynamics):
	'''
	Mechanical load model type 1.

	:a: Speed squared coefficient (a). Default: 
	:b: Speed coefficient (b). Default: 
	:d: Speed to the exponent coefficient (d). Default: 
	:e: Exponent (e). Default: 
		'''

	cgmesProfile = MechanicalLoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						'b': [cgmesProfile.DY.value, ],
						'd': [cgmesProfile.DY.value, ],
						'e': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MechanicalLoadDynamics: \n' + MechanicalLoadDynamics.__doc__ 

	def __init__(self, a = , b = , d = , e = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.a = a
		self.b = b
		self.d = d
		self.e = e
		
	def __str__(self):
		str = 'class=MechLoad1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
