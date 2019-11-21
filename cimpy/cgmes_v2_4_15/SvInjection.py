from cimpy.cgmes_v2_4_15_flat.Base import Base


class SvInjection(Base):
	'''
	The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

	:pInjection: The active power injected into the bus in addition to injections from equipment terminals.  Positive sign means injection into the TopologicalNode (bus). Default: 0.0
	:qInjection: The reactive power injected into the bus in addition to injections from equipment terminals. Positive sign means injection into the TopologicalNode (bus). Default: 0.0
	:TopologicalNode: The injection flows state variables associated with the topological node. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'pInjection': [cgmesProfile.SV.value, ],
						'qInjection': [cgmesProfile.SV.value, ],
						'TopologicalNode': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, pInjection = 0.0, qInjection = 0.0, TopologicalNode = None,  ):
	
		self.pInjection = pInjection
		self.qInjection = qInjection
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=SvInjection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
