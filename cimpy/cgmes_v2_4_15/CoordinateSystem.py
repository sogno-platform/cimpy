from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class CoordinateSystem(IdentifiedObject):
	'''
	Coordinate reference system.

	:crsUrn: A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define 'Location.PositionPoints'. An example would be the European Petroleum Survey Group (EPSG) code for a coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as: urn:ogc:def:uom:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG Registry web site http://www.epsg-registry.org/). To define the coordinate system as being WGS84 (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:uom:EPSG::4236. A profile should limit this code to a set of allowed URNs agreed to by all sending and receiving parties. Default: ''
	:Location: All locations described with position points in this coordinate system. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						'crsUrn': [cgmesProfile.GL.value, ],
						'Location': [cgmesProfile.GL.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, crsUrn = '', Location = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.crsUrn = crsUrn
		self.Location = Location
		
	def __str__(self):
		str = 'class=CoordinateSystem\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
