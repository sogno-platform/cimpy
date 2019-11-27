from cimpy.cgmes_v2_4_15.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
	'''
	The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

	:vtmin: Terminal undervoltage comparison level (). Default: 0.0
	:tdr: Reset time delay (). Default: 0.0
		'''

	cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vtmin': [cgmesProfile.DY.value, ],
						'tdr': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n' + DiscontinuousExcitationControlDynamics.__doc__ 

	def __init__(self, vtmin = 0.0, tdr = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vtmin = vtmin
		self.tdr = tdr
		
	def __str__(self):
		str = 'class=DiscExcContIEEEDEC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
