from .IdentifiedObject import IdentifiedObject


class WindProtectionIEC(IdentifiedObject):
	'''
	The grid protection model includes protection against over- and under-voltage, and against over- and under-frequency. Reference: IEC 61400-27-1:2015, 5.6.6.

	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this grid protection model. Default: "list"
	:dfimax: Maximum rate of change of frequency (<i>dF</i><i><sub>max</sub></i>). It is a type-dependent parameter. Default: 0.0
	:fover: Wind turbine over frequency protection activation threshold (<i>f</i><i><sub>over</sub></i>). It is a project-dependent parameter. Default: 0.0
	:funder: Wind turbine under frequency protection activation threshold (<i>f</i><i><sub>under</sub></i>). It is a project-dependent parameter. Default: 0.0
	:mzc: Zero crossing measurement mode (<i>Mzc</i>).  It is a type-dependent parameter.  true = WT protection system uses zero crossings to detect frequency (1 in the IEC model) false = WT protection system does not use zero crossings to detect frequency (0 in the IEC model). Default: False
	:tfma: Time interval of moving average window (<i>TfMA</i>) (&gt;= 0).  It is a type-dependent parameter. Default: 0
	:uover: Wind turbine over voltage protection activation threshold (<i>u</i><i><sub>over</sub></i>). It is a project-dependent parameter. Default: 0.0
	:uunder: Wind turbine under voltage protection activation threshold (<i>u</i><i><sub>under</sub></i>). It is a project-dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this wind turbine protection model is associated. Default: None
	:WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind turbine protection model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						'dfimax': [cgmesProfile.DY.value, ],
						'fover': [cgmesProfile.DY.value, ],
						'funder': [cgmesProfile.DY.value, ],
						'mzc': [cgmesProfile.DY.value, ],
						'tfma': [cgmesProfile.DY.value, ],
						'uover': [cgmesProfile.DY.value, ],
						'uunder': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindDynamicsLookupTable = "list", dfimax = 0.0, fover = 0.0, funder = 0.0, mzc = False, tfma = 0, uover = 0.0, uunder = 0.0, WindTurbineType3or4IEC = None, WindTurbineType1or2IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.dfimax = dfimax
		self.fover = fover
		self.funder = funder
		self.mzc = mzc
		self.tfma = tfma
		self.uover = uover
		self.uunder = uunder
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindTurbineType1or2IEC = WindTurbineType1or2IEC
		
	def __str__(self):
		str = 'class=WindProtectionIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
