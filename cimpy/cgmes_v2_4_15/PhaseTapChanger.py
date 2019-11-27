from cimpy.cgmes_v2_4_15.TapChanger import TapChanger


class PhaseTapChanger(TapChanger):
	'''
	A transformer phase shifting tap model that controls the phase angle difference across the power transformer and potentially the active power flow through the power transformer.  This phase tap model may also impact the voltage magnitude.

	:TransformerEnd: Phase tap changer associated with this transformer end. Default: None
		'''

	cgmesProfile = TapChanger.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'TransformerEnd': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TapChanger: \n' + TapChanger.__doc__ 

	def __init__(self, TransformerEnd = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TransformerEnd = TransformerEnd
		
	def __str__(self):
		str = 'class=PhaseTapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
