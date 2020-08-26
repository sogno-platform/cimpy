from cimpy.output.IdentifiedObject import IdentifiedObject


class LoadResponseCharacteristic(IdentifiedObject):
	'''
	Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means "multiply" and ** is "raised to power of".

	:EnergyConsumer: The set of loads that have the response characteristics. Default: 
	:exponentModel: Indicates the exponential voltage dependency model is to be used.   If false, the coefficient model is to be used. The exponential voltage dependency model consist of the attributes - pVoltageExponent - qVoltageExponent. The coefficient model consist of the attributes - pConstantImpedance - pConstantCurrent - pConstantPower - qConstantImpedance - qConstantCurrent - qConstantPower. The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal 1. The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1. Default: 
	:pConstantCurrent: Portion of active power load modeled as constant current. Default: 
	:pConstantImpedance: Portion of active power load modeled as constant impedance. Default: 
	:pConstantPower: Portion of active power load modeled as constant power. Default: 
	:pFrequencyExponent: Exponent of per unit frequency effecting active power. Default: 
	:pVoltageExponent: Exponent of per unit voltage effecting real power. Default: 
	:qConstantCurrent: Portion of reactive power load modeled as constant current. Default: 
	:qConstantImpedance: Portion of reactive power load modeled as constant impedance. Default: 
	:qConstantPower: Portion of reactive power load modeled as constant power. Default: 
	:qFrequencyExponent: Exponent of per unit frequency effecting reactive power. Default: 
	:qVoltageExponent: Exponent of per unit voltage effecting reactive power. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'EnergyConsumer': [cgmesProfile.EQ.value, ],
						'exponentModel': [cgmesProfile.EQ.value, ],
						'pConstantCurrent': [cgmesProfile.EQ.value, ],
						'pConstantImpedance': [cgmesProfile.EQ.value, ],
						'pConstantPower': [cgmesProfile.EQ.value, ],
						'pFrequencyExponent': [cgmesProfile.EQ.value, ],
						'pVoltageExponent': [cgmesProfile.EQ.value, ],
						'qConstantCurrent': [cgmesProfile.EQ.value, ],
						'qConstantImpedance': [cgmesProfile.EQ.value, ],
						'qConstantPower': [cgmesProfile.EQ.value, ],
						'qFrequencyExponent': [cgmesProfile.EQ.value, ],
						'qVoltageExponent': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, EnergyConsumer = , exponentModel = , pConstantCurrent = , pConstantImpedance = , pConstantPower = , pFrequencyExponent = , pVoltageExponent = , qConstantCurrent = , qConstantImpedance = , qConstantPower = , qFrequencyExponent = , qVoltageExponent = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergyConsumer = EnergyConsumer
		self.exponentModel = exponentModel
		self.pConstantCurrent = pConstantCurrent
		self.pConstantImpedance = pConstantImpedance
		self.pConstantPower = pConstantPower
		self.pFrequencyExponent = pFrequencyExponent
		self.pVoltageExponent = pVoltageExponent
		self.qConstantCurrent = qConstantCurrent
		self.qConstantImpedance = qConstantImpedance
		self.qConstantPower = qConstantPower
		self.qFrequencyExponent = qFrequencyExponent
		self.qVoltageExponent = qVoltageExponent
		
	def __str__(self):
		str = 'class=LoadResponseCharacteristic\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
