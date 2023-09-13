from .IdentifiedObject import IdentifiedObject


class WindContQPQULimIEC(IdentifiedObject):
	'''
	QP and QU limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.10.

	:tpfiltql: Power measurement filter time constant for Q capacity (<i>T</i><i><sub>pfiltql</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:tufiltql: Voltage measurement filter time constant for Q capacity (<i>T</i><i><sub>ufiltql</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this QP and QU limitation model is associated. Default: None
	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this QP and QU limitation model. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tpfiltql': [cgmesProfile.DY.value, ],
						'tufiltql': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, tpfiltql = 0, tufiltql = 0, WindTurbineType3or4IEC = None, WindDynamicsLookupTable = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tpfiltql = tpfiltql
		self.tufiltql = tufiltql
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		
	def __str__(self):
		str = 'class=WindContQPQULimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
