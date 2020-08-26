from cimpy.output.SynchronousMachineDynamics import SynchronousMachineDynamics


class SynchronousMachineDetailed(SynchronousMachineDynamics):
	'''
	All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The several variations differ in the following ways:   It is not necessary for each simulation tool to have separate models for each of the model types.  The same model can often be used for several types by alternative logic within the model.  Also, differences in saturation representation may not result in significant model performance differences so model substitutions are often acceptable.

	:saturationFactorQAxis: Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value = 0.02. Default: 
	:saturationFactor120QAxis: Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).  Typical Value = 0.12. Default: 
	:efdBaseRatio: Ratio of Efd bases of exciter and generator models.  Typical Value = 1. Default: 
	:ifdBaseType: Excitation base system mode.  Typical Value = ifag. Default: 
	:ifdBaseValue: Ifd base current if .ifdBaseType = other. Not needed if .ifdBaseType not = other.   Unit = A.  Typical Value = 0. Default: 
		'''

	cgmesProfile = SynchronousMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'saturationFactorQAxis': [cgmesProfile.DY.value, ],
						'saturationFactor120QAxis': [cgmesProfile.DY.value, ],
						'efdBaseRatio': [cgmesProfile.DY.value, ],
						'ifdBaseType': [cgmesProfile.DY.value, ],
						'ifdBaseValue': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SynchronousMachineDynamics: \n' + SynchronousMachineDynamics.__doc__ 

	def __init__(self, saturationFactorQAxis = , saturationFactor120QAxis = , efdBaseRatio = , ifdBaseType = , ifdBaseValue = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.saturationFactorQAxis = saturationFactorQAxis
		self.saturationFactor120QAxis = saturationFactor120QAxis
		self.efdBaseRatio = efdBaseRatio
		self.ifdBaseType = ifdBaseType
		self.ifdBaseValue = ifdBaseValue
		
	def __str__(self):
		str = 'class=SynchronousMachineDetailed\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
