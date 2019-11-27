from cimpy.cgmes_v2_4_15.WindGenTurbineType3IEC import WindGenTurbineType3IEC


class WindGenTurbineType3aIEC(WindGenTurbineType3IEC):
	'''
	IEC Type 3A generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.2.

	:kpc: Current PI controller proportional gain (K). It is type dependent parameter. Default: 0.0
	:xs: Electromagnetic transient reactance (x). It is type dependent parameter. Default: 0.0
	:tic: Current PI controller integration time constant (T). It is type dependent parameter. Default: 0.0
		'''

	cgmesProfile = WindGenTurbineType3IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpc': [cgmesProfile.DY.value, ],
						'xs': [cgmesProfile.DY.value, ],
						'tic': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class WindGenTurbineType3IEC: \n' + WindGenTurbineType3IEC.__doc__ 

	def __init__(self, kpc = 0.0, xs = 0.0, tic = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpc = kpc
		self.xs = xs
		self.tic = tic
		
	def __str__(self):
		str = 'class=WindGenTurbineType3aIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
