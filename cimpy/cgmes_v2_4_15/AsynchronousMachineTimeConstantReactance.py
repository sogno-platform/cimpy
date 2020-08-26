from cimpy.output.AsynchronousMachineDynamics import AsynchronousMachineDynamics


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
	'''
	The parameters used for models expressed in time constant reactance form include:

	:xs: Synchronous reactance (Xs) (>= X`).  Typical Value = 1.8. Default: 
	:xp: Transient reactance (unsaturated) (X`) (>=X``).  Typical Value = 0.5. Default: 
	:xpp: Subtransient reactance (unsaturated) (X``) (> Xl).  Typical Value = 0.2. Default: 
	:tpo: Transient rotor time constant (T`o) (> T``o).  Typical Value = 5. Default: 
	:tppo: Subtransient rotor time constant (T``o) (> 0).  Typical Value = 0.03. Default: 
		'''

	cgmesProfile = AsynchronousMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'xs': [cgmesProfile.DY.value, ],
						'xp': [cgmesProfile.DY.value, ],
						'xpp': [cgmesProfile.DY.value, ],
						'tpo': [cgmesProfile.DY.value, ],
						'tppo': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class AsynchronousMachineDynamics: \n' + AsynchronousMachineDynamics.__doc__ 

	def __init__(self, xs = , xp = , xpp = , tpo = , tppo = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.xs = xs
		self.xp = xp
		self.xpp = xpp
		self.tpo = tpo
		self.tppo = tppo
		
	def __str__(self):
		str = 'class=AsynchronousMachineTimeConstantReactance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
