from cimpy.cgmes_v2_4_15_flat.AsynchronousMachineDynamics import AsynchronousMachineDynamics


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
	'''
	The parameters used for models expressed in time constant reactance form include:

	:xs: Synchronous reactance (Xs) (>= X').  Typical Value = 1.8. Default: 0.0
	:xp: Transient reactance (unsaturated) (X') (>=X'').  Typical Value = 0.5. Default: 0.0
	:xpp: Subtransient reactance (unsaturated) (X'') (> Xl).  Typical Value = 0.2. Default: 0.0
	:tpo: Transient rotor time constant (T'o) (> T''o).  Typical Value = 5. Default: 0.0
	:tppo: Subtransient rotor time constant (T''o) (> 0).  Typical Value = 0.03. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'xs': [cgmesProfile.DY.value, ],
						'xp': [cgmesProfile.DY.value, ],
						'xpp': [cgmesProfile.DY.value, ],
						'tpo': [cgmesProfile.DY.value, ],
						'tppo': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class AsynchronousMachineDynamics: \n' + AsynchronousMachineDynamics.__doc__ 

	def __init__(self, xs = 0.0, xp = 0.0, xpp = 0.0, tpo = 0.0, tppo = 0.0,  *args, **kw_args):
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
