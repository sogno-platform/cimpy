from .IdentifiedObject import IdentifiedObject


class LoadDynamics(IdentifiedObject):
	'''
	Load whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font> A standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single load definition.  The load model is always applied to individual bus loads (energy consumers).

	:EnergyConsumer: Energy consumer to which this dynamics load model applies. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'EnergyConsumer': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, EnergyConsumer = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergyConsumer = EnergyConsumer
		
	def __str__(self):
		str = 'class=LoadDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
