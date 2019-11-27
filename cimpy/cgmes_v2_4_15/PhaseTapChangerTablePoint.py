from cimpy.cgmes_v2_4_15.TapChangerTablePoint import TapChangerTablePoint


class PhaseTapChangerTablePoint(TapChangerTablePoint):
	'''
	Describes each tap step in the phase tap changer tabular curve.

	:PhaseTapChangerTable: The table of this point. Default: None
	:angle: The angle difference in degrees. Default: 0.0
		'''

	cgmesProfile = TapChangerTablePoint.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'PhaseTapChangerTable': [cgmesProfile.EQ.value, ],
						'angle': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TapChangerTablePoint: \n' + TapChangerTablePoint.__doc__ 

	def __init__(self, PhaseTapChangerTable = None, angle = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PhaseTapChangerTable = PhaseTapChangerTable
		self.angle = angle
		
	def __str__(self):
		str = 'class=PhaseTapChangerTablePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
