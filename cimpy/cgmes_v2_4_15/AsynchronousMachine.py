from cimpy.output.RotatingMachine import RotatingMachine


class AsynchronousMachine(RotatingMachine):
	'''
	A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g squirrel-cage induction machine.

	:nominalFrequency: Nameplate data indicates if the machine is 50 or 60 Hz. Default: 
	:nominalSpeed: Nameplate data.  Depends on the slip and number of pole pairs. Default: 
	:converterFedDrive: Indicates whether the machine is a converter fed drive. Used for short circuit data exchange according to IEC 60909 Default: 
	:efficiency: Efficiency of the asynchronous machine at nominal operation in percent. Indicator for converter drive motors. Used for short circuit data exchange according to IEC 60909 Default: 
	:iaIrRatio: Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data exchange according to IEC 60909 Default: 
	:polePairNumber: Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909 Default: 
	:ratedMechanicalPower: Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data exchange according to IEC 60909. Default: 
	:reversible: Indicates for converter drive motors if the power can be reversible. Used for short circuit data exchange according to IEC 60909 Default: 
	:rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909 Default: 
	:asynchronousMachineType: Indicates the type of Asynchronous Machine (motor or generator). Default: 
	:AsynchronousMachineDynamics: Asynchronous machine dynamics model used to describe dynamic behavior of this asynchronous machine. Default: 
		'''

	cgmesProfile = RotatingMachine.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'nominalFrequency': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'nominalSpeed': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'converterFedDrive': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'efficiency': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'iaIrRatio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'polePairNumber': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedMechanicalPower': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'reversible': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'rxLockedRotorRatio': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'asynchronousMachineType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachine: \n' + RotatingMachine.__doc__ 

	def __init__(self, nominalFrequency = , nominalSpeed = , converterFedDrive = , efficiency = , iaIrRatio = , polePairNumber = , ratedMechanicalPower = , reversible = , rxLockedRotorRatio = , asynchronousMachineType = , AsynchronousMachineDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.nominalFrequency = nominalFrequency
		self.nominalSpeed = nominalSpeed
		self.converterFedDrive = converterFedDrive
		self.efficiency = efficiency
		self.iaIrRatio = iaIrRatio
		self.polePairNumber = polePairNumber
		self.ratedMechanicalPower = ratedMechanicalPower
		self.reversible = reversible
		self.rxLockedRotorRatio = rxLockedRotorRatio
		self.asynchronousMachineType = asynchronousMachineType
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		
	def __str__(self):
		str = 'class=AsynchronousMachine\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
