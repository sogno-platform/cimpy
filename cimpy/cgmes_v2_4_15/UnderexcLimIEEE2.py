from cimpy.cgmes_v2_4_15_flat.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
	'''
	The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).

	:tuv: Voltage filter time constant (T).  Typical Value = 5. Default: 0.0
	:tup: Real power filter time constant (T).  Typical Value = 5. Default: 0.0
	:tuq: Reactive power filter time constant (T).  Typical Value = 0. Default: 0.0
	:kui: UEL integral gain (K).  Typical Value = 0.5. Default: 0.0
	:kul: UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0
	:vuimax: UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0
	:vuimin: UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0
	:kuf: UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0
	:kfb: Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0
	:tul: Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0.0
	:tu1: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
	:tu2: UEL lag time constant (T).  Typical Value = 0. Default: 0.0
	:tu3: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
	:tu4: UEL lag time constant (T).  Typical Value = 0. Default: 0.0
	:vulmax: UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0
	:vulmin: UEL output minimum limit (V).  Typical Value = 0. Default: 0.0
	:p0: Real power values for endpoints (P).  Typical Value = 0. Default: 0.0
	:q0: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0
	:p1: Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0
	:q1: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0
	:p2: Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0
	:q2: Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0
	:p3: Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0
	:q3: Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0
	:p4: Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0
	:q4: Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0
	:p5: Real power values for endpoints (P). Default: 0.0
	:q5: Reactive power values for endpoints (Q). Default: 0.0
	:p6: Real power values for endpoints (P). Default: 0.0
	:q6: Reactive power values for endpoints (Q). Default: 0.0
	:p7: Real power values for endpoints (P). Default: 0.0
	:q7: Reactive power values for endpoints (Q). Default: 0.0
	:p8: Real power values for endpoints (P). Default: 0.0
	:q8: Reactive power values for endpoints (Q). Default: 0.0
	:p9: Real power values for endpoints (P). Default: 0.0
	:q9: Reactive power values for endpoints (Q). Default: 0.0
	:p10: Real power values for endpoints (P). Default: 0.0
	:q10: Reactive power values for endpoints (Q). Default: 0.0
	:k1: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0
	:k2: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tuv': [cgmesProfile.DY.value, ],
						'tup': [cgmesProfile.DY.value, ],
						'tuq': [cgmesProfile.DY.value, ],
						'kui': [cgmesProfile.DY.value, ],
						'kul': [cgmesProfile.DY.value, ],
						'vuimax': [cgmesProfile.DY.value, ],
						'vuimin': [cgmesProfile.DY.value, ],
						'kuf': [cgmesProfile.DY.value, ],
						'kfb': [cgmesProfile.DY.value, ],
						'tul': [cgmesProfile.DY.value, ],
						'tu1': [cgmesProfile.DY.value, ],
						'tu2': [cgmesProfile.DY.value, ],
						'tu3': [cgmesProfile.DY.value, ],
						'tu4': [cgmesProfile.DY.value, ],
						'vulmax': [cgmesProfile.DY.value, ],
						'vulmin': [cgmesProfile.DY.value, ],
						'p0': [cgmesProfile.DY.value, ],
						'q0': [cgmesProfile.DY.value, ],
						'p1': [cgmesProfile.DY.value, ],
						'q1': [cgmesProfile.DY.value, ],
						'p2': [cgmesProfile.DY.value, ],
						'q2': [cgmesProfile.DY.value, ],
						'p3': [cgmesProfile.DY.value, ],
						'q3': [cgmesProfile.DY.value, ],
						'p4': [cgmesProfile.DY.value, ],
						'q4': [cgmesProfile.DY.value, ],
						'p5': [cgmesProfile.DY.value, ],
						'q5': [cgmesProfile.DY.value, ],
						'p6': [cgmesProfile.DY.value, ],
						'q6': [cgmesProfile.DY.value, ],
						'p7': [cgmesProfile.DY.value, ],
						'q7': [cgmesProfile.DY.value, ],
						'p8': [cgmesProfile.DY.value, ],
						'q8': [cgmesProfile.DY.value, ],
						'p9': [cgmesProfile.DY.value, ],
						'q9': [cgmesProfile.DY.value, ],
						'p10': [cgmesProfile.DY.value, ],
						'q10': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class UnderexcitationLimiterDynamics: \n' + UnderexcitationLimiterDynamics.__doc__ 

	def __init__(self, tuv = 0.0, tup = 0.0, tuq = 0.0, kui = 0.0, kul = 0.0, vuimax = 0.0, vuimin = 0.0, kuf = 0.0, kfb = 0.0, tul = 0.0, tu1 = 0.0, tu2 = 0.0, tu3 = 0.0, tu4 = 0.0, vulmax = 0.0, vulmin = 0.0, p0 = 0.0, q0 = 0.0, p1 = 0.0, q1 = 0.0, p2 = 0.0, q2 = 0.0, p3 = 0.0, q3 = 0.0, p4 = 0.0, q4 = 0.0, p5 = 0.0, q5 = 0.0, p6 = 0.0, q6 = 0.0, p7 = 0.0, q7 = 0.0, p8 = 0.0, q8 = 0.0, p9 = 0.0, q9 = 0.0, p10 = 0.0, q10 = 0.0, k1 = 0.0, k2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tuv = tuv
		self.tup = tup
		self.tuq = tuq
		self.kui = kui
		self.kul = kul
		self.vuimax = vuimax
		self.vuimin = vuimin
		self.kuf = kuf
		self.kfb = kfb
		self.tul = tul
		self.tu1 = tu1
		self.tu2 = tu2
		self.tu3 = tu3
		self.tu4 = tu4
		self.vulmax = vulmax
		self.vulmin = vulmin
		self.p0 = p0
		self.q0 = q0
		self.p1 = p1
		self.q1 = q1
		self.p2 = p2
		self.q2 = q2
		self.p3 = p3
		self.q3 = q3
		self.p4 = p4
		self.q4 = q4
		self.p5 = p5
		self.q5 = q5
		self.p6 = p6
		self.q6 = q6
		self.p7 = p7
		self.q7 = q7
		self.p8 = p8
		self.q8 = q8
		self.p9 = p9
		self.q9 = q9
		self.p10 = p10
		self.q10 = q10
		self.k1 = k1
		self.k2 = k2
		
	def __str__(self):
		str = 'class=UnderexcLimIEEE2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
