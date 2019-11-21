from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class WindPlantReactiveControlIEC(IdentifiedObject):
	'''
	Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.  Reference: IEC Standard 61400-27-1 Annex E.

	:WindPlantIEC: Wind plant model with which this wind reactive control is associated. Default: None
	:kiwpx: Plant Q controller integral gain (). It is type dependent parameter. Default: 0.0
	:kpwpx: Plant Q controller proportional gain (). It is type dependent parameter. Default: 0.0
	:kwpqu: Plant voltage control droop (). It is project dependent parameter. Default: 0.0
	:mwppf: Power factor control modes selector (). Used only if mwpu is set to false. true = 1: power factor control false = 0: reactive power control. It is project dependent parameter. Default: False
	:mwpu: Reactive power control modes selector (). true = 1: voltage control false = 0: reactive power control. It is project dependent parameter. Default: False
	:twppfilt: Filter time constant for active power measurement (). It is type dependent parameter. Default: 0.0
	:twpqfilt: Filter time constant for reactive power measurement (). It is type dependent parameter. Default: 0.0
	:twpufilt: Filter time constant for voltage measurement (). It is type dependent parameter. Default: 0.0
	:txft: Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 0.0
	:txfv: Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 0.0
	:uwpqdip: Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0
	:xrefmax: Maximum  ( or delta ) request from the plant controller (). It is project dependent parameter. Default: 0.0
	:xrefmin: Minimum  ( or delta) request from the plant controller (). It is project dependent parameter. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindPlantIEC': [cgmesProfile.DY.value, ],
						'kiwpx': [cgmesProfile.DY.value, ],
						'kpwpx': [cgmesProfile.DY.value, ],
						'kwpqu': [cgmesProfile.DY.value, ],
						'mwppf': [cgmesProfile.DY.value, ],
						'mwpu': [cgmesProfile.DY.value, ],
						'twppfilt': [cgmesProfile.DY.value, ],
						'twpqfilt': [cgmesProfile.DY.value, ],
						'twpufilt': [cgmesProfile.DY.value, ],
						'txft': [cgmesProfile.DY.value, ],
						'txfv': [cgmesProfile.DY.value, ],
						'uwpqdip': [cgmesProfile.DY.value, ],
						'xrefmax': [cgmesProfile.DY.value, ],
						'xrefmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindPlantIEC = None, kiwpx = 0.0, kpwpx = 0.0, kwpqu = 0.0, mwppf = False, mwpu = False, twppfilt = 0.0, twpqfilt = 0.0, twpufilt = 0.0, txft = 0.0, txfv = 0.0, uwpqdip = 0.0, xrefmax = 0.0, xrefmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindPlantIEC = WindPlantIEC
		self.kiwpx = kiwpx
		self.kpwpx = kpwpx
		self.kwpqu = kwpqu
		self.mwppf = mwppf
		self.mwpu = mwpu
		self.twppfilt = twppfilt
		self.twpqfilt = twpqfilt
		self.twpufilt = twpufilt
		self.txft = txft
		self.txfv = txfv
		self.uwpqdip = uwpqdip
		self.xrefmax = xrefmax
		self.xrefmin = xrefmin
		
	def __str__(self):
		str = 'class=WindPlantReactiveControlIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
