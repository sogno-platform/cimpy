from cimpy.cgmes_v2_4_15.VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType1(VoltageCompensatorDynamics):
	'''
	Reference: IEEE Standard 421.5-2005 Section 4.

	:rc:  Default: 0.0
	:xc:  Default: 0.0
	:tr:  Default: 0.0
		'''

	cgmesProfile = VoltageCompensatorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'rc': [cgmesProfile.DY.value, ],
						'xc': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class VoltageCompensatorDynamics: \n' + VoltageCompensatorDynamics.__doc__ 

	def __init__(self, rc = 0.0, xc = 0.0, tr = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.rc = rc
		self.xc = xc
		self.tr = tr
		
	def __str__(self):
		str = 'class=VCompIEEEType1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
