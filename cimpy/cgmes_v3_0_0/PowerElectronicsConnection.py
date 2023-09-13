from .RegulatingCondEq import RegulatingCondEq


class PowerElectronicsConnection(RegulatingCondEq):
	'''
	A connection to the AC network for energy production or consumption that uses power electronics rather than rotating machines.

	:WindTurbineType3or4Dynamics: The wind turbine type 3 or type 4 dynamics model associated with this power electronics connection. Default: None
	:p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
	:q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
	:maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0
	:minQ: Minimum reactive power limit for the unit. This is the minimum (nameplate) limit for the unit. Default: 0.0
	:ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value. Default: 0.0
	:ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. The attribute shall be a positive value. Default: 0.0
	:PowerElectronicsUnit: An AC network connection may have several power electronics units connecting through it. Default: None
		'''

	cgmesProfile = RegulatingCondEq.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.DY.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						'maxQ': [cgmesProfile.EQ.value, ],
						'minQ': [cgmesProfile.EQ.value, ],
						'ratedS': [cgmesProfile.EQ.value, ],
						'ratedU': [cgmesProfile.EQ.value, ],
						'PowerElectronicsUnit': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, WindTurbineType3or4Dynamics = None, p = 0.0, q = 0.0, maxQ = 0.0, minQ = 0.0, ratedS = 0.0, ratedU = 0.0, PowerElectronicsUnit = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
		self.p = p
		self.q = q
		self.maxQ = maxQ
		self.minQ = minQ
		self.ratedS = ratedS
		self.ratedU = ratedU
		self.PowerElectronicsUnit = PowerElectronicsUnit
		
	def __str__(self):
		str = 'class=PowerElectronicsConnection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
