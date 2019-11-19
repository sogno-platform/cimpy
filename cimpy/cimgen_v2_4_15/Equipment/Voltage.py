from cimpy.cimgen_v2_4_15.Base import Base


class Voltage(Base):
	'''
	Electrical voltage, can be both AC and DC.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	reference_dict = { 'StateVariablesVersion': ['value','unit','multiplier', ],
					'SteadyStateHypothesisVersion': ['value','unit','multiplier', ],
					 } 

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Voltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
