from cimpy.cgmes_v2_4_15.AsynchronousMachineDynamics import AsynchronousMachineDynamics


class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
	'''
	The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes, with two equivalent rotor windings in each axis.      =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * (+ ) Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of = sign and AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm + RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1) tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2 * (xm + xlr1).

	:xm: Magnetizing reactance. Default: 0.0
	:rr1: Damper 1 winding resistance. Default: 0.0
	:xlr1: Damper 1 winding leakage reactance. Default: 0.0
	:rr2: Damper 2 winding resistance. Default: 0.0
	:xlr2: Damper 2 winding leakage reactance. Default: 0.0
		'''

	cgmesProfile = AsynchronousMachineDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'xm': [cgmesProfile.DY.value, ],
						'rr1': [cgmesProfile.DY.value, ],
						'xlr1': [cgmesProfile.DY.value, ],
						'rr2': [cgmesProfile.DY.value, ],
						'xlr2': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class AsynchronousMachineDynamics: \n' + AsynchronousMachineDynamics.__doc__ 

	def __init__(self, xm = 0.0, rr1 = 0.0, xlr1 = 0.0, rr2 = 0.0, xlr2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.xm = xm
		self.rr1 = rr1
		self.xlr1 = xlr1
		self.rr2 = rr2
		self.xlr2 = xlr2
		
	def __str__(self):
		str = 'class=AsynchronousMachineEquivalentCircuit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
