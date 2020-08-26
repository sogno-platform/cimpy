from cimpy.output.TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


class TurbLCFB1(TurbineLoadControllerDynamics):
	'''
	Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the turbine governor.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load reference governor. Typical Value = true. Default: 
	:db: Controller dead band (db).  Typical Value = 0. Default: 
	:emax: Maximum control error (Emax) (note 4).  Typical Value = 0.02. Default: 
	:fb: Frequency bias gain (Fb).  Typical Value = 0. Default: 
	:kp: Proportional gain (Kp).  Typical Value = 0. Default: 
	:ki: Integral gain (Ki).  Typical Value = 0. Default: 
	:fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false. Default: 
	:pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value = false. Default: 
	:tpelec: Power transducer time constant (Tpelec).  Typical Value = 0. Default: 
	:irmax: Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0. Default: 
	:pmwset: Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0. Default: 
		'''

	cgmesProfile = TurbineLoadControllerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'speedReferenceGovernor': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'db': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'emax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'fb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'fbf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pbf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpelec': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'irmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmwset': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineLoadControllerDynamics: \n' + TurbineLoadControllerDynamics.__doc__ 

	def __init__(self, mwbase = , speedReferenceGovernor = , db = , emax = , fb = , kp = , ki = , fbf = , pbf = , tpelec = , irmax = , pmwset = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.speedReferenceGovernor = speedReferenceGovernor
		self.db = db
		self.emax = emax
		self.fb = fb
		self.kp = kp
		self.ki = ki
		self.fbf = fbf
		self.pbf = pbf
		self.tpelec = tpelec
		self.irmax = irmax
		self.pmwset = pmwset
		
	def __str__(self):
		str = 'class=TurbLCFB1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
