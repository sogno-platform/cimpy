from cimpy.cgmes_v2_4_15.EquipmentContainer import EquipmentContainer


class VoltageLevel(EquipmentContainer):
	'''
	A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

	:BaseVoltage: The base voltage used for all equipment within the voltage level. Default: None
	:Substation: The substation of the voltage level. Default: None
	:highVoltageLimit: The bus bar's high voltage limit Default: 0.0
	:lowVoltageLimit: The bus bar's low voltage limit Default: 0.0
		'''

	cgmesProfile = EquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'BaseVoltage': [cgmesProfile.EQ.value, ],
						'Substation': [cgmesProfile.EQ.value, ],
						'highVoltageLimit': [cgmesProfile.EQ.value, ],
						'lowVoltageLimit': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, BaseVoltage = None, Substation = None, highVoltageLimit = 0.0, lowVoltageLimit = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BaseVoltage = BaseVoltage
		self.Substation = Substation
		self.highVoltageLimit = highVoltageLimit
		self.lowVoltageLimit = lowVoltageLimit
		
	def __str__(self):
		str = 'class=VoltageLevel\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
