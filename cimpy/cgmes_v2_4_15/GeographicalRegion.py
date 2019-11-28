from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class GeographicalRegion(IdentifiedObject):
	'''
	A geographical region of a power system network model.

	:Regions: All sub-geograhpical regions within this geographical region. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Regions': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Regions = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Regions = Regions
		
	def __str__(self):
		str = 'class=GeographicalRegion\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
