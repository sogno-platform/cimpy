from .HVDCDynamics import HVDCDynamics


class VSCDynamics(HVDCDynamics):
	'''
	VSC function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

	:VsConverter: Voltage source converter to which voltage source converter dynamics model applies. Default: None
		'''

	cgmesProfile = HVDCDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'VsConverter': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class HVDCDynamics: \n' + HVDCDynamics.__doc__ 

	def __init__(self, VsConverter = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.VsConverter = VsConverter
		
	def __str__(self):
		str = 'class=VSCDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
