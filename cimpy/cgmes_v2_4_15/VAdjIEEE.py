from cimpy.cgmes_v2_4_15.VoltageAdjusterDynamics import VoltageAdjusterDynamics


class VAdjIEEE(VoltageAdjusterDynamics):
	'''
	The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

	:vadjf: Set high to provide a continuous raise or lower (). Default: 0.0
	:adjslew: Rate at which output of adjuster changes ().  Unit = sec./PU.  Typical Value = 300. Default: 0.0
	:vadjmax: Maximum output of the adjuster ().  Typical Value = 1.1. Default: 0.0
	:vadjmin: Minimum output of the adjuster ().  Typical Value = 0.9. Default: 0.0
	:taon: Time that adjuster pulses are on ().  Typical Value = 0.1. Default: 0.0
	:taoff: Time that adjuster pulses are off ().  Typical Value = 0.5. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class VoltageAdjusterDynamics: \n' + VoltageAdjusterDynamics.__doc__ 

	def __init__(self, vadjf = 0.0, adjslew = 0.0, vadjmax = 0.0, vadjmin = 0.0, taon = 0.0, taoff = 0.0,  *args, **kw_args):
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
