from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class WindMechIEC(IdentifiedObject):
	'''
	Two mass model.  Reference: IEC Standard 61400-27-1 Section 6.6.2.1.

	:WindGenTurbineType3IEC: Wind turbine Type 3 model with which this wind mechanical model is associated. Default: None
	:cdrt: Drive train damping (. It is type dependent parameter. Default: 0.0
	:hgen: Inertia constant of generator (). It is type dependent parameter. Default: 0.0
	:hwtr: Inertia constant of wind turbine rotor (). It is type dependent parameter. Default: 0.0
	:kdrt: Drive train stiffness (). It is type dependent parameter. Default: 0.0
	:WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated. Default: None
	:WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind mechanical model is associated. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindGenTurbineType3IEC': [cgmesProfile.DY.value, ],
						'cdrt': [cgmesProfile.DY.value, ],
						'hgen': [cgmesProfile.DY.value, ],
						'hwtr': [cgmesProfile.DY.value, ],
						'kdrt': [cgmesProfile.DY.value, ],
						'WindTurbineType4bIEC': [cgmesProfile.DY.value, ],
						'WindTurbineType1or2IEC': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, WindGenTurbineType3IEC = None, cdrt = 0.0, hgen = 0.0, hwtr = 0.0, kdrt = 0.0, WindTurbineType4bIEC = None, WindTurbineType1or2IEC = None,  *args, **kw_args):
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
