from cimpy.cgmes_v2_4_15_flat.Base import Base


class SvTapStep(Base):
	'''
	State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.

	:position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined by the related tap changer model and normally is constrained to be within the range of minimum and maximum tap positions. Default: 0.0
	:TapChanger: The tap changer associated with the tap step state. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'position': [cgmesProfile.SV.value, ],
						'TapChanger': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, position = 0.0, TapChanger = None,  ):
	
		self.position = position
		self.TapChanger = TapChanger
		
	def __str__(self):
		str = 'class=SvTapStep\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
