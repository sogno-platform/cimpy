from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class WindContPType4bIEC(IdentifiedObject):
	'''
	P control model Type 4B.  Reference: IEC Standard 61400-27-1 Section 6.6.5.5.

	:dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0
	:tpaero: Time constant in aerodynamic power response (). It is type dependent parameter. Default: 0.0
	:tpord: Time constant in power order lag (). It is type dependent parameter. Default: 0.0
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 0.0
	:WindTurbineType4bIEC: Wind turbine type 4B model with which this wind control P type 4B model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dpmax': [cgmesProfile.DY.value, ],
						'tpaero': [cgmesProfile.DY.value, ],
						'tpord': [cgmesProfile.DY.value, ],
						'tufilt': [cgmesProfile.DY.value, ],
						'WindTurbineType4bIEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpmax = 0.0, tpaero = 0.0, tpord = 0.0, tufilt = 0.0, WindTurbineType4bIEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpmax = dpmax
		self.tpaero = tpaero
		self.tpord = tpord
		self.tufilt = tufilt
		self.WindTurbineType4bIEC = WindTurbineType4bIEC
		
	def __str__(self):
		str = 'class=WindContPType4bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
