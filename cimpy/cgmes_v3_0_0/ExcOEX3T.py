from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcOEX3T(ExcitationSystemDynamics):
	'''
	Modified IEEE type ST1 excitation system with semi-continuous and acting terminal voltage limiter.

	:t1: Time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0). Default: 0
	:t2: Time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0). Default: 0
	:t3: Time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0). Default: 0
	:t4: Time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0). Default: 0
	:ka: Gain (<i>K</i><i><sub>A</sub></i>). Default: 0.0
	:t5: Time constant (<i>T</i><i><sub>5</sub></i>) (&gt;= 0). Default: 0
	:t6: Time constant (<i>T</i><i><sub>6</sub></i>) (&gt;= 0). Default: 0
	:vrmax: Limiter (<i>V</i><i><sub>RMAX</sub></i>) (&gt; ExcOEX3T.vrmin). Default: 0.0
	:vrmin: Limiter (<i>V</i><i><sub>RMIN</sub></i>) (&lt; ExcOEX3T.vrmax). Default: 0.0
	:te: Time constant (<i>T</i><i><sub>E</sub></i>) (&gt;= 0). Default: 0
	:kf: Gain (<i>K</i><i><sub>F</sub></i>). Default: 0.0
	:tf: Time constant (<i>T</i><i><sub>F</sub></i>) (&gt;= 0). Default: 0
	:kc: Gain (<i>K</i><i><sub>C</sub></i>). Default: 0.0
	:kd: Gain (<i>K</i><i><sub>D</sub></i>). Default: 0.0
	:ke: Gain (<i>K</i><i><sub>E</sub></i>). Default: 0.0
	:e1: Saturation parameter (<i>E</i><i><sub>1</sub></i>). Default: 0.0
	:see1: Saturation parameter (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>1</sub></i><i>]</i>). Default: 0.0
	:e2: Saturation parameter (<i>E</i><i><sub>2</sub></i>). Default: 0.0
	:see2: Saturation parameter (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>2</sub></i><i>]</i>). Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'see1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'see2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, t1 = 0, t2 = 0, t3 = 0, t4 = 0, ka = 0.0, t5 = 0, t6 = 0, vrmax = 0.0, vrmin = 0.0, te = 0, kf = 0.0, tf = 0, kc = 0.0, kd = 0.0, ke = 0.0, e1 = 0.0, see1 = 0.0, e2 = 0.0, see2 = 0.0,  *args, **kw_args):
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
