from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR5(ExcitationSystemDynamics):
	'''
	Manual excitation control with field circuit resistance. This model can be used as a very simple representation of manual voltage control.

	:ka: Gain (Ka). Default: 0.0
	:ta: Time constant (Ta). Default: 0.0
	:rex: Effective Output Resistance (Rex). Rex represents the effective output resistance seen by the excitation system. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'rex': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0.0, rex = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.rex = rex
		
	def __str__(self):
		str = 'class=ExcAVR5\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
