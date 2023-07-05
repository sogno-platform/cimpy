from .IdentifiedObject import IdentifiedObject


class BaseVoltage(IdentifiedObject):
	'''
	Defines a system base voltage which is referenced.

	:TopologicalNode: The topological nodes at the base voltage. Default: "list"
	:nominalVoltage: The power system resource`s base voltage.  Shall be a positive value and not zero. Default: 0.0
	:ConductingEquipment: All conducting equipment with this base voltage.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: "list"
	:VoltageLevel: The voltage levels having this base voltage. Default: "list"
	:TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.TP.value, cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						'nominalVoltage': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'ConductingEquipment': [cgmesProfile.EQ.value, ],
						'VoltageLevel': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'TransformerEnds': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, TopologicalNode = "list", nominalVoltage = 0.0, ConductingEquipment = "list", VoltageLevel = "list", TransformerEnds = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TopologicalNode = TopologicalNode
		self.nominalVoltage = nominalVoltage
		self.ConductingEquipment = ConductingEquipment
		self.VoltageLevel = VoltageLevel
		self.TransformerEnds = TransformerEnds
		
	def __str__(self):
		str = 'class=BaseVoltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
