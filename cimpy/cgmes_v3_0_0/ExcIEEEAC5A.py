from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC5A(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type AC5A model. The model represents a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances.  Unlike other AC models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the DC models.  Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required. Reference: IEEE 421.5-2005, 6.5.

	:ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 400. Default: 0.0
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 7,3. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -7,3. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 0,8. Default: 0
	:kf: Excitation control system stabilizer gains (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:tf1: Excitation control system stabilizer time constant (<i>T</i><i><sub>F1</sub></i>) (&gt; 0).  Typical value = 1. Default: 0
	:tf2: Excitation control system stabilizer time constant (<i>T</i><i><sub>F2</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tf3: Excitation control system stabilizer time constant (<i>T</i><i><sub>F3</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:efd1: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD1</sub></i>) (&gt; 0).  Typical value = 5,6. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD1</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,86. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD2</sub></i>) (&gt; 0).  Typical value = 4,2. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD2</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,5. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'tf3': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0, kf = 0.0, tf1 = 0, tf2 = 0, tf3 = 0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		self.tf3 = tf3
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		
	def __str__(self):
		str = 'class=ExcIEEEAC5A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
