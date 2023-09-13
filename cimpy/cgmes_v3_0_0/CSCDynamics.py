from .HVDCDynamics import HVDCDynamics


class CSCDynamics(HVDCDynamics):
	'''
	CSC function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

	:CSConverter: Current source converter to which current source converter dynamics model applies. Default: None
		'''

	cgmesProfile = HVDCDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'CSConverter': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class HVDCDynamics: \n' + HVDCDynamics.__doc__ 

	def __init__(self, CSConverter = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CSConverter = CSConverter
		
	def __str__(self):
		str = 'class=CSCDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
