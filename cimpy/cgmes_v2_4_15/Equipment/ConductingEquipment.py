from cimpy.cgmes_v2_4_15.Equipment.Equipment import Equipment


class ConductingEquipment(Equipment):
	'''
	The parts of the AC power system that are designed to carry current or that are conductively connected through terminals.

	:BaseVoltage: All conducting equipment with this base voltage.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: None
	:Terminals: Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: []
	:SvStatus: The status state variable associated with this conducting equipment. Default: None
		'''

	reference_dict = { 'StateVariablesVersion': ['SvStatus', ],
					 } 

	__doc__ += '\n Documentation of parent class Equipment: \n' + Equipment.__doc__ 

	def __init__(self, BaseVoltage = None, Terminals = [], SvStatus = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BaseVoltage = BaseVoltage
		self.Terminals = Terminals
		self.SvStatus = SvStatus
		
	def __str__(self):
		str = 'class=ConductingEquipment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
