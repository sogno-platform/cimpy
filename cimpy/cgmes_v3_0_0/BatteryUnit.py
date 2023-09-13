from .PowerElectronicsUnit import PowerElectronicsUnit


class BatteryUnit(PowerElectronicsUnit):
	'''
	An electrochemical energy storage device.

	:batteryState: The current state of the battery (charging, full, etc.). Default: None
	:storedE: Amount of energy currently stored. The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE. Default: 0.0
	:ratedE: Full energy storage capacity of the battery. The attribute shall be a positive value. Default: 0.0
		'''

	cgmesProfile = PowerElectronicsUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'batteryState': [cgmesProfile.SSH.value, ],
						'storedE': [cgmesProfile.SSH.value, ],
						'ratedE': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerElectronicsUnit: \n' + PowerElectronicsUnit.__doc__ 

	def __init__(self, batteryState = None, storedE = 0.0, ratedE = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.batteryState = batteryState
		self.storedE = storedE
		self.ratedE = ratedE
		
	def __str__(self):
		str = 'class=BatteryUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
