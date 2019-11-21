from cimpy.cgmes_v2_4_15_flat.Base import Base


class SvShuntCompensatorSections(Base):
	'''
	State variable for the number of sections in service for a shunt compensator.

	:sections: The number of sections in service as a continous variable. To get integer value scale with ShuntCompensator.bPerSection. Default: 0.0
	:ShuntCompensator: The shunt compensator for which the state applies. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'sections': [cgmesProfile.SV.value, ],
						'ShuntCompensator': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, sections = 0.0, ShuntCompensator = None,  ):
	
		self.sections = sections
		self.ShuntCompensator = ShuntCompensator
		
	def __str__(self):
		str = 'class=SvShuntCompensatorSections\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
