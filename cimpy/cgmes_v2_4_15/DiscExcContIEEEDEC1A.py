from cimpy.output.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
	'''
	The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.  Reference: IEEE Standard 421.5-2005 Section 12.2.

	:vtlmt: Voltage reference ().  Typical Value = 1.1. Default: 
	:vomax: Limiter ().  Typical Value = 0.3. Default: 
	:vomin: Limiter ().  Typical Value = 0.1. Default: 
	:ketl: Terminal voltage limiter gain ().  Typical Value = 47. Default: 
	:vtc: Terminal voltage level reference ().  Typical Value = 0.95. Default: 
	:val: Regulator voltage reference ().  Typical Value = 5.5. Default: 
	:esc: Speed change reference ().  Typical Value = 0.0015. Default: 
	:kan: Discontinuous controller gain ().  Typical Value = 400. Default: 
	:tan: Discontinuous controller time constant ().  Typical Value = 0.08. Default: 
	:tw5: DEC washout time constant ().  Typical Value = 5. Default: 
	:vsmax: Limiter ().  Typical Value = 0.2. Default: 
	:vsmin: Limiter ().  Typical Value = -0.066. Default: 
	:td: Time constant ().  Typical Value = 0.03. Default: 
	:tl1: Time constant ().  Typical Value = 0.025. Default: 
	:tl2: Time constant ().  Typical Value = 1.25. Default: 
	:vtm: Voltage limits ().  Typical Value = 1.13. Default: 
	:vtn: Voltage limits ().  Typical Value = 1.12. Default: 
	:vanmax: Limiter for Van (). Default: 
		'''

	cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtlmt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vomax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vomin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ketl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'val': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'esc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kan': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tan': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'td': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tl1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tl2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vtn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vanmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n' + DiscontinuousExcitationControlDynamics.__doc__ 

	def __init__(self, vtlmt = , vomax = , vomin = , ketl = , vtc = , val = , esc = , kan = , tan = , tw5 = , vsmax = , vsmin = , td = , tl1 = , tl2 = , vtm = , vtn = , vanmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vtlmt = vtlmt
		self.vomax = vomax
		self.vomin = vomin
		self.ketl = ketl
		self.vtc = vtc
		self.val = val
		self.esc = esc
		self.kan = kan
		self.tan = tan
		self.tw5 = tw5
		self.vsmax = vsmax
		self.vsmin = vsmin
		self.td = td
		self.tl1 = tl1
		self.tl2 = tl2
		self.vtm = vtm
		self.vtn = vtn
		self.vanmax = vanmax
		
	def __str__(self):
		str = 'class=DiscExcContIEEEDEC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
