from cimpy.output.IdentifiedObject import IdentifiedObject


class WindMechIEC(IdentifiedObject):
	'''
	Two mass model.  Reference: IEC Standard 61400-27-1 Section 6.6.2.1.

	:WindGenTurbineType3IEC: Wind turbine Type 3 model with which this wind mechanical model is associated. Default: 
	:cdrt: Drive train damping (. It is type dependent parameter. Default: 
	:hgen: Inertia constant of generator (). It is type dependent parameter. Default: 
	:hwtr: Inertia constant of wind turbine rotor (). It is type dependent parameter. Default: 
	:kdrt: Drive train stiffness (). It is type dependent parameter. Default: 
	:WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated. Default: 
	:WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind mechanical model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindGenTurbineType3IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'cdrt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'hgen': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'hwtr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kdrt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType4bIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType1or2IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindGenTurbineType3IEC = , cdrt = , hgen = , hwtr = , kdrt = , WindTurbineType4bIEC = , WindTurbineType1or2IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
		self.cdrt = cdrt
		self.hgen = hgen
		self.hwtr = hwtr
		self.kdrt = kdrt
		self.WindTurbineType4bIEC = WindTurbineType4bIEC
		self.WindTurbineType1or2IEC = WindTurbineType1or2IEC
		
	def __str__(self):
		str = 'class=WindMechIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
