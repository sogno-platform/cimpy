from cimpy.output.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
	'''
	The class represents IEEE Type DEC2A model for the discontinuous excitation control. This system provides transient excitation boosting via an open-loop control as initiated by a trigger signal generated remotely.  Reference: IEEE Standard 421.5-2005 Section 12.3.

	:vk: Discontinuous controller input reference (). Default: 
	:td1: Discontinuous controller time constant (). Default: 
	:td2: Discontinuous controller washout time constant (). Default: 
	:vdmin: Limiter (). Default: 
	:vdmax: Limiter (). Default: 
		'''

	cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vk': [cgmesProfile.DY.value, ],
						'td1': [cgmesProfile.DY.value, ],
						'td2': [cgmesProfile.DY.value, ],
						'vdmin': [cgmesProfile.DY.value, ],
						'vdmax': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n' + DiscontinuousExcitationControlDynamics.__doc__ 

	def __init__(self, vk = , td1 = , td2 = , vdmin = , vdmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vk = vk
		self.td1 = td1
		self.td2 = td2
		self.vdmin = vdmin
		self.vdmax = vdmax
		
	def __str__(self):
		str = 'class=DiscExcContIEEEDEC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
