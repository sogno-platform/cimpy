from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
	'''
	The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit diagram for the direct- and quadrature- axes, with two equivalent rotor windings in each axis.   Equations for conversion between equivalent circuit and time constant reactance forms: <i>Xs</i> = <i>Xm</i> + <i>Xl</i> <i>X'</i> = <i>Xl</i> + <i>Xm</i> x <i>Xlr1 </i>/ (<i>Xm </i>+ <i>Xlr1</i>) <i>X''</i> = <i>Xl</i> + <i>Xm</i> x <i>Xlr1</i> x <i>Xlr2</i> / (<i>Xm</i> x <i>Xlr1</i> + <i>Xm</i> x <i>Xlr2</i> + <i>Xlr1</i> x <i>Xlr2</i>) <i>T'o</i> = (<i>Xm</i> + <i>Xlr1</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>Rr1</i>) <i>T''o</i> = (<i>Xm</i> x <i>Xlr1</i> + <i>Xm</i> x <i>Xlr2</i> + <i>Xlr1</i> x <i>Xlr2</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>Rr2</i> x (<i>Xm</i> + <i>Xlr1</i>) Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of "=" and AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm + RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 x xlr2 / (xm x xlr1 + xm x xlr2 + xlr1 x xlr2) tpo = (xm + xlr1) / (2 x pi x nominal frequency x rr1) tppo = (xm x xlr1 + xm x xlr2 + xlr1 x xlr2) / (2 x pi x nominal frequency x rr2 x (xm + xlr1).

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

	serializationProfile = {}

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
