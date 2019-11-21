from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class WindProtectionIEC(IdentifiedObject):
	'''
	The grid protection model includes protection against over and under voltage, and against over and under frequency.  Reference: IEC Standard 614000-27-1 Section 6.6.6.

	:fover: Set of wind turbine over frequency protection levels (). It is project dependent parameter. Default: 0.0
	:funder: Set of wind turbine under frequency protection levels (). It is project dependent parameter. Default: 0.0
	:tfover: Set of corresponding wind turbine over frequency protection disconnection times (). It is project dependent parameter. Default: 0.0
	:tfunder: Set of corresponding wind turbine under frequency protection disconnection times (). It is project dependent parameter. Default: 0.0
	:tuover: Set of corresponding wind turbine over voltage protection disconnection times (). It is project dependent parameter. Default: 0.0
	:tuunder: Set of corresponding wind turbine under voltage protection disconnection times (). It is project dependent parameter. Default: 0.0
	:uover: Set of wind turbine over voltage protection levels (). It is project dependent parameter. Default: 0.0
	:uunder: Set of wind turbine under voltage protection levels (). It is project dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind generator type 3 or 4 model with which this wind turbine protection model is associated. Default: None
	:WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind turbine protection model is associated. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'fover': [cgmesProfile.DY.value, ],
						'funder': [cgmesProfile.DY.value, ],
						'tfover': [cgmesProfile.DY.value, ],
						'tfunder': [cgmesProfile.DY.value, ],
						'tuover': [cgmesProfile.DY.value, ],
						'tuunder': [cgmesProfile.DY.value, ],
						'uover': [cgmesProfile.DY.value, ],
						'uunder': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2IEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, fover = 0.0, funder = 0.0, tfover = 0.0, tfunder = 0.0, tuover = 0.0, tuunder = 0.0, uover = 0.0, uunder = 0.0, WindTurbineType3or4IEC = None, WindTurbineType1or2IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fover = fover
		self.funder = funder
		self.tfover = tfover
		self.tfunder = tfunder
		self.tuover = tuover
		self.tuunder = tuunder
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
