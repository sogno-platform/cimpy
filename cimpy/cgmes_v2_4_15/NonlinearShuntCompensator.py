from cimpy.output.ShuntCompensator import ShuntCompensator


class NonlinearShuntCompensator(ShuntCompensator):
	'''
	A non linear shunt compensator has bank or section admittance values that differs.

	:NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator. Default: 
		'''

	cgmesProfile = ShuntCompensator.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'NonlinearShuntCompensatorPoints': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ShuntCompensator: \n' + ShuntCompensator.__doc__ 

	def __init__(self, NonlinearShuntCompensatorPoints = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.NonlinearShuntCompensatorPoints = NonlinearShuntCompensatorPoints
		
	def __str__(self):
		str = 'class=NonlinearShuntCompensator\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
