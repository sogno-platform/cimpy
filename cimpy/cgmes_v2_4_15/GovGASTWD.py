from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGASTWD(TurbineGovernorDynamics):
	'''
	Woodward Gas turbine governor model.

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
	:kdroop: (Kdroop). Default: 0.0
	:kp: PID Proportional gain (Kp). Default: 0.0
	:ki: Isochronous Governor Gain (Ki). Default: 0.0
	:kd: Drop Governor Gain (Kd). Default: 0.0
	:etd: Turbine and exhaust delay (Etd). Default: 0.0
	:tcd: Compressor discharge time constant (Tcd). Default: 0.0
	:trate: Turbine rating (Trate).  Unit = MW. Default: 0.0
	:t: Fuel Control Time Constant (T). Default: 0.0
	:tmax: Maximum Turbine limit (Tmax). Default: 0.0
	:tmin: Minimum Turbine limit (Tmin). Default: 0.0
	:ecr: Combustion reaction time delay (Ecr). Default: 0.0
	:k3: Ratio of Fuel Adjustment (K3). Default: 0.0
	:a: Valve positioner (). Default: 0.0
	:b: Valve positioner (). Default: 0.0
	:c: Valve positioner (). Default: 0.0
	:tf: Fuel system time constant (Tf). Default: 0.0
	:kf: Fuel system feedback (Kf). Default: 0.0
	:k5: Gain of radiation shield (K5). Default: 0.0
	:k4: Gain of radiation shield (K4). Default: 0.0
	:t3: Radiation shield time constant (T3). Default: 0.0
	:t4: Thermocouple time constant (T4). Default: 0.0
	:tt: Temperature controller integration rate (Tt). Default: 0.0
	:t5: Temperature control time constant (T5). Default: 0.0
	:af1: Exhaust temperature Parameter (Af1). Default: 0.0
	:bf1: (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr. Default: 0.0
	:af2: Coefficient equal to 0.5(1-speed) (Af2). Default: 0.0
	:bf2: Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 0.0
	:cf2: Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K(23% fuel flow). Default: 0.0
	:tr: Rated temperature (Tr). Default: 0.0
	:k6: Minimum fuel flow (K6). Default: 0.0
	:tc: Temperature control (Tc). Default: 0.0
	:td: Power transducer time constant (Td). Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'kdroop': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'etd': [cgmesProfile.DY.value, ],
						'tcd': [cgmesProfile.DY.value, ],
						'trate': [cgmesProfile.DY.value, ],
						't': [cgmesProfile.DY.value, ],
						'tmax': [cgmesProfile.DY.value, ],
						'tmin': [cgmesProfile.DY.value, ],
						'ecr': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						'b': [cgmesProfile.DY.value, ],
						'c': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'k5': [cgmesProfile.DY.value, ],
						'k4': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						'af1': [cgmesProfile.DY.value, ],
						'bf1': [cgmesProfile.DY.value, ],
						'af2': [cgmesProfile.DY.value, ],
						'bf2': [cgmesProfile.DY.value, ],
						'cf2': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'k6': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, kdroop = 0.0, kp = 0.0, ki = 0.0, kd = 0.0, etd = 0.0, tcd = 0.0, trate = 0.0, t = 0.0, tmax = 0.0, tmin = 0.0, ecr = 0.0, k3 = 0.0, a = 0.0, b = 0.0, c = 0.0, tf = 0.0, kf = 0.0, k5 = 0.0, k4 = 0.0, t3 = 0.0, t4 = 0.0, tt = 0.0, t5 = 0.0, af1 = 0.0, bf1 = 0.0, af2 = 0.0, bf2 = 0.0, cf2 = 0.0, tr = 0.0, k6 = 0.0, tc = 0.0, td = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.kdroop = kdroop
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.etd = etd
		self.tcd = tcd
		self.trate = trate
		self.t = t
		self.tmax = tmax
		self.tmin = tmin
		self.ecr = ecr
		self.k3 = k3
		self.a = a
		self.b = b
		self.c = c
		self.tf = tf
		self.kf = kf
		self.k5 = k5
		self.k4 = k4
		self.t3 = t3
		self.t4 = t4
		self.tt = tt
		self.t5 = t5
		self.af1 = af1
		self.bf1 = bf1
		self.af2 = af2
		self.bf2 = bf2
		self.cf2 = cf2
		self.tr = tr
		self.k6 = k6
		self.tc = tc
		self.td = td
		
	def __str__(self):
		str = 'class=GovGASTWD\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
