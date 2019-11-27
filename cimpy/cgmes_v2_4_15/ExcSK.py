from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSK(ExcitationSystemDynamics):
	'''
	Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is used, there cannot be a separate underexcitation limiter or VAr controller model.

	:efdmax: Field voltage clipping limit (Efdmax). Default: 0.0
	:efdmin: Field voltage clipping limit (Efdmin). Default: 0.0
	:emax: Maximum field voltage output (Emax).  Typical Value = 20. Default: 0.0
	:emin: Minimum field voltage output (Emin).  Typical Value = -20. Default: 0.0
	:k: Gain (K).  Typical Value = 1. Default: 0.0
	:k1: Parameter of underexcitation limit (K1).  Typical Value = 0.1364. Default: 0.0
	:k2: Parameter of underexcitation limit (K2).  Typical Value = -0.3861. Default: 0.0
	:kc: PI controller gain (Kc).  Typical Value = 70. Default: 0.0
	:kce: Rectifier regulation factor (Kce).  Typical Value = 0. Default: 0.0
	:kd: Exciter internal reactance (Kd).  Typical Value = 0. Default: 0.0
	:kgob: P controller gain (Kgob).  Typical Value = 10. Default: 0.0
	:kp: PI controller gain (Kp).  Typical Value = 1. Default: 0.0
	:kqi: PI controller gain of integral component (Kqi).  Typical Value = 0. Default: 0.0
	:kqob: Rate of rise of the reactive power (Kqob). Default: 0.0
	:kqp: PI controller gain (Kqp).  Typical Value = 0. Default: 0.0
	:nq: Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001. Default: 0.0
	:qconoff: Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary voltage control is OFF. Typical Value = false. Default: False
	:qz: Desired value (setpoint) of reactive power, manual setting (Qz). Default: 0.0
	:remote: Selector to apply automatic calculation in secondary controller model. true = automatic calculation is activated false = manual set is active; the use of desired value of reactive power (Qz) is required. Typical Value = true. Default: False
	:sbase: Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259. Default: 0.0
	:tc: PI controller phase lead time constant (Tc).  Typical Value = 8. Default: 0.0
	:te: Time constant of gain block (Te).  Typical Value = 0.1. Default: 0.0
	:ti: PI controller phase lead time constant (Ti).  Typical Value = 2. Default: 0.0
	:tp: Time constant (Tp).  Typical Value = 0.1. Default: 0.0
	:tr: Voltage transducer time constant (Tr).  Typical Value = 0.01. Default: 0.0
	:uimax: Maximum error (Uimax).  Typical Value = 10. Default: 0.0
	:uimin: Minimum error (UImin).  Typical Value = -10. Default: 0.0
	:urmax: Maximum controller output (URmax).  Typical Value = 10. Default: 0.0
	:urmin: Minimum controller output (URmin).  Typical Value = -10. Default: 0.0
	:vtmax: Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05. Default: 0.0
	:vtmin: Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95. Default: 0.0
	:yp: Maximum output (Yp).  Minimum output = 0.  Typical Value = 1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'efdmin': [cgmesProfile.DY.value, ],
						'emax': [cgmesProfile.DY.value, ],
						'emin': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kce': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'kgob': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'kqi': [cgmesProfile.DY.value, ],
						'kqob': [cgmesProfile.DY.value, ],
						'kqp': [cgmesProfile.DY.value, ],
						'nq': [cgmesProfile.DY.value, ],
						'qconoff': [cgmesProfile.DY.value, ],
						'qz': [cgmesProfile.DY.value, ],
						'remote': [cgmesProfile.DY.value, ],
						'sbase': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'ti': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'uimax': [cgmesProfile.DY.value, ],
						'uimin': [cgmesProfile.DY.value, ],
						'urmax': [cgmesProfile.DY.value, ],
						'urmin': [cgmesProfile.DY.value, ],
						'vtmax': [cgmesProfile.DY.value, ],
						'vtmin': [cgmesProfile.DY.value, ],
						'yp': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, efdmax = 0.0, efdmin = 0.0, emax = 0.0, emin = 0.0, k = 0.0, k1 = 0.0, k2 = 0.0, kc = 0.0, kce = 0.0, kd = 0.0, kgob = 0.0, kp = 0.0, kqi = 0.0, kqob = 0.0, kqp = 0.0, nq = 0.0, qconoff = False, qz = 0.0, remote = False, sbase = 0.0, tc = 0.0, te = 0.0, ti = 0.0, tp = 0.0, tr = 0.0, uimax = 0.0, uimin = 0.0, urmax = 0.0, urmin = 0.0, vtmax = 0.0, vtmin = 0.0, yp = 0.0,  *args, **kw_args):
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
