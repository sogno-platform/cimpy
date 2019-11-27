from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class RatioTapChangerTable(IdentifiedObject):
	'''
	Describes a curve for how the voltage magnitude and impedance varies with the tap step.

	:RatioTapChanger: The tap ratio table for this ratio  tap changer. Default: []
	:RatioTapChangerTablePoint: Table of this point. Default: []
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'RatioTapChanger': [cgmesProfile.EQ.value, ],
						'RatioTapChangerTablePoint': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, RatioTapChanger = [], RatioTapChangerTablePoint = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RatioTapChanger = RatioTapChanger
		self.RatioTapChangerTablePoint = RatioTapChangerTablePoint
		
	def __str__(self):
		str = 'class=RatioTapChangerTable\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
