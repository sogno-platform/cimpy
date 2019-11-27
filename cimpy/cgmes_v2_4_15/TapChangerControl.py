from cimpy.cgmes_v2_4_15.RegulatingControl import RegulatingControl


class TapChangerControl(RegulatingControl):
	'''
	Describes behavior specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

	:TapChanger: The regulating control scheme in which this tap changer participates. Default: []
		'''

	cgmesProfile = RegulatingControl.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'TapChanger': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingControl: \n' + RegulatingControl.__doc__ 

	def __init__(self, TapChanger = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TapChanger = TapChanger
		
	def __str__(self):
		str = 'class=TapChangerControl\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
