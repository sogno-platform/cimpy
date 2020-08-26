from cimpy.cgmes_v2_4_15.RotatingMachine import RotatingMachine


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

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.DY.value, ],
						'nominalFrequency': [cgmesProfile.EQ.value, ],
						'nominalSpeed': [cgmesProfile.EQ.value, ],
						'converterFedDrive': [cgmesProfile.EQ.value, ],
						'efficiency': [cgmesProfile.EQ.value, ],
						'iaIrRatio': [cgmesProfile.EQ.value, ],
						'polePairNumber': [cgmesProfile.EQ.value, ],
						'ratedMechanicalPower': [cgmesProfile.EQ.value, ],
						'reversible': [cgmesProfile.EQ.value, ],
						'rxLockedRotorRatio': [cgmesProfile.EQ.value, ],
						'asynchronousMachineType': [cgmesProfile.SSH.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.DY.value, ],
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
