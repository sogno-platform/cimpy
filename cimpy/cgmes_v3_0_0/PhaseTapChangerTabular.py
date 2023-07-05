from .PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerTabular(PhaseTapChanger):
	'''
	Describes a tap changer with a table defining the relation between the tap step and the phase angle difference across the transformer.

	:PhaseTapChangerTable: The phase tap changer table for this phase tap changer. Default: None
		'''

	cgmesProfile = PhaseTapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'PhaseTapChangerTable': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

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
