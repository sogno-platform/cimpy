from .IdentifiedObject import IdentifiedObject


class WindContQIEC(IdentifiedObject):
	'''
	Q control model. Reference: IEC 61400-27-1:2015, 5.6.5.7.

	:iqh1: Maximum reactive current injection during dip (<i>i</i><i><sub>qh1</sub></i>). It is a type-dependent parameter. Default: 0.0
	:iqmax: Maximum reactive current injection (<i>i</i><i><sub>qmax</sub></i>) (&gt; WindContQIEC.iqmin). It is a type-dependent parameter. Default: 0.0
	:iqmin: Minimum reactive current injection (<i>i</i><i><sub>qmin</sub></i>) (&lt; WindContQIEC.iqmax). It is a type-dependent parameter. Default: 0.0
	:iqpost: Post fault reactive current injection (<i>i</i><i><sub>qpost</sub></i>). It is a project-dependent parameter. Default: 0.0
	:kiq: Reactive power PI controller integration gain (<i>K</i><i><sub>I,q</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kiu: Voltage PI controller integration gain (<i>K</i><i><sub>I,u</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kpq: Reactive power PI controller proportional gain (<i>K</i><i><sub>P,q</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kpu: Voltage PI controller proportional gain (<i>K</i><i><sub>P,u</sub></i>). It is a type-dependent parameter. Default: 0.0
	:kqv: Voltage scaling factor for UVRT current (<i>K</i><i><sub>qv</sub></i>). It is a project-dependent parameter. Default: 0.0
	:tpfiltq: Power measurement filter time constant (<i>T</i><i><sub>pfiltq</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:rdroop: Resistive component of voltage drop impedance (<i>r</i><i><sub>droop</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0.0
	:tufiltq: Voltage measurement filter time constant (<i>T</i><i><sub>ufiltq</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:tpost: Length of time period where post fault reactive power is injected (<i>T</i><i><sub>post</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
	:tqord: Time constant in reactive power order lag (<i>T</i><i><sub>qord</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
	:udb1: Voltage deadband lower limit (<i>u</i><i><sub>db1</sub></i>). It is a type-dependent parameter. Default: 0.0
	:udb2: Voltage deadband upper limit (<i>u</i><i><sub>db2</sub></i>). It is a type-dependent parameter. Default: 0.0
	:umax: Maximum voltage in voltage PI controller integral term (<i>u</i><i><sub>max</sub></i>) (&gt; WindContQIEC.umin). It is a type-dependent parameter. Default: 0.0
	:umin: Minimum voltage in voltage PI controller integral term (<i>u</i><i><sub>min</sub></i>) (&lt; WindContQIEC.umax). It is a type-dependent parameter. Default: 0.0
	:uqdip: Voltage threshold for UVRT detection in Q control (<i>u</i><i><sub>qdip</sub></i>). It is a type-dependent parameter. Default: 0.0
	:uref0: User-defined bias in voltage reference (<i>u</i><i><sub>ref0</sub></i>). It is a case-dependent parameter. Default: 0.0
	:windQcontrolModesType: Types of general wind turbine Q control modes (<i>M</i><i><sub>qG</sub></i>).  It is a project-dependent parameter. Default: None
	:windUVRTQcontrolModesType: Types of UVRT Q control modes (<i>M</i><i><sub>qUVRT</sub></i>). It is a project-dependent parameter. Default: None
	:xdroop: Inductive component of voltage drop impedance (<i>x</i><i><sub>droop</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reactive control model is associated. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'iqh1': [cgmesProfile.DY.value, ],
						'iqmax': [cgmesProfile.DY.value, ],
						'iqmin': [cgmesProfile.DY.value, ],
						'iqpost': [cgmesProfile.DY.value, ],
						'kiq': [cgmesProfile.DY.value, ],
						'kiu': [cgmesProfile.DY.value, ],
						'kpq': [cgmesProfile.DY.value, ],
						'kpu': [cgmesProfile.DY.value, ],
						'kqv': [cgmesProfile.DY.value, ],
						'tpfiltq': [cgmesProfile.DY.value, ],
						'rdroop': [cgmesProfile.DY.value, ],
						'tufiltq': [cgmesProfile.DY.value, ],
						'tpost': [cgmesProfile.DY.value, ],
						'tqord': [cgmesProfile.DY.value, ],
						'udb1': [cgmesProfile.DY.value, ],
						'udb2': [cgmesProfile.DY.value, ],
						'umax': [cgmesProfile.DY.value, ],
						'umin': [cgmesProfile.DY.value, ],
						'uqdip': [cgmesProfile.DY.value, ],
						'uref0': [cgmesProfile.DY.value, ],
						'windQcontrolModesType': [cgmesProfile.DY.value, ],
						'windUVRTQcontrolModesType': [cgmesProfile.DY.value, ],
						'xdroop': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, iqh1 = 0.0, iqmax = 0.0, iqmin = 0.0, iqpost = 0.0, kiq = 0.0, kiu = 0.0, kpq = 0.0, kpu = 0.0, kqv = 0.0, tpfiltq = 0, rdroop = 0.0, tufiltq = 0, tpost = 0, tqord = 0, udb1 = 0.0, udb2 = 0.0, umax = 0.0, umin = 0.0, uqdip = 0.0, uref0 = 0.0, windQcontrolModesType = None, windUVRTQcontrolModesType = None, xdroop = 0.0, WindTurbineType3or4IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.iqh1 = iqh1
		self.iqmax = iqmax
		self.iqmin = iqmin
		self.iqpost = iqpost
		self.kiq = kiq
		self.kiu = kiu
		self.kpq = kpq
		self.kpu = kpu
		self.kqv = kqv
		self.tpfiltq = tpfiltq
		self.rdroop = rdroop
		self.tufiltq = tufiltq
		self.tpost = tpost
		self.tqord = tqord
		self.udb1 = udb1
		self.udb2 = udb2
		self.umax = umax
		self.umin = umin
		self.uqdip = uqdip
		self.uref0 = uref0
		self.windQcontrolModesType = windQcontrolModesType
		self.windUVRTQcontrolModesType = windUVRTQcontrolModesType
		self.xdroop = xdroop
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		
	def __str__(self):
		str = 'class=WindContQIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
