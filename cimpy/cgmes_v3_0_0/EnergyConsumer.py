from .EnergyConnection import EnergyConnection


class EnergyConsumer(EnergyConnection):
	'''
	Generic user of energy - a  point of consumption on the power system model. EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning only if there is no LoadResponseCharacteristic associated with EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to False.

	:LoadDynamics: Load dynamics model used to describe dynamic behaviour of this energy consumer. Default: None
	:p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
	:q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
	:pfixed: Active power of the load that is a fixed quantity and does not vary as load group value varies. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:pfixedPct: Fixed active power as a percentage of load group fixed active power. Used to represent the time-varying components.  Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:qfixed: Reactive power of the load that is a fixed quantity and does not vary as load group value varies. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:qfixedPct: Fixed reactive power as a percentage of load group fixed reactive power. Used to represent the time-varying components.  Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power. Default: None
		'''

	cgmesProfile = EnergyConnection.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'LoadDynamics': [cgmesProfile.DY.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						'pfixed': [cgmesProfile.EQ.value, ],
						'pfixedPct': [cgmesProfile.EQ.value, ],
						'qfixed': [cgmesProfile.EQ.value, ],
						'qfixedPct': [cgmesProfile.EQ.value, ],
						'LoadResponse': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EnergyConnection: \n' + EnergyConnection.__doc__ 

	def __init__(self, LoadDynamics = None, p = 0.0, q = 0.0, pfixed = 0.0, pfixedPct = 0.0, qfixed = 0.0, qfixedPct = 0.0, LoadResponse = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadDynamics = LoadDynamics
		self.p = p
		self.q = q
		self.pfixed = pfixed
		self.pfixedPct = pfixedPct
		self.qfixed = qfixed
		self.qfixedPct = qfixedPct
		self.LoadResponse = LoadResponse
		
	def __str__(self):
		str = 'class=EnergyConsumer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
