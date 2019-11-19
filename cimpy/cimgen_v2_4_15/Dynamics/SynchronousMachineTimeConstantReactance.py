from cimpy.cimgen_v2_4_15.Dynamics.SynchronousMachineDetailed import SynchronousMachineDetailed


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
	'''
	Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.     The parameters used for models expressed in time constant reactance form include:

	:rotorType: Type of rotor on physical machine. Default: None
	:modelType: Type of synchronous machine model used in Dynamic simulation applications. Default: None
	:ks: Saturation loading correction factor (Ks) (&gt;= 0).  Used only by Type J model.  Typical Value = 0. Default: 0.0
	:xDirectSync: Direct-axis synchronous reactance (Xd) (&gt;= X'd). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. Typical Value = 1.8. Default: 0.0
	:xDirectTrans: Direct-axis transient reactance (unsaturated) (X'd) (&gt; =X''d).  Typical Value = 0.5. Default: 0.0
	:xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X''d) (&gt; Xl).  Typical Value = 0.2. Default: 0.0
	:xQuadSync: Quadrature-axis synchronous reactance (Xq) (&gt; =X'q). The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical Value = 1.6. Default: 0.0
	:xQuadTrans: Quadrature-axis transient reactance (X'q) (&gt; =X''q).  Typical Value = 0.3. Default: 0.0
	:xQuadSubtrans: Quadrature-axis subtransient reactance (X''q) (&gt; Xl).  Typical Value = 0.2. Default: 0.0
	:tpdo: Direct-axis transient rotor time constant (T'do) (&gt; T''do).  Typical Value = 5. Default: 0.0
	:tppdo: Direct-axis subtransient rotor time constant (T''do) (&gt; 0).  Typical Value = 0.03. Default: 0.0
	:tpqo: Quadrature-axis transient rotor time constant (T'qo) (&gt; T''qo). Typical Value = 0.5. Default: 0.0
	:tppqo: Quadrature-axis subtransient rotor time constant (T''qo) (&gt; 0). Typical Value = 0.03. Default: 0.0
	:tc: Damping time constant for &quot;Canay&quot; reactance.  Typical Value = 0. Default: 0.0
		'''

	

	__doc__ += '\n Documentation of parent class SynchronousMachineDetailed: \n' + SynchronousMachineDetailed.__doc__ 

	def __init__(self, rotorType = None, modelType = None, ks = 0.0, xDirectSync = 0.0, xDirectTrans = 0.0, xDirectSubtrans = 0.0, xQuadSync = 0.0, xQuadTrans = 0.0, xQuadSubtrans = 0.0, tpdo = 0.0, tppdo = 0.0, tpqo = 0.0, tppqo = 0.0, tc = 0.0,  *args, **kw_args):
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
