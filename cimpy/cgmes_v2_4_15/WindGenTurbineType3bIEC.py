from cimpy.cgmes_v2_4_15.WindGenTurbineType3IEC import WindGenTurbineType3IEC


class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
	'''
	IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

	:fducw: Crowbar duration versus voltage variation look-up table (f()). It is case dependent parameter. Default: 0.0
	:tg: Current generation Time constant (). It is type dependent parameter. Default: 0.0
	:two: Time constant for crowbar washout filter (). It is case dependent parameter. Default: 0.0
	:mwtcwp: Crowbar control mode ().   The parameter is case dependent parameter. Default: False
	:xs: Electromagnetic transient reactance (x). It is type dependent parameter. Default: 0.0
		'''

	cgmesProfile = WindGenTurbineType3IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'fducw': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'two': [cgmesProfile.DY.value, ],
						'mwtcwp': [cgmesProfile.DY.value, ],
						'xs': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class WindGenTurbineType3IEC: \n' + WindGenTurbineType3IEC.__doc__ 

	def __init__(self, fducw = 0.0, tg = 0.0, two = 0.0, mwtcwp = False, xs = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fducw = fducw
		self.tg = tg
		self.two = two
		self.mwtcwp = mwtcwp
		self.xs = xs
		
	def __str__(self):
		str = 'class=WindGenTurbineType3bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
