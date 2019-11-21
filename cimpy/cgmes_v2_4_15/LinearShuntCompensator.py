from cimpy.cgmes_v2_4_15_flat.ShuntCompensator import ShuntCompensator


class LinearShuntCompensator(ShuntCompensator):
	'''
	A linear shunt compensator has banks or sections with equal admittance values.

	:bPerSection: Positive sequence shunt (charging) susceptance per section Default: 0.0
	:gPerSection: Positive sequence shunt (charging) conductance per section Default: 0.0
	:b0PerSection: Zero sequence shunt (charging) susceptance per section Default: 0.0
	:g0PerSection: Zero sequence shunt (charging) conductance per section Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'bPerSection': [cgmesProfile.EQ.value, ],
						'gPerSection': [cgmesProfile.EQ.value, ],
						'b0PerSection': [cgmesProfile.EQ.value, ],
						'g0PerSection': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ShuntCompensator: \n' + ShuntCompensator.__doc__ 

	def __init__(self, bPerSection = 0.0, gPerSection = 0.0, b0PerSection = 0.0, g0PerSection = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bPerSection = bPerSection
		self.gPerSection = gPerSection
		self.b0PerSection = b0PerSection
		self.g0PerSection = g0PerSection
		
	def __str__(self):
		str = 'class=LinearShuntCompensator\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
