from cimpy.output.VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType2(VoltageCompensatorDynamics):
	'''
	

	:tr:  Default: 
	:GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another generator. Default: 
		'''

	cgmesProfile = VoltageCompensatorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'GenICompensationForGenJ': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class VoltageCompensatorDynamics: \n' + VoltageCompensatorDynamics.__doc__ 

	def __init__(self, tr = , GenICompensationForGenJ = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tr = tr
		self.GenICompensationForGenJ = GenICompensationForGenJ
		
	def __str__(self):
		str = 'class=VCompIEEEType2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
