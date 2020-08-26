from cimpy.output.VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType1(VoltageCompensatorDynamics):
	'''
	Reference: IEEE Standard 421.5-2005 Section 4.

	:rc:  Default: 
	:xc:  Default: 
	:tr:  Default: 
		'''

	cgmesProfile = VoltageCompensatorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'rc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class VoltageCompensatorDynamics: \n' + VoltageCompensatorDynamics.__doc__ 

	def __init__(self, rc = , xc = , tr = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.rc = rc
		self.xc = xc
		self.tr = tr
		
	def __str__(self):
		str = 'class=VCompIEEEType1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
