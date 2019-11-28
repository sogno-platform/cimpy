from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class WindContCurrLimIEC(IdentifiedObject):
	'''
	Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard 61400-27-1 Section 6.6.5.7.

	:imax: Maximum continuous current at the wind turbine terminals (). It is type dependent parameter. Default: 0.0
	:imaxdip: Maximum current during voltage dip at the wind turbine terminals (). It is project dependent parameter. Default: 0.0
	:mdfslim: Limitation of type 3 stator current  ():  - false=0: total current limitation,  - true=1: stator current limitation).  It is type dependent parameter. Default: False
	:mqpri: Prioritisation of q control during LVRT (): - true = 1: reactive power priority, - false = 0: active power priority.  It is project dependent parameter. Default: False
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this wind control current limitation model is associated. Default: None
	:WindDynamicsLookupTable: The current control limitation model with which this wind dynamics lookup table is associated. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'imax': [cgmesProfile.DY.value, ],
						'imaxdip': [cgmesProfile.DY.value, ],
						'mdfslim': [cgmesProfile.DY.value, ],
						'mqpri': [cgmesProfile.DY.value, ],
						'tufilt': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, imax = 0.0, imaxdip = 0.0, mdfslim = False, mqpri = False, tufilt = 0.0, WindTurbineType3or4IEC = None, WindDynamicsLookupTable = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.imax = imax
		self.imaxdip = imaxdip
		self.mdfslim = mdfslim
		self.mqpri = mqpri
		self.tufilt = tufilt
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		
	def __str__(self):
		str = 'class=WindContCurrLimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
