from .VoltageAdjusterDynamics import VoltageAdjusterDynamics


class VAdjIEEE(VoltageAdjusterDynamics):
	'''
	IEEE voltage adjuster which is used to represent the voltage adjuster in either a power factor or VAr control system. Reference: IEEE 421.5-2005, 11.1.

	:vadjf: Set high to provide a continuous raise or lower (<i>V</i><i><sub>ADJF</sub></i>). Default: 0.0
	:adjslew: Rate at which output of adjuster changes (<i>ADJ_SLEW</i>).  Unit = s / PU.  Typical value = 300. Default: 0.0
	:vadjmax: Maximum output of the adjuster (<i>V</i><i><sub>ADJMAX</sub></i>) (&gt; VAdjIEEE.vadjmin).  Typical value = 1,1. Default: 0.0
	:vadjmin: Minimum output of the adjuster (<i>V</i><i><sub>ADJMIN</sub></i>) (&lt; VAdjIEEE.vadjmax).  Typical value = 0,9. Default: 0.0
	:taon: Time that adjuster pulses are on (<i>T</i><i><sub>AON</sub></i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:taoff: Time that adjuster pulses are off (<i>T</i><i><sub>AOFF</sub></i>) (&gt;= 0).  Typical value = 0,5. Default: 0
		'''

	cgmesProfile = VoltageAdjusterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vadjf': [cgmesProfile.DY.value, ],
						'adjslew': [cgmesProfile.DY.value, ],
						'vadjmax': [cgmesProfile.DY.value, ],
						'vadjmin': [cgmesProfile.DY.value, ],
						'taon': [cgmesProfile.DY.value, ],
						'taoff': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class VoltageAdjusterDynamics: \n' + VoltageAdjusterDynamics.__doc__ 

	def __init__(self, vadjf = 0.0, adjslew = 0.0, vadjmax = 0.0, vadjmin = 0.0, taon = 0, taoff = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vadjf = vadjf
		self.adjslew = adjslew
		self.vadjmax = vadjmax
		self.vadjmin = vadjmin
		self.taon = taon
		self.taoff = taoff
		
	def __str__(self):
		str = 'class=VAdjIEEE\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
