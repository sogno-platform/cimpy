from .IdentifiedObject import IdentifiedObject


class WindAeroTwoDimIEC(IdentifiedObject):
	'''
	Two-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.3.

	:dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (<i>dp</i><i><sub>omega</sub></i>). It is a type-dependent parameter. Default: 0.0
	:dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (<i>dp</i><i><sub>theta</sub></i>). It is a type-dependent parameter. Default: 0.0
	:dpv1: Partial derivative (<i>dp</i><i><sub>v1</sub></i>). It is a type-dependent parameter. Default: 0.0
	:omegazero: Rotor speed if the wind turbine is not derated (<i>omega</i><i><sub>0</sub></i>). It is a type-dependent parameter. Default: 0.0
	:pavail: Available aerodynamic power (<i>p</i><i><sub>avail</sub></i><i>)</i>. It is a case-dependent parameter. Default: 0.0
	:thetazero: Pitch angle if the wind turbine is not derated (<i>theta</i><i><sub>0</sub></i>). It is a case-dependent parameter. Default: 0.0
	:thetav2: Blade angle at twice rated wind speed (<i>theta</i><i><sub>v2</sub></i>). It is a type-dependent parameter. Default: 0.0
	:WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dpomega': [cgmesProfile.DY.value, ],
						'dptheta': [cgmesProfile.DY.value, ],
						'dpv1': [cgmesProfile.DY.value, ],
						'omegazero': [cgmesProfile.DY.value, ],
						'pavail': [cgmesProfile.DY.value, ],
						'thetazero': [cgmesProfile.DY.value, ],
						'thetav2': [cgmesProfile.DY.value, ],
						'WindTurbineType3IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpomega = 0.0, dptheta = 0.0, dpv1 = 0.0, omegazero = 0.0, pavail = 0.0, thetazero = 0.0, thetav2 = 0.0, WindTurbineType3IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpomega = dpomega
		self.dptheta = dptheta
		self.dpv1 = dpv1
		self.omegazero = omegazero
		self.pavail = pavail
		self.thetazero = thetazero
		self.thetav2 = thetav2
		self.WindTurbineType3IEC = WindTurbineType3IEC
		
	def __str__(self):
		str = 'class=WindAeroTwoDimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
