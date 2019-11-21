from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class SubGeographicalRegion(IdentifiedObject):
	'''
	A subset of a geographical region of a power system network model.

	:DCLines:  Default: []
	:Region: The geographical region to which this sub-geographical region is within. Default: None
	:Lines: The lines within the sub-geographical region. Default: []
	:Substations: The substations in this sub-geographical region. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'DCLines': [cgmesProfile.EQ.value, ],
						'Region': [cgmesProfile.EQ.value, ],
						'Lines': [cgmesProfile.EQ.value, ],
						'Substations': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCLines = [], Region = None, Lines = [], Substations = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCLines = DCLines
		self.Region = Region
		self.Lines = Lines
		self.Substations = Substations
		
	def __str__(self):
		str = 'class=SubGeographicalRegion\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
