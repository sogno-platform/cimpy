from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class WindContQIEC(IdentifiedObject):
	'''
	Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.

	:iqh1: Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 0.0
	:iqmax: Maximum reactive current injection (i). It is type dependent parameter. Default: 0.0
	:iqmin: Minimum reactive current injection (i). It is type dependent parameter. Default: 0.0
	:iqpost: Post fault reactive current injection (). It is project dependent parameter. Default: 0.0
	:kiq: Reactive power PI controller integration gain (). It is type dependent parameter. Default: 0.0
	:kiu: Voltage PI controller integration gain (). It is type dependent parameter. Default: 0.0
	:kpq: Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 0.0
	:kpu: Voltage PI controller proportional gain (). It is type dependent parameter. Default: 0.0
	:kqv: Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 0.0
	:qmax: Maximum reactive power (q). It is type dependent parameter. Default: 0.0
	:qmin: Minimum reactive power (q). It is type dependent parameter. Default: 0.0
	:rdroop: Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0
	:tiq: Time constant in reactive current lag (T). It is type dependent parameter. Default: 0.0
	:tpfilt: Power measurement filter time constant (). It is type dependent parameter. Default: 0.0
	:tpost: Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 0.0
	:tqord: Time constant in reactive power order lag (). It is type dependent parameter. Default: 0.0
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 0.0
	:udb1: Voltage dead band lower limit (). It is type dependent parameter. Default: 0.0
	:udb2: Voltage dead band upper limit (). It is type dependent parameter. Default: 0.0
	:umax: Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0
	:umin: Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 0.0
	:uqdip: Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 0.0
	:uref0: User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 0.0
	:windLVRTQcontrolModesType: Types of LVRT Q control modes (). It is project dependent parameter. Default: None
	:windQcontrolModesType: Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: None
	:xdroop: Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 0.0
	:WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: None
		'''

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
						'qmax': [cgmesProfile.DY.value, ],
						'qmin': [cgmesProfile.DY.value, ],
						'rdroop': [cgmesProfile.DY.value, ],
						'tiq': [cgmesProfile.DY.value, ],
						'tpfilt': [cgmesProfile.DY.value, ],
						'tpost': [cgmesProfile.DY.value, ],
						'tqord': [cgmesProfile.DY.value, ],
						'tufilt': [cgmesProfile.DY.value, ],
						'udb1': [cgmesProfile.DY.value, ],
						'udb2': [cgmesProfile.DY.value, ],
						'umax': [cgmesProfile.DY.value, ],
						'umin': [cgmesProfile.DY.value, ],
						'uqdip': [cgmesProfile.DY.value, ],
						'uref0': [cgmesProfile.DY.value, ],
						'windLVRTQcontrolModesType': [cgmesProfile.DY.value, ],
						'windQcontrolModesType': [cgmesProfile.DY.value, ],
						'xdroop': [cgmesProfile.DY.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, iqh1 = 0.0, iqmax = 0.0, iqmin = 0.0, iqpost = 0.0, kiq = 0.0, kiu = 0.0, kpq = 0.0, kpu = 0.0, kqv = 0.0, qmax = 0.0, qmin = 0.0, rdroop = 0.0, tiq = 0.0, tpfilt = 0.0, tpost = 0.0, tqord = 0.0, tufilt = 0.0, udb1 = 0.0, udb2 = 0.0, umax = 0.0, umin = 0.0, uqdip = 0.0, uref0 = 0.0, windLVRTQcontrolModesType = None, windQcontrolModesType = None, xdroop = 0.0, WindTurbineType3or4IEC = None,  *args, **kw_args):
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
		self.qmax = qmax
		self.qmin = qmin
		self.rdroop = rdroop
		self.tiq = tiq
		self.tpfilt = tpfilt
		self.tpost = tpost
		self.tqord = tqord
		self.tufilt = tufilt
		self.udb1 = udb1
		self.udb2 = udb2
		self.umax = umax
		self.umin = umin
		self.uqdip = uqdip
		self.uref0 = uref0
		self.windLVRTQcontrolModesType = windLVRTQcontrolModesType
		self.windQcontrolModesType = windQcontrolModesType
		self.xdroop = xdroop
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		
	def __str__(self):
		str = 'class=WindContQIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
