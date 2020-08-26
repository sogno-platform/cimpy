from cimpy.output.IdentifiedObject import IdentifiedObject


class WindContPitchAngleIEC(IdentifiedObject):
	'''
	Pitch angle control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.8.

	:dthetamax: Maximum pitch positive ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 
	:dthetamin: Maximum pitch negative ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 
	:kic: Power PI controller integration gain (). It is type dependent parameter. Default: 
	:kiomega: Speed PI controller integration gain (). It is type dependent parameter. Default: 
	:kpc: Power PI controller proportional gain (). It is type dependent parameter. Default: 
	:kpomega: Speed PI controller proportional gain (). It is type dependent parameter. Default: 
	:kpx: Pitch cross coupling gain (K). It is type dependent parameter. Default: 
	:thetamax: Maximum pitch angle (). It is type dependent parameter. Default: 
	:thetamin: Minimum pitch angle (). It is type dependent parameter. Default: 
	:ttheta: Pitch time constant (t). It is type dependent parameter. Default: 
	:WindGenTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'dthetamax': [cgmesProfile.DY.value, ],
						'dthetamin': [cgmesProfile.DY.value, ],
						'kic': [cgmesProfile.DY.value, ],
						'kiomega': [cgmesProfile.DY.value, ],
						'kpc': [cgmesProfile.DY.value, ],
						'kpomega': [cgmesProfile.DY.value, ],
						'kpx': [cgmesProfile.DY.value, ],
						'thetamax': [cgmesProfile.DY.value, ],
						'thetamin': [cgmesProfile.DY.value, ],
						'ttheta': [cgmesProfile.DY.value, ],
						'WindGenTurbineType3IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dthetamax = , dthetamin = , kic = , kiomega = , kpc = , kpomega = , kpx = , thetamax = , thetamin = , ttheta = , WindGenTurbineType3IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dthetamax = dthetamax
		self.dthetamin = dthetamin
		self.kic = kic
		self.kiomega = kiomega
		self.kpc = kpc
		self.kpomega = kpomega
		self.kpx = kpx
		self.thetamax = thetamax
		self.thetamin = thetamin
		self.ttheta = ttheta
		self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
		
	def __str__(self):
		str = 'class=WindContPitchAngleIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
