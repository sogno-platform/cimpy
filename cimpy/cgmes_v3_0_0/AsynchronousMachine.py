from .RotatingMachine import RotatingMachine


class AsynchronousMachine(RotatingMachine):
	'''
	A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g. squirrel-cage induction machine.

	:AsynchronousMachineDynamics: Asynchronous machine dynamics model used to describe dynamic behaviour of this asynchronous machine. Default: None
	:asynchronousMachineType: Indicates the type of Asynchronous Machine (motor or generator). Default: None
	:nominalFrequency: Nameplate data indicates if the machine is 50 Hz or 60 Hz. Default: 0.0
	:nominalSpeed: Nameplate data.  Depends on the slip and number of pole pairs. Default: 0.0
	:converterFedDrive: Indicates whether the machine is a converter fed drive. Used for short circuit data exchange according to IEC 60909. Default: False
	:efficiency: Efficiency of the asynchronous machine at nominal operation as a percentage. Indicator for converter drive motors. Used for short circuit data exchange according to IEC 60909. Default: 0.0
	:iaIrRatio: Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data exchange according to IEC 60909. Default: 0.0
	:polePairNumber: Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909. Default: 0
	:ratedMechanicalPower: Rated mechanical power (Pr in IEC 60909-0). Used for short circuit data exchange according to IEC 60909. Default: 0.0
	:reversible: Indicates for converter drive motors if the power can be reversible. Used for short circuit data exchange according to IEC 60909. Default: False
	:rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909. Default: 0.0
		'''

	cgmesProfile = RotatingMachine.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'asynchronousMachineType': [cgmesProfile.SSH.value, ],
						'nominalFrequency': [cgmesProfile.EQ.value, ],
						'nominalSpeed': [cgmesProfile.EQ.value, ],
						'converterFedDrive': [cgmesProfile.SC.value, ],
						'efficiency': [cgmesProfile.SC.value, ],
						'iaIrRatio': [cgmesProfile.SC.value, ],
						'polePairNumber': [cgmesProfile.SC.value, ],
						'ratedMechanicalPower': [cgmesProfile.SC.value, ],
						'reversible': [cgmesProfile.SC.value, ],
						'rxLockedRotorRatio': [cgmesProfile.SC.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RotatingMachine: \n' + RotatingMachine.__doc__ 

	def __init__(self, AsynchronousMachineDynamics = None, asynchronousMachineType = None, nominalFrequency = 0.0, nominalSpeed = 0.0, converterFedDrive = False, efficiency = 0.0, iaIrRatio = 0.0, polePairNumber = 0, ratedMechanicalPower = 0.0, reversible = False, rxLockedRotorRatio = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		self.asynchronousMachineType = asynchronousMachineType
		self.nominalFrequency = nominalFrequency
		self.nominalSpeed = nominalSpeed
		self.converterFedDrive = converterFedDrive
		self.efficiency = efficiency
		self.iaIrRatio = iaIrRatio
		self.polePairNumber = polePairNumber
		self.ratedMechanicalPower = ratedMechanicalPower
		self.reversible = reversible
		self.rxLockedRotorRatio = rxLockedRotorRatio
		
	def __str__(self):
		str = 'class=AsynchronousMachine\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
