from cimpy.cgmes_v2_4_15.EquivalentEquipment import EquivalentEquipment


class EquivalentBranch(EquivalentEquipment):
	'''
	The class represents equivalent branches.

	:r: Positive sequence series resistance of the reduced branch. Default: 0.0
	:r21: Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0
	:x: Positive sequence series reactance of the reduced branch. Default: 0.0
	:x21: Reactance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x. Usage rule : EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0
	:negativeR12: Negative sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:negativeR21: Negative sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:negativeX12: Negative sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:negativeX21: Negative sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:positiveR12: Positive sequence series resistance from terminal sequence  1 to terminal sequence 2 . Used for short circuit data exchange according to IEC 60909.  EquivalentBranch is a result of network reduction prior to the data exchange. Default: 0.0
	:positiveR21: Positive sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:positiveX12: Positive sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:positiveX21: Positive sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:zeroR12: Zero sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:zeroR21: Zero sequence series resistance from terminal sequence  2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:zeroX12: Zero sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
	:zeroX21: Zero sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data exchange according to IEC 60909 Usage : EquivalentBranch is a result of network reduction prior to the data exchange Default: 0.0
		'''

	cgmesProfile = EquivalentEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'r': [cgmesProfile.EQ.value, ],
						'r21': [cgmesProfile.EQ.value, ],
						'x': [cgmesProfile.EQ.value, ],
						'x21': [cgmesProfile.EQ.value, ],
						'negativeR12': [cgmesProfile.EQ.value, ],
						'negativeR21': [cgmesProfile.EQ.value, ],
						'negativeX12': [cgmesProfile.EQ.value, ],
						'negativeX21': [cgmesProfile.EQ.value, ],
						'positiveR12': [cgmesProfile.EQ.value, ],
						'positiveR21': [cgmesProfile.EQ.value, ],
						'positiveX12': [cgmesProfile.EQ.value, ],
						'positiveX21': [cgmesProfile.EQ.value, ],
						'zeroR12': [cgmesProfile.EQ.value, ],
						'zeroR21': [cgmesProfile.EQ.value, ],
						'zeroX12': [cgmesProfile.EQ.value, ],
						'zeroX21': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class EquivalentEquipment: \n' + EquivalentEquipment.__doc__ 

	def __init__(self, r = 0.0, r21 = 0.0, x = 0.0, x21 = 0.0, negativeR12 = 0.0, negativeR21 = 0.0, negativeX12 = 0.0, negativeX21 = 0.0, positiveR12 = 0.0, positiveR21 = 0.0, positiveX12 = 0.0, positiveX21 = 0.0, zeroR12 = 0.0, zeroR21 = 0.0, zeroX12 = 0.0, zeroX21 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.r = r
		self.r21 = r21
		self.x = x
		self.x21 = x21
		self.negativeR12 = negativeR12
		self.negativeR21 = negativeR21
		self.negativeX12 = negativeX12
		self.negativeX21 = negativeX21
		self.positiveR12 = positiveR12
		self.positiveR21 = positiveR21
		self.positiveX12 = positiveX12
		self.positiveX21 = positiveX21
		self.zeroR12 = zeroR12
		self.zeroR21 = zeroR21
		self.zeroX12 = zeroX12
		self.zeroX21 = zeroX21
		
	def __str__(self):
		str = 'class=EquivalentBranch\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
