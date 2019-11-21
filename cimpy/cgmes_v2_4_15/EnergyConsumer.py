from cimpy.cgmes_v2_4_15_flat.ConductingEquipment import ConductingEquipment


class EnergyConsumer(ConductingEquipment):
	'''
	Generic user of energy - a  point of consumption on the power system model.

	:LoadDynamics: Load dynamics model used to describe dynamic behavior of this energy consumer. Default: None
	:LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power. Default: None
	:p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
	:q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'LoadDynamics': [cgmesProfile.DY.value, ],
						'LoadResponse': [cgmesProfile.EQ.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, LoadDynamics = None, LoadResponse = None, p = 0.0, q = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadDynamics = LoadDynamics
		self.LoadResponse = LoadResponse
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=EnergyConsumer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
