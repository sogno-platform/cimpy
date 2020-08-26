from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST2(TurbineGovernorDynamics):
	'''
	Gas turbine model.

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 
	:w: Governor gain (1/droop) on turbine rating (W). Default: 
	:x: Governor lead time constant (X). Default: 
	:y: Governor lag time constant (Y) (>0). Default: 
	:z: Governor mode (Z). true = Droop false = ISO. Default: 
	:etd: Turbine and exhaust delay (Etd). Default: 
	:tcd: Compressor discharge time constant (Tcd). Default: 
	:trate: Turbine rating (Trate).  Unit = MW. Default: 
	:t: Fuel Control Time Constant (T). Default: 
	:tmax: Maximum Turbine limit (Tmax). Default: 
	:tmin: Minimum Turbine limit (Tmin). Default: 
	:ecr: Combustion reaction time delay (Ecr). Default: 
	:k3: Ratio of Fuel Adjustment (K3). Default: 
	:a: Valve positioner (A). Default: 
	:b: Valve positioner (B). Default: 
	:c: Valve positioner (C). Default: 
	:tf: Fuel system time constant (Tf). Default: 
	:kf: Fuel system feedback (Kf). Default: 
	:k5: Gain of radiation shield (K5). Default: 
	:k4: Gain of radiation shield (K4). Default: 
	:t3: Radiation shield time constant (T3). Default: 
	:t4: Thermocouple time constant (T4). Default: 
	:tt: Temperature controller integration rate (Tt). Default: 
	:t5: Temperature control time constant (T5). Default: 
	:af1: Exhaust temperature Parameter (Af1).  Unit = per unit temperature.  Based on temperature in degrees C. Default: 
	:bf1: (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.  Unit = per unit temperature.  Based on temperature in degrees C. Default: 
	:af2: Coefficient equal to 0.5(1-speed) (Af2). Default: 
	:bf2: Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 
	:cf2: Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K (23% fuel flow). Default: 
	:tr: Rated temperature (Tr).  Unit = [SYMBOL REMOVED]C depending on parameters Af1 and Bf1. Default: 
	:k6: Minimum fuel flow (K6). Default: 
	:tc: Temperature control (Tc).  Unit = [SYMBOL REMOVED]F or [SYMBOL REMOVED]C depending on constants Af1 and Bf1. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'w': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'x': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'y': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'z': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'etd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tcd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'trate': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ecr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'b': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'c': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'af1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'bf1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'af2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'bf2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'cf2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , w = , x = , y = , z = , etd = , tcd = , trate = , t = , tmax = , tmin = , ecr = , k3 = , a = , b = , c = , tf = , kf = , k5 = , k4 = , t3 = , t4 = , tt = , t5 = , af1 = , bf1 = , af2 = , bf2 = , cf2 = , tr = , k6 = , tc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.w = w
		self.x = x
		self.y = y
		self.z = z
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
		
	def __str__(self):
		str = 'class=GovGAST2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
