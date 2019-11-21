from cimpy.cgmes_v2_4_15_flat.VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType2(VoltageCompensatorDynamics):
	'''
	

	:tr:  Default: 0.0
	:GenICompensationForGenJ: Compensation of this voltage compensator's generator for current flow out of another generator. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'GenICompensationForGenJ': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class VoltageCompensatorDynamics: \n' + VoltageCompensatorDynamics.__doc__ 

	def __init__(self, tr = 0.0, GenICompensationForGenJ = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tr = tr
		self.GenICompensationForGenJ = GenICompensationForGenJ
		
	def __str__(self):
		str = 'class=VCompIEEEType2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
