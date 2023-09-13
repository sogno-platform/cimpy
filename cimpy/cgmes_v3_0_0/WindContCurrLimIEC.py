from .IdentifiedObject import IdentifiedObject


class WindContCurrLimIEC(IdentifiedObject):
	'''
	Current limitation model.  The current limitation model combines the physical limits and the control limits. Reference: IEC 61400-27-1:2015, 5.6.5.8.

	:imax: Maximum continuous current at the wind turbine terminals (<i>i</i><i><sub>max</sub></i>). It is a type-dependent parameter. Default: 0.0
	:imaxdip: Maximum current during voltage dip at the wind turbine terminals (<i>i</i><i><sub>maxdip</sub></i>). It is a project-dependent parameter. Default: 0.0
	:kpqu: Partial derivative of reactive current limit (<i>K</i><i><sub>pqu</sub></i>) versus voltage. It is a type-dependent parameter. Default: 0.0
	:mdfslim: Limitation of type 3 stator current (<i>M</i><i><sub>DFSLim</sub></i>). <i>M</i><i><sub>DFSLim</sub></i><sub> </sub>= 1 for wind turbines type 4. It is a type-dependent parameter. false= total current limitation (0 in the IEC model) true=stator current limitation (1 in the IEC model). Default: False
	:mqpri: Prioritisation of Q control during UVRT (<i>M</i><i><sub>qpri</sub></i>). It is a project-dependent parameter. true = reactive power priority (1 in the IEC model) false = active power priority (0 in the IEC model). Default: False
	:tufiltcl: Voltage measurement filter time constant (<i>T</i><i><sub>ufiltcl</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:upqumax: Wind turbine voltage in the operation point where zero reactive current can be delivered (<i>u</i><i><sub>pqumax</sub></i>). It is a type-dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this wind control current limitation model is associated. Default: None
	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this current control limitation model. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'imax': [cgmesProfile.DY.value, ],
						'imaxdip': [cgmesProfile.DY.value, ],
						'kpqu': [cgmesProfile.DY.value, ],
						'mdfslim': [cgmesProfile.DY.value, ],
						'mqpri': [cgmesProfile.DY.value, ],
						'tufiltcl': [cgmesProfile.DY.value, ],
						'upqumax': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, imax = 0.0, imaxdip = 0.0, kpqu = 0.0, mdfslim = False, mqpri = False, tufiltcl = 0, upqumax = 0.0, WindTurbineType3or4IEC = None, WindDynamicsLookupTable = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.imax = imax
		self.imaxdip = imaxdip
		self.kpqu = kpqu
		self.mdfslim = mdfslim
		self.mqpri = mqpri
		self.tufiltcl = tufiltcl
		self.upqumax = upqumax
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		
	def __str__(self):
		str = 'class=WindContCurrLimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
