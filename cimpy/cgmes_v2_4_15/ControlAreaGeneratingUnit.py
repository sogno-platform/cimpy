from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class ControlAreaGeneratingUnit(IdentifiedObject):
	'''
	A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.

	:GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. Default: None
	:ControlArea: The parent control area for the generating unit specifications. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'GeneratingUnit': [cgmesProfile.EQ.value, ],
						'ControlArea': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, GeneratingUnit = None, ControlArea = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.GeneratingUnit = GeneratingUnit
		self.ControlArea = ControlArea
		
	def __str__(self):
		str = 'class=ControlAreaGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
