from cimpy.output.VoltageAdjusterDynamics import VoltageAdjusterDynamics


class VAdjIEEE(VoltageAdjusterDynamics):
	'''
	The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

	:vadjf: Set high to provide a continuous raise or lower (). Default: 
	:adjslew: Rate at which output of adjuster changes ().  Unit = sec./PU.  Typical Value = 300. Default: 
	:vadjmax: Maximum output of the adjuster ().  Typical Value = 1.1. Default: 
	:vadjmin: Minimum output of the adjuster ().  Typical Value = 0.9. Default: 
	:taon: Time that adjuster pulses are on ().  Typical Value = 0.1. Default: 
	:taoff: Time that adjuster pulses are off ().  Typical Value = 0.5. Default: 
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

	def __init__(self, vadjf = , adjslew = , vadjmax = , vadjmin = , taon = , taoff = ,  *args, **kw_args):
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
