from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class Curve(IdentifiedObject):
	'''
	A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.

	:curveStyle: The style or shape of the curve. Default: None
	:xUnit: The X-axis units of measure. Default: None
	:y1Unit: The Y1-axis units of measure. Default: None
	:y2Unit: The Y2-axis units of measure. Default: None
	:CurveDatas: The curve of  this curve data point. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'curveStyle': [cgmesProfile.EQ.value, ],
						'xUnit': [cgmesProfile.EQ.value, ],
						'y1Unit': [cgmesProfile.EQ.value, ],
						'y2Unit': [cgmesProfile.EQ.value, ],
						'CurveDatas': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, curveStyle = None, xUnit = None, y1Unit = None, y2Unit = None, CurveDatas = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.curveStyle = curveStyle
		self.xUnit = xUnit
		self.y1Unit = y1Unit
		self.y2Unit = y2Unit
		self.CurveDatas = CurveDatas
		
	def __str__(self):
		str = 'class=Curve\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
