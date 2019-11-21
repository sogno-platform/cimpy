from cimpy.cgmes_v2_4_15_flat.PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerTabular(PhaseTapChanger):
	'''
	

	:PhaseTapChangerTable: The phase tap changer table for this phase tap changer. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'PhaseTapChangerTable': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class PhaseTapChanger: \n' + PhaseTapChanger.__doc__ 

	def __init__(self, PhaseTapChangerTable = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PhaseTapChangerTable = PhaseTapChangerTable
		
	def __str__(self):
		str = 'class=PhaseTapChangerTabular\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
