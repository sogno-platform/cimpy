from cimpy.output.IdentifiedObject import IdentifiedObject


class WindAeroLinearIEC(IdentifiedObject):
	'''
	The linearised aerodynamic model.    Reference: IEC Standard 614000-27-1 Section 6.6.1.2.

	:dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (). It is case dependent parameter. Default: 
	:dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (). It is case dependent parameter. Default: 
	:omegazero: Rotor speed if the wind turbine is not derated (). It is case dependent parameter. Default: 
	:pavail: Available aerodynamic power (). It is case dependent parameter. Default: 
	:thetazero: Pitch angle if the wind turbine is not derated (). It is case dependent parameter. Default: 
	:WindGenTurbineType3IEC: Wind generator type 3 model with which this wind aerodynamic model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dpomega': [cgmesProfile.DY.value, ],
						'dptheta': [cgmesProfile.DY.value, ],
						'omegazero': [cgmesProfile.DY.value, ],
						'pavail': [cgmesProfile.DY.value, ],
						'thetazero': [cgmesProfile.DY.value, ],
						'WindGenTurbineType3IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpomega = , dptheta = , omegazero = , pavail = , thetazero = , WindGenTurbineType3IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpomega = dpomega
		self.dptheta = dptheta
		self.omegazero = omegazero
		self.pavail = pavail
		self.thetazero = thetazero
		self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
		
	def __str__(self):
		str = 'class=WindAeroLinearIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
