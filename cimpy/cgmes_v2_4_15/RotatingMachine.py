from cimpy.cgmes_v2_4_15_flat.RegulatingCondEq import RegulatingCondEq


class RotatingMachine(RegulatingCondEq):
	'''
	A rotating machine which may be used as a generator or motor.

	:GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: None
	:HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. Default: None
	:ratedPowerFactor: Power factor (nameplate data). It is primarily used for short circuit data exchange according to IEC 60909. Default: 0.0
	:ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value. Default: 0.0
	:ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. Default: 0.0
	:p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
	:q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'GeneratingUnit': [cgmesProfile.EQ.value, ],
						'HydroPump': [cgmesProfile.EQ.value, ],
						'ratedPowerFactor': [cgmesProfile.EQ.value, ],
						'ratedS': [cgmesProfile.EQ.value, ],
						'ratedU': [cgmesProfile.EQ.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, GeneratingUnit = None, HydroPump = None, ratedPowerFactor = 0.0, ratedS = 0.0, ratedU = 0.0, p = 0.0, q = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.GeneratingUnit = GeneratingUnit
		self.HydroPump = HydroPump
		self.ratedPowerFactor = ratedPowerFactor
		self.ratedS = ratedS
		self.ratedU = ratedU
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=RotatingMachine\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
