from cimpy.cgmes_v2_4_15_flat.Base import Base


class SvVoltage(Base):
	'''
	State variable for voltage.

	:angle: The voltage angle of the topological node complex voltage with respect to system reference. Default: 0.0
	:v: The voltage magnitude of the topological node. Default: 0.0
	:TopologicalNode: The state voltage associated with the topological node. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'angle': [cgmesProfile.SV.value, ],
						'v': [cgmesProfile.SV.value, ],
						'TopologicalNode': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, angle = 0.0, v = 0.0, TopologicalNode = None,  ):
	
		self.angle = angle
		self.v = v
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=SvVoltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
