from cimpy.cgmes_v2_4_15_flat.Base import Base


class TapChangerTablePoint(Base):
	'''
	

	:b: The magnetizing branch susceptance deviation in percent of nominal value. The actual susceptance is calculated as follows: calculated magnetizing susceptance = b(nominal) * (1 + b(from this class)/100).   The b(nominal) is defined as the static magnetizing susceptance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
	:g: The magnetizing branch conductance deviation in percent of nominal value. The actual conductance is calculated as follows: calculated magnetizing conductance = g(nominal) * (1 + g(from this class)/100).   The g(nominal) is defined as the static magnetizing conductance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
	:r: The resistance deviation in percent of nominal value. The actual reactance is calculated as follows: calculated resistance = r(nominal) * (1 + r(from this class)/100).   The r(nominal) is defined as the static resistance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
	:ratio: The voltage ratio in per unit. Hence this is a value close to one. Default: 0.0
	:step: The tap step. Default: 0
	:x: The series reactance deviation in percent of nominal value. The actual reactance is calculated as follows: calculated reactance = x(nominal) * (1 + x(from this class)/100).   The x(nominal) is defined as the static series reactance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'b': [cgmesProfile.EQ.value, ],
						'g': [cgmesProfile.EQ.value, ],
						'r': [cgmesProfile.EQ.value, ],
						'ratio': [cgmesProfile.EQ.value, ],
						'step': [cgmesProfile.EQ.value, ],
						'x': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, b = 0.0, g = 0.0, r = 0.0, ratio = 0.0, step = 0, x = 0.0,  ):
	
		self.b = b
		self.g = g
		self.r = r
		self.ratio = ratio
		self.step = step
		self.x = x
		
	def __str__(self):
		str = 'class=TapChangerTablePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
