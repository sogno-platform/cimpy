from cimpy.output.SynchronousMachineDetailed import SynchronousMachineDetailed


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
	'''
	Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.     The parameters used for models expressed in time constant reactance form include:

	:rotorType: Type of rotor on physical machine. Default: 
	:modelType: Type of synchronous machine model used in Dynamic simulation applications. Default: 
	:ks: Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.  Typical Value = 0. Default: 
	:xDirectSync: Direct-axis synchronous reactance (Xd) (>= X`d). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. Typical Value = 1.8. Default: 
	:xDirectTrans: Direct-axis transient reactance (unsaturated) (X`d) (> =X``d).  Typical Value = 0.5. Default: 
	:xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X``d) (> Xl).  Typical Value = 0.2. Default: 
	:xQuadSync: Quadrature-axis synchronous reactance (Xq) (> =X`q). The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical Value = 1.6. Default: 
	:xQuadTrans: Quadrature-axis transient reactance (X`q) (> =X``q).  Typical Value = 0.3. Default: 
	:xQuadSubtrans: Quadrature-axis subtransient reactance (X``q) (> Xl).  Typical Value = 0.2. Default: 
	:tpdo: Direct-axis transient rotor time constant (T`do) (> T``do).  Typical Value = 5. Default: 
	:tppdo: Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical Value = 0.03. Default: 
	:tpqo: Quadrature-axis transient rotor time constant (T`qo) (> T``qo). Typical Value = 0.5. Default: 
	:tppqo: Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical Value = 0.03. Default: 
	:tc: Damping time constant for `Canay` reactance.  Typical Value = 0. Default: 
		'''

	cgmesProfile = SynchronousMachineDetailed.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'rotorType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'modelType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xDirectSync': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xDirectTrans': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xDirectSubtrans': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xQuadSync': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xQuadTrans': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xQuadSubtrans': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpdo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tppdo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpqo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tppqo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SynchronousMachineDetailed: \n' + SynchronousMachineDetailed.__doc__ 

	def __init__(self, rotorType = , modelType = , ks = , xDirectSync = , xDirectTrans = , xDirectSubtrans = , xQuadSync = , xQuadTrans = , xQuadSubtrans = , tpdo = , tppdo = , tpqo = , tppqo = , tc = ,  *args, **kw_args):
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
