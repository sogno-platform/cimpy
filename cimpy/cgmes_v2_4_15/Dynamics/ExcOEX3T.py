from cimpy.cgmes_v2_4_15.Dynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcOEX3T(ExcitationSystemDynamics):
	'''
	Modified IEEE Type ST1 Excitation System with semi-continuous and acting terminal voltage limiter.

	:t1: Time constant (T). Default: 0.0
	:t2: Time constant (T). Default: 0.0
	:t3: Time constant (T). Default: 0.0
	:t4: Time constant (T). Default: 0.0
	:ka: Gain (K). Default: 0.0
	:t5: Time constant (T). Default: 0.0
	:t6: Time constant (T). Default: 0.0
	:vrmax: Limiter (V). Default: 0.0
	:vrmin: Limiter (V). Default: 0.0
	:te: Time constant (T). Default: 0.0
	:kf: Gain (K). Default: 0.0
	:tf: Time constant (T). Default: 0.0
	:kc: Gain (K). Default: 0.0
	:kd: Gain (K). Default: 0.0
	:ke: Gain (K). Default: 0.0
	:e1: Saturation parameter (E). Default: 0.0
	:see1: Saturation parameter (S(E)). Default: 0.0
	:e2: Saturation parameter (E). Default: 0.0
	:see2: Saturation parameter (S(E)). Default: 0.0
		'''

	

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, ka = 0.0, t5 = 0.0, t6 = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0.0, kf = 0.0, tf = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, e1 = 0.0, see1 = 0.0, e2 = 0.0, see2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.ka = ka
		self.t5 = t5
		self.t6 = t6
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.e1 = e1
		self.see1 = see1
		self.e2 = e2
		self.see2 = see2
		
	def __str__(self):
		str = 'class=ExcOEX3T\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
