from cimpy.cgmes_v2_4_15.Base import Base


class Resistance(Base):
	'''
	Resistance (real part of impedance).

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	reference_dict = { 'SteadyStateHypothesisVersion': ['value','unit','multiplier', ],
					 } 

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Resistance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
