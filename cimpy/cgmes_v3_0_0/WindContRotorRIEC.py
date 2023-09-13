from .IdentifiedObject import IdentifiedObject


class WindContRotorRIEC(IdentifiedObject):
	'''
	Rotor resistance control model. Reference: IEC 61400-27-1:2015, 5.6.5.3.

	:kirr: Integral gain in rotor resistance PI controller (<i>K</i><i><sub>Irr</sub></i>). It is a type-dependent parameter. Default: 0.0
	:komegafilt: Filter gain for generator speed measurement (<i>K</i><i><sub>omegafilt</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kpfilt: Filter gain for power measurement (<i>K</i><i><sub>pfilt</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kprr: Proportional gain in rotor resistance PI controller (<i>K</i><i><sub>Prr</sub></i>). It is a type-dependent parameter. Default: 0.0
	:rmax: Maximum rotor resistance (<i>r</i><i><sub>max</sub></i>) (&gt; WindContRotorRIEC.rmin). It is a type-dependent parameter. Default: 0.0
	:rmin: Minimum rotor resistance (<i>r</i><i><sub>min</sub></i>) (&lt; WindContRotorRIEC.rmax). It is a type-dependent parameter. Default: 0.0
	:tomegafiltrr: Filter time constant for generator speed measurement (<i>T</i><i><sub>omegafiltrr</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:tpfiltrr: Filter time constant for power measurement (<i>T</i><i><sub>pfiltrr</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model. Default: "list"
	:WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kirr': [cgmesProfile.DY.value, ],
						'komegafilt': [cgmesProfile.DY.value, ],
						'kpfilt': [cgmesProfile.DY.value, ],
						'kprr': [cgmesProfile.DY.value, ],
						'rmax': [cgmesProfile.DY.value, ],
						'rmin': [cgmesProfile.DY.value, ],
						'tomegafiltrr': [cgmesProfile.DY.value, ],
						'tpfiltrr': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						'WindGenTurbineType2IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, kirr = 0.0, komegafilt = 0.0, kpfilt = 0.0, kprr = 0.0, rmax = 0.0, rmin = 0.0, tomegafiltrr = 0, tpfiltrr = 0, WindDynamicsLookupTable = "list", WindGenTurbineType2IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kirr = kirr
		self.komegafilt = komegafilt
		self.kpfilt = kpfilt
		self.kprr = kprr
		self.rmax = rmax
		self.rmin = rmin
		self.tomegafiltrr = tomegafiltrr
		self.tpfiltrr = tpfiltrr
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
		
	def __str__(self):
		str = 'class=WindContRotorRIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
