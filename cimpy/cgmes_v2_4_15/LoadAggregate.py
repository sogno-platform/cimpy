from cimpy.cgmes_v2_4_15.LoadDynamics import LoadDynamics


class LoadAggregate(LoadDynamics):
	'''
	Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.

	:LoadStatic: Aggregate static load associated with this aggregate load. Default: None
	:LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load. Default: None
		'''

	cgmesProfile = LoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'LoadStatic': [cgmesProfile.DY.value, ],
						'LoadMotor': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, LoadStatic = None, LoadMotor = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadStatic = LoadStatic
		self.LoadMotor = LoadMotor
		
	def __str__(self):
		str = 'class=LoadAggregate\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
