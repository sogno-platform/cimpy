from cimpy.cgmes_v2_4_15_flat.SynchronousMachineDetailed import SynchronousMachineDetailed


class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
	'''
	The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit diagram for the direct and quadrature axes.    =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  =  +   =  +  *  / (+ )  =  +  **  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * ( + )  = ( + ) / ( * )  = ( *  +  *  +  * )/ ( *  * ( + ) Same equations using CIM attributes from SynchronousMachineTimeConstantReactance class on left of = sign and SynchronousMachineEquivalentCircuit class on right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd / (xad + xfd) xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d) xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+ x1q) xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q / (xaq * x1q + xaq * x2q + x1q * x2q)  tpdo = (xad + xfd) / (2*pi*nominal frequency * rfd) tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*nominal frequency * r1d * (xad + xfd) tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q) tppqo = (xaq * x1q + xaq * x2q + x1q * x2q)/ (2*pi*nominal frequency * r2q * (xaq + x1q).  Are only valid for a simplified model where "Canay" reactance is zero.

	:xad: D-axis mutual reactance. Default: 0.0
	:rfd: Field winding resistance. Default: 0.0
	:xfd: Field winding leakage reactance. Default: 0.0
	:r1d: D-axis damper 1 winding resistance. Default: 0.0
	:x1d: D-axis damper 1 winding leakage reactance. Default: 0.0
	:xf1d: Differential mutual ("Canay") reactance. Default: 0.0
	:xaq: Q-axis mutual reactance. Default: 0.0
	:r1q: Q-axis damper 1 winding resistance. Default: 0.0
	:x1q: Q-axis damper 1 winding leakage reactance. Default: 0.0
	:r2q: Q-axis damper 2 winding resistance. Default: 0.0
	:x2q: Q-axis damper 2 winding leakage reactance. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'xad': [cgmesProfile.DY.value, ],
						'rfd': [cgmesProfile.DY.value, ],
						'xfd': [cgmesProfile.DY.value, ],
						'r1d': [cgmesProfile.DY.value, ],
						'x1d': [cgmesProfile.DY.value, ],
						'xf1d': [cgmesProfile.DY.value, ],
						'xaq': [cgmesProfile.DY.value, ],
						'r1q': [cgmesProfile.DY.value, ],
						'x1q': [cgmesProfile.DY.value, ],
						'r2q': [cgmesProfile.DY.value, ],
						'x2q': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class SynchronousMachineDetailed: \n' + SynchronousMachineDetailed.__doc__ 

	def __init__(self, xad = 0.0, rfd = 0.0, xfd = 0.0, r1d = 0.0, x1d = 0.0, xf1d = 0.0, xaq = 0.0, r1q = 0.0, x1q = 0.0, r2q = 0.0, x2q = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.xad = xad
		self.rfd = rfd
		self.xfd = xfd
		self.r1d = r1d
		self.x1d = x1d
		self.xf1d = xf1d
		self.xaq = xaq
		self.r1q = r1q
		self.x1q = x1q
		self.r2q = r2q
		self.x2q = x2q
		
	def __str__(self):
		str = 'class=SynchronousMachineEquivalentCircuit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
