from cimpy.cgmes_v2_4_15.TapChangerTablePoint import TapChangerTablePoint


class RatioTapChangerTablePoint(TapChangerTablePoint):
	'''
	Describes each tap step in the ratio tap changer tabular curve.

	:RatioTapChangerTable: Points of this table. Default: None
		'''

	cgmesProfile = TapChangerTablePoint.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'RatioTapChangerTable': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TapChangerTablePoint: \n' + TapChangerTablePoint.__doc__ 

	def __init__(self, RatioTapChangerTable = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RatioTapChangerTable = RatioTapChangerTable
		
	def __str__(self):
		str = 'class=RatioTapChangerTablePoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
