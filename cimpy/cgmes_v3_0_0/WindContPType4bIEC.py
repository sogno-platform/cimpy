from .IdentifiedObject import IdentifiedObject


class WindContPType4bIEC(IdentifiedObject):
	'''
	P control model type 4B. Reference: IEC 61400-27-1:2015, 5.6.5.6.

	:dpmaxp4b: Maximum wind turbine power ramp rate (<i>dp</i><i><sub>maxp4B</sub></i>). It is a project-dependent parameter. Default: 0.0
	:tpaero: Time constant in aerodynamic power response (<i>T</i><i><sub>paero</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:tpordp4b: Time constant in power order lag (<i>T</i><i><sub>pordp4B</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:tufiltp4b: Voltage measurement filter time constant (<i>T</i><i><sub>ufiltp4B</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:WindTurbineType4bIEC: Wind turbine type 4B model with which this wind control P type 4B model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dpmaxp4b': [cgmesProfile.DY.value, ],
						'tpaero': [cgmesProfile.DY.value, ],
						'tpordp4b': [cgmesProfile.DY.value, ],
						'tufiltp4b': [cgmesProfile.DY.value, ],
						'WindTurbineType4bIEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpmaxp4b = 0.0, tpaero = 0, tpordp4b = 0, tufiltp4b = 0, WindTurbineType4bIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpmaxp4b = dpmaxp4b
		self.tpaero = tpaero
		self.tpordp4b = tpordp4b
		self.tufiltp4b = tufiltp4b
		self.WindTurbineType4bIEC = WindTurbineType4bIEC
		
	def __str__(self):
		str = 'class=WindContPType4bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
