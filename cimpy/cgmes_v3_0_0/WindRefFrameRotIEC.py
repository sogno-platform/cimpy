from .IdentifiedObject import IdentifiedObject


class WindRefFrameRotIEC(IdentifiedObject):
	'''
	Reference frame rotation model. Reference: IEC 61400-27-1:2015, 5.6.3.5.

	:tpll: Time constant for PLL first order filter model (<i>T</i><i><sub>PLL</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:upll1: Voltage below which the angle of the voltage is filtered and possibly also frozen (<i>u</i><i><sub>PLL1</sub></i>). It is a type-dependent parameter. Default: 0.0
	:upll2: Voltage (<i>u</i><i><sub>PLL2</sub></i>) below which the angle of the voltage is frozen if <i>u</i><i><sub>PLL2</sub></i><sub> </sub>is smaller or equal to <i>u</i><i><sub>PLL1</sub></i> . It is a type-dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reference frame rotation model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tpll': [cgmesProfile.DY.value, ],
						'upll1': [cgmesProfile.DY.value, ],
						'upll2': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, tpll = 0, upll1 = 0.0, upll2 = 0.0, WindTurbineType3or4IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tpll = tpll
		self.upll1 = upll1
		self.upll2 = upll2
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		
	def __str__(self):
		str = 'class=WindRefFrameRotIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
