from cimpy.cgmes_v2_4_15.TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


class TurbLCFB1(TurbineLoadControllerDynamics):
	'''
	Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the turbine governor.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
	:speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load reference governor. Typical Value = true. Default: False
	:db: Controller dead band (db).  Typical Value = 0. Default: 0.0
	:emax: Maximum control error (Emax) (note 4).  Typical Value = 0.02. Default: 0.0
	:fb: Frequency bias gain (Fb).  Typical Value = 0. Default: 0.0
	:kp: Proportional gain (Kp).  Typical Value = 0. Default: 0.0
	:ki: Integral gain (Ki).  Typical Value = 0. Default: 0.0
	:fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false. Default: False
	:pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value = false. Default: False
	:tpelec: Power transducer time constant (Tpelec).  Typical Value = 0. Default: 0.0
	:irmax: Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0. Default: 0.0
	:pmwset: Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0. Default: 0.0
		'''

	cgmesProfile = TurbineLoadControllerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'speedReferenceGovernor': [cgmesProfile.DY.value, ],
						'db': [cgmesProfile.DY.value, ],
						'emax': [cgmesProfile.DY.value, ],
						'fb': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'fbf': [cgmesProfile.DY.value, ],
						'pbf': [cgmesProfile.DY.value, ],
						'tpelec': [cgmesProfile.DY.value, ],
						'irmax': [cgmesProfile.DY.value, ],
						'pmwset': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineLoadControllerDynamics: \n' + TurbineLoadControllerDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, speedReferenceGovernor = False, db = 0.0, emax = 0.0, fb = 0.0, kp = 0.0, ki = 0.0, fbf = False, pbf = False, tpelec = 0.0, irmax = 0.0, pmwset = 0.0,  *args, **kw_args):
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
