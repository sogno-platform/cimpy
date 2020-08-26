from cimpy.output.ConductingEquipment import ConductingEquipment


class EnergySource(ConductingEquipment):
	'''
	A generic equivalent for an energy supplier on a transmission or distribution voltage level.

	:EnergySchedulingType: Energy Source of a particular Energy Scheduling Type Default: 
	:nominalVoltage: Phase-to-phase nominal voltage. Default: 
	:r: Positive sequence Thevenin resistance. Default: 
	:r0: Zero sequence Thevenin resistance. Default: 
	:rn: Negative sequence Thevenin resistance. Default: 
	:voltageAngle: Phase angle of a-phase open circuit. Default: 
	:voltageMagnitude: Phase-to-phase open circuit voltage magnitude. Default: 
	:x: Positive sequence Thevenin reactance. Default: 
	:x0: Zero sequence Thevenin reactance. Default: 
	:xn: Negative sequence Thevenin reactance. Default: 
	:activePower: High voltage source active injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
	:reactivePower: High voltage source reactive injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 
	:WindTurbineType3or4Dynamics: Wind generator Type 3 or 4 dynamics model associated with this energy source. Default: 
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'EnergySchedulingType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'nominalVoltage': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'rn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'voltageAngle': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'voltageMagnitude': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'xn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'activePower': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'reactivePower': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'WindTurbineType3or4Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, EnergySchedulingType = , nominalVoltage = , r = , r0 = , rn = , voltageAngle = , voltageMagnitude = , x = , x0 = , xn = , activePower = , reactivePower = , WindTurbineType3or4Dynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergySchedulingType = EnergySchedulingType
		self.nominalVoltage = nominalVoltage
		self.r = r
		self.r0 = r0
		self.rn = rn
		self.voltageAngle = voltageAngle
		self.voltageMagnitude = voltageMagnitude
		self.x = x
		self.x0 = x0
		self.xn = xn
		self.activePower = activePower
		self.reactivePower = reactivePower
		self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
		
	def __str__(self):
		str = 'class=EnergySource\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
