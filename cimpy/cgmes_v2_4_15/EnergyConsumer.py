from .ConductingEquipment import ConductingEquipment


class EnergyConsumer(ConductingEquipment):
	'''
	Generic user of energy - a  point of consumption on the power system model.

	:LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power. Default: None
	:pfixed: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:pfixedPct: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:qfixed: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
	:p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
	:q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
	:LoadDynamics: Load dynamics model used to describe dynamic behavior of this energy consumer. Default: None
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.DY.value, ],
						'LoadResponse': [cgmesProfile.EQ.value, ],
						'pfixed': [cgmesProfile.EQ.value, ],
						'pfixedPct': [cgmesProfile.EQ.value, ],
						'qfixed': [cgmesProfile.EQ.value, ],
						'qfixedPct': [cgmesProfile.EQ.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						'LoadDynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, LoadResponse = None, pfixed = 0.0, pfixedPct = 0.0, qfixed = 0.0, qfixedPct = 0.0, p = 0.0, q = 0.0, LoadDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadResponse = LoadResponse
		self.pfixed = pfixed
		self.pfixedPct = pfixedPct
		self.qfixed = qfixed
		self.qfixedPct = qfixedPct
		self.p = p
		self.q = q
		self.LoadDynamics = LoadDynamics
		
	def __str__(self):
		str = 'class=EnergyConsumer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
