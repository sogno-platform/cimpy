from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR7(ExcitationSystemDynamics):
	'''
	IVO excitation system.

	:k1: Gain (<i>K</i><i><sub>1</sub></i>).  Typical value = 1. Default: 0.0
	:a1: Lead coefficient (<i>A</i><i><sub>1</sub></i>).  Typical value = 0,5. Default: 0.0
	:a2: Lag coefficient (<i>A</i><i><sub>2</sub></i>).  Typical value = 0,5. Default: 0.0
	:t1: Lead time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
	:t2: Lag time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:vmax1: Lead-lag maximum limit (<i>Vmax1</i>) (&gt; ExcAVR7.vmin1).  Typical value = 5. Default: 0.0
	:vmin1: Lead-lag minimum limit (<i>Vmin1</i>) (&lt; ExcAVR7.vmax1).  Typical value = -5. Default: 0.0
	:k3: Gain (<i>K</i><i><sub>3</sub></i>).  Typical value = 3. Default: 0.0
	:a3: Lead coefficient (<i>A</i><i><sub>3</sub></i>).  Typical value = 0,5. Default: 0.0
	:a4: Lag coefficient (<i>A</i><i><sub>4</sub></i>).  Typical value = 0,5. Default: 0.0
	:t3: Lead time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:t4: Lag time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:vmax3: Lead-lag maximum limit (<i>Vmax3</i>) (&gt; ExcAVR7.vmin3).  Typical value = 5. Default: 0.0
	:vmin3: Lead-lag minimum limit (<i>Vmin3</i>) (&lt; ExcAVR7.vmax3).  Typical value = -5. Default: 0.0
	:k5: Gain (<i>K</i><i><sub>5</sub></i>).  Typical value = 1. Default: 0.0
	:a5: Lead coefficient (<i>A</i><i><sub>5</sub></i>).  Typical value = 0,5. Default: 0.0
	:a6: Lag coefficient (<i>A</i><i><sub>6</sub></i>).  Typical value = 0,5. Default: 0.0
	:t5: Lead time constant (<i>T</i><i><sub>5</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:t6: Lag time constant (<i>T</i><i><sub>6</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:vmax5: Lead-lag maximum limit (<i>Vmax5</i>) (&gt; ExcAVR7.vmin5).  Typical value = 5. Default: 0.0
	:vmin5: Lead-lag minimum limit (<i>Vmin5</i>) (&lt; ExcAVR7.vmax5).  Typical value = -2. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'a1': [cgmesProfile.DY.value, ],
						'a2': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'vmax1': [cgmesProfile.DY.value, ],
						'vmin1': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'a3': [cgmesProfile.DY.value, ],
						'a4': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'vmax3': [cgmesProfile.DY.value, ],
						'vmin3': [cgmesProfile.DY.value, ],
						'k5': [cgmesProfile.DY.value, ],
						'a5': [cgmesProfile.DY.value, ],
						'a6': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'vmax5': [cgmesProfile.DY.value, ],
						'vmin5': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = 0.0, a1 = 0.0, a2 = 0.0, t1 = 0, t2 = 0, vmax1 = 0.0, vmin1 = 0.0, k3 = 0.0, a3 = 0.0, a4 = 0.0, t3 = 0, t4 = 0, vmax3 = 0.0, vmin3 = 0.0, k5 = 0.0, a5 = 0.0, a6 = 0.0, t5 = 0, t6 = 0, vmax5 = 0.0, vmin5 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.vmax1 = vmax1
		self.vmin1 = vmin1
		self.k3 = k3
		self.a3 = a3
		self.a4 = a4
		self.t3 = t3
		self.t4 = t4
		self.vmax3 = vmax3
		self.vmin3 = vmin3
		self.k5 = k5
		self.a5 = a5
		self.a6 = a6
		self.t5 = t5
		self.t6 = t6
		self.vmax5 = vmax5
		self.vmin5 = vmin5
		
	def __str__(self):
		str = 'class=ExcAVR7\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
