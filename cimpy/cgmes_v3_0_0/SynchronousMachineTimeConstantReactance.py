from .SynchronousMachineDetailed import SynchronousMachineDetailed


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
	'''
	Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.   Parameter details: <ol> 	<li>The "p" in the time-related attribute names is a substitution for a "prime" in the usual parameter notation, e.g. tpdo refers to <i>T'do</i>.</li> 	<li>The parameters used for models expressed in time constant reactance form include:</li> </ol> - RotatingMachine.ratedS (<i>MVAbase</i>); - RotatingMachineDynamics.damping (<i>D</i>); - RotatingMachineDynamics.inertia (<i>H</i>); - RotatingMachineDynamics.saturationFactor (<i>S1</i>); - RotatingMachineDynamics.saturationFactor120 (<i>S12</i>); - RotatingMachineDynamics.statorLeakageReactance (<i>Xl</i>); - RotatingMachineDynamics.statorResistance (<i>Rs</i>); - SynchronousMachineTimeConstantReactance.ks (<i>Ks</i>); - SynchronousMachineDetailed.saturationFactorQAxis (<i>S1q</i>); - SynchronousMachineDetailed.saturationFactor120QAxis (<i>S12q</i>); - SynchronousMachineDetailed.efdBaseRatio; - SynchronousMachineDetailed.ifdBaseType; - .xDirectSync (<i>Xd</i>); - .xDirectTrans (<i>X'd</i>); - .xDirectSubtrans (<i>X''d</i>); - .xQuadSync (<i>Xq</i>); - .xQuadTrans (<i>X'q</i>); - .xQuadSubtrans (<i>X''q</i>); - .tpdo (<i>T'do</i>); - .tppdo (<i>T''do</i>); - .tpqo (<i>T'qo</i>); - .tppqo (<i>T''qo</i>); - .tc.

	:rotorType: Type of rotor on physical machine. Default: None
	:modelType: Type of synchronous machine model used in dynamic simulation applications. Default: None
	:ks: Saturation loading correction factor (<i>Ks</i>) (&gt;= 0).  Used only by type J model.  Typical value = 0. Default: 0.0
	:xDirectSync: Direct-axis synchronous reactance (<i>Xd</i>) (&gt;= SynchronousMachineTimeConstantReactance.xDirectTrans). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed.  Typical value = 1,8. Default: 0.0
	:xDirectTrans: Direct-axis transient reactance (unsaturated) (<i>X`d</i>) (&gt;= SynchronousMachineTimeConstantReactance.xDirectSubtrans).  Typical value = 0,5. Default: 0.0
	:xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (<i>X``d</i>) (&gt; RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2. Default: 0.0
	:xQuadSync: Quadrature-axis synchronous reactance (<i>Xq</i>) (&gt;= SynchronousMachineTimeConstantReactance.xQuadTrans). The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical value = 1,6. Default: 0.0
	:xQuadTrans: Quadrature-axis transient reactance (<i>X`q</i>) (&gt;= SynchronousMachineTimeConstantReactance.xQuadSubtrans).  Typical value = 0,3. Default: 0.0
	:xQuadSubtrans: Quadrature-axis subtransient reactance (<i>X``q</i>) (&gt; RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2. Default: 0.0
	:tpdo: Direct-axis transient rotor time constant (<i>T`do</i>) (&gt; SynchronousMachineTimeConstantReactance.tppdo).  Typical value = 5. Default: 0
	:tppdo: Direct-axis subtransient rotor time constant (<i>T``do</i>) (&gt; 0).  Typical value = 0,03. Default: 0
	:tpqo: Quadrature-axis transient rotor time constant (<i>T`qo</i>) (&gt; SynchronousMachineTimeConstantReactance.tppqo). Typical value = 0,5. Default: 0
	:tppqo: Quadrature-axis subtransient rotor time constant (<i>T``qo</i>) (&gt; 0). Typical value = 0,03. Default: 0
	:tc: Damping time constant for `Canay` reactance (&gt;= 0).  Typical value = 0. Default: 0
		'''

	cgmesProfile = SynchronousMachineDetailed.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'rotorType': [cgmesProfile.DY.value, ],
						'modelType': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'xDirectSync': [cgmesProfile.DY.value, ],
						'xDirectTrans': [cgmesProfile.DY.value, ],
						'xDirectSubtrans': [cgmesProfile.DY.value, ],
						'xQuadSync': [cgmesProfile.DY.value, ],
						'xQuadTrans': [cgmesProfile.DY.value, ],
						'xQuadSubtrans': [cgmesProfile.DY.value, ],
						'tpdo': [cgmesProfile.DY.value, ],
						'tppdo': [cgmesProfile.DY.value, ],
						'tpqo': [cgmesProfile.DY.value, ],
						'tppqo': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SynchronousMachineDetailed: \n' + SynchronousMachineDetailed.__doc__ 

	def __init__(self, rotorType = None, modelType = None, ks = 0.0, xDirectSync = 0.0, xDirectTrans = 0.0, xDirectSubtrans = 0.0, xQuadSync = 0.0, xQuadTrans = 0.0, xQuadSubtrans = 0.0, tpdo = 0, tppdo = 0, tpqo = 0, tppqo = 0, tc = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.rotorType = rotorType
		self.modelType = modelType
		self.ks = ks
		self.xDirectSync = xDirectSync
		self.xDirectTrans = xDirectTrans
		self.xDirectSubtrans = xDirectSubtrans
		self.xQuadSync = xQuadSync
		self.xQuadTrans = xQuadTrans
		self.xQuadSubtrans = xQuadSubtrans
		self.tpdo = tpdo
		self.tppdo = tppdo
		self.tpqo = tpqo
		self.tppqo = tppqo
		self.tc = tc
		
	def __str__(self):
		str = 'class=SynchronousMachineTimeConstantReactance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
