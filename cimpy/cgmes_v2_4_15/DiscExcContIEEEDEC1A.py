from cimpy.cgmes_v2_4_15_flat.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
	'''
	The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.  Reference: IEEE Standard 421.5-2005 Section 12.2.

	:vtlmt: Voltage reference ().  Typical Value = 1.1. Default: 0.0
	:vomax: Limiter ().  Typical Value = 0.3. Default: 0.0
	:vomin: Limiter ().  Typical Value = 0.1. Default: 0.0
	:ketl: Terminal voltage limiter gain ().  Typical Value = 47. Default: 0.0
	:vtc: Terminal voltage level reference ().  Typical Value = 0.95. Default: 0.0
	:val: Regulator voltage reference ().  Typical Value = 5.5. Default: 0.0
	:esc: Speed change reference ().  Typical Value = 0.0015. Default: 0.0
	:kan: Discontinuous controller gain ().  Typical Value = 400. Default: 0.0
	:tan: Discontinuous controller time constant ().  Typical Value = 0.08. Default: 0.0
	:tw5: DEC washout time constant ().  Typical Value = 5. Default: 0.0
	:vsmax: Limiter ().  Typical Value = 0.2. Default: 0.0
	:vsmin: Limiter ().  Typical Value = -0.066. Default: 0.0
	:td: Time constant ().  Typical Value = 0.03. Default: 0.0
	:tl1: Time constant ().  Typical Value = 0.025. Default: 0.0
	:tl2: Time constant ().  Typical Value = 1.25. Default: 0.0
	:vtm: Voltage limits ().  Typical Value = 1.13. Default: 0.0
	:vtn: Voltage limits ().  Typical Value = 1.12. Default: 0.0
	:vanmax: Limiter for Van (). Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vtlmt': [cgmesProfile.DY.value, ],
						'vomax': [cgmesProfile.DY.value, ],
						'vomin': [cgmesProfile.DY.value, ],
						'ketl': [cgmesProfile.DY.value, ],
						'vtc': [cgmesProfile.DY.value, ],
						'val': [cgmesProfile.DY.value, ],
						'esc': [cgmesProfile.DY.value, ],
						'kan': [cgmesProfile.DY.value, ],
						'tan': [cgmesProfile.DY.value, ],
						'tw5': [cgmesProfile.DY.value, ],
						'vsmax': [cgmesProfile.DY.value, ],
						'vsmin': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'tl1': [cgmesProfile.DY.value, ],
						'tl2': [cgmesProfile.DY.value, ],
						'vtm': [cgmesProfile.DY.value, ],
						'vtn': [cgmesProfile.DY.value, ],
						'vanmax': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n' + DiscontinuousExcitationControlDynamics.__doc__ 

	def __init__(self, vtlmt = 0.0, vomax = 0.0, vomin = 0.0, ketl = 0.0, vtc = 0.0, val = 0.0, esc = 0.0, kan = 0.0, tan = 0.0, tw5 = 0.0, vsmax = 0.0, vsmin = 0.0, td = 0.0, tl1 = 0.0, tl2 = 0.0, vtm = 0.0, vtn = 0.0, vanmax = 0.0,  *args, **kw_args):
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
