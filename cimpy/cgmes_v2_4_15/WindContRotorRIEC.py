from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class WindContRotorRIEC(IdentifiedObject):
	'''
	Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

	:kirr: Integral gain in rotor resistance PI controller (). It is type dependent parameter. Default: 
	:komegafilt: Filter gain for generator speed measurement (K). It is type dependent parameter. Default: 
	:kpfilt: Filter gain for power measurement (). It is type dependent parameter. Default: 
	:kprr: Proportional gain in rotor resistance PI controller (). It is type dependent parameter. Default: 
	:rmax: Maximum rotor resistance (). It is type dependent parameter. Default: 
	:rmin: Minimum rotor resistance (). It is type dependent parameter. Default: 
	:tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 
	:tpfilt: Filter time constant for power measurement (). It is type dependent parameter. Default: 
	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model. Default: 
	:WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kirr': [cgmesProfile.DY.value, ],
						'komegafilt': [cgmesProfile.DY.value, ],
						'kpfilt': [cgmesProfile.DY.value, ],
						'kprr': [cgmesProfile.DY.value, ],
						'rmax': [cgmesProfile.DY.value, ],
						'rmin': [cgmesProfile.DY.value, ],
						'tomegafilt': [cgmesProfile.DY.value, ],
						'tpfilt': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						'WindGenTurbineType2IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, kirr = , komegafilt = , kpfilt = , kprr = , rmax = , rmin = , tomegafilt = , tpfilt = , WindDynamicsLookupTable = , WindGenTurbineType2IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kirr = kirr
		self.komegafilt = komegafilt
		self.kpfilt = kpfilt
		self.kprr = kprr
		self.rmax = rmax
		self.rmin = rmin
		self.tomegafilt = tomegafilt
		self.tpfilt = tpfilt
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
		
	def __str__(self):
		str = 'class=WindContRotorRIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
