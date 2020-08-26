from cimpy.output.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
	'''
	The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

	:vtmin: Terminal undervoltage comparison level (). Default: 
	:tdr: Reset time delay (). Default: 
		'''

	cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tdr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n' + DiscontinuousExcitationControlDynamics.__doc__ 

	def __init__(self, vtmin = , tdr = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vtmin = vtmin
		self.tdr = tdr
		
	def __str__(self):
		str = 'class=DiscExcContIEEEDEC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
