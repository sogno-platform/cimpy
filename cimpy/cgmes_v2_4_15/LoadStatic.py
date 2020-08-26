from cimpy.output.IdentifiedObject import IdentifiedObject


class LoadStatic(IdentifiedObject):
	'''
	General static load model representing the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.

	:LoadAggregate: Aggregate load to which this aggregate static load belongs. Default: 
	:staticLoadModelType: Type of static load model.  Typical Value = constantZ. Default: 
	:kp1: First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ. Default: 
	:kp2: Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ. Default: 
	:kp3: Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ. Default: 
	:kp4: Frequency coefficient for active power (Kp4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 
	:ep1: First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential. Default: 
	:ep2: Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential. Default: 
	:ep3: Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential. Default: 
	:kpf: Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ. Default: 
	:kq1: First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ. Default: 
	:kq2: Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ. Default: 
	:kq3: Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ. Default: 
	:kq4: Frequency coefficient for reactive power (Kq4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 
	:eq1: First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential. Default: 
	:eq2: Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential. Default: 
	:eq3: Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential. Default: 
	:kqf: Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'LoadAggregate': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'staticLoadModelType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ep1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ep2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ep3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kq1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kq2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kq3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kq4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eq1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eq2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eq3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kqf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, LoadAggregate = , staticLoadModelType = , kp1 = , kp2 = , kp3 = , kp4 = , ep1 = , ep2 = , ep3 = , kpf = , kq1 = , kq2 = , kq3 = , kq4 = , eq1 = , eq2 = , eq3 = , kqf = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadAggregate = LoadAggregate
		self.staticLoadModelType = staticLoadModelType
		self.kp1 = kp1
		self.kp2 = kp2
		self.kp3 = kp3
		self.kp4 = kp4
		self.ep1 = ep1
		self.ep2 = ep2
		self.ep3 = ep3
		self.kpf = kpf
		self.kq1 = kq1
		self.kq2 = kq2
		self.kq3 = kq3
		self.kq4 = kq4
		self.eq1 = eq1
		self.eq2 = eq2
		self.eq3 = eq3
		self.kqf = kqf
		
	def __str__(self):
		str = 'class=LoadStatic\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
