from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSK(ExcitationSystemDynamics):
	'''
	Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.

	:efdmax: Field voltage clipping limit (Efdmax). Default: 
	:efdmin: Field voltage clipping limit (Efdmin). Default: 
	:emax: Maximum field voltage output (Emax).  Typical Value = 20. Default: 
	:emin: Minimum field voltage output (Emin).  Typical Value = -20. Default: 
	:k: Gain (K).  Typical Value = 1. Default: 
	:k1: Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 
	:k2: Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 
	:kc: PI controller gain (Kc).  Typical Value = 70. Default: 
	:kce: Rectifier regulation factor (Kce).  Typical Value = 0. Default: 
	:kd: Exciter internal reactance (Kd).  Typical Value = 0. Default: 
	:kgob: P controller gain (Kgob).  Typical Value = 10. Default: 
	:kp: PI controller gain (Kp).  Typical Value = 1. Default: 
	:kqi: PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 
	:kqob: Rate of rise of the reactive power (Kqob). Default: 
	:kqp: PI controller gain (Kqp).  Typical Value = 0. Default: 
	:nq: Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 
	:qconoff: Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: 
	:qz: Desired value (setpoint) of reactive power, manual setting (Qz). Default: 
	:remote: Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: 
	:sbase: Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 
	:tc: PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 
	:te: Time constant of gain block (Te).  Typical Value = 0.1. Default: 
	:ti: PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 
	:tp: Time constant (Tp).  Typical Value = 0.1. Default: 
	:tr: Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 
	:uimax: Maximum error (Uimax).  Typical Value = 10. Default: 
	:uimin: Minimum error (UImin).  Typical Value = -10. Default: 
	:urmax: Maximum controller output (URmax).  Typical Value = 10. Default: 
	:urmin: Minimum controller output (URmin).  Typical Value = -10. Default: 
	:vtmax: Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 
	:vtmin: Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 
	:yp: Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'emax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'emin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kce': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kgob': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kqi': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kqob': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kqp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'nq': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qconoff': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qz': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'remote': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'sbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ti': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uimax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uimin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'urmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'urmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'yp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, efdmax = , efdmin = , emax = , emin = , k = , k1 = , k2 = , kc = , kce = , kd = , kgob = , kp = , kqi = , kqob = , kqp = , nq = , qconoff = , qz = , remote = , sbase = , tc = , te = , ti = , tp = , tr = , uimax = , uimin = , urmax = , urmin = , vtmax = , vtmin = , yp = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.efdmax = efdmax
		self.efdmin = efdmin
		self.emax = emax
		self.emin = emin
		self.k = k
		self.k1 = k1
		self.k2 = k2
		self.kc = kc
		self.kce = kce
		self.kd = kd
		self.kgob = kgob
		self.kp = kp
		self.kqi = kqi
		self.kqob = kqob
		self.kqp = kqp
		self.nq = nq
		self.qconoff = qconoff
		self.qz = qz
		self.remote = remote
		self.sbase = sbase
		self.tc = tc
		self.te = te
		self.ti = ti
		self.tp = tp
		self.tr = tr
		self.uimax = uimax
		self.uimin = uimin
		self.urmax = urmax
		self.urmin = urmin
		self.vtmax = vtmax
		self.vtmin = vtmin
		self.yp = yp
		
	def __str__(self):
		str = 'class=ExcSK\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
