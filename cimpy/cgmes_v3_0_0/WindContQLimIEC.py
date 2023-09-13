from .IdentifiedObject import IdentifiedObject


class WindContQLimIEC(IdentifiedObject):
	'''
	Constant Q limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.9.

	:qmax: Maximum reactive power (<i>q</i><i><sub>max</sub></i>) (&gt; WindContQLimIEC.qmin). It is a type-dependent parameter. Default: 0.0
	:qmin: Minimum reactive power (<i>q</i><i><sub>min</sub></i>) (&lt; WindContQLimIEC.qmax). It is a type-dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this constant Q limitation model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'qmax': [cgmesProfile.DY.value, ],
						'qmin': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, qmax = 0.0, qmin = 0.0, WindTurbineType3or4IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.qmax = qmax
		self.qmin = qmin
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		
	def __str__(self):
		str = 'class=WindContQLimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
