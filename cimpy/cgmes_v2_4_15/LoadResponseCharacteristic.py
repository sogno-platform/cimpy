from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class LoadResponseCharacteristic(IdentifiedObject):
	'''
	Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means "multiply" and ** is "raised to power of".

	:EnergyConsumer: The set of loads that have the response characteristics. Default: "many"
	:exponentModel: Indicates the exponential voltage dependency model is to be used.   If false, the coefficient model is to be used. The exponential voltage dependency model consist of the attributes - pVoltageExponent - qVoltageExponent. The coefficient model consist of the attributes - pConstantImpedance - pConstantCurrent - pConstantPower - qConstantImpedance - qConstantCurrent - qConstantPower. The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal 1. The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1. Default: False
	:pConstantCurrent: Portion of active power load modeled as constant current. Default: 0.0
	:pConstantImpedance: Portion of active power load modeled as constant impedance. Default: 0.0
	:pConstantPower: Portion of active power load modeled as constant power. Default: 0.0
	:pFrequencyExponent: Exponent of per unit frequency effecting active power. Default: 0.0
	:pVoltageExponent: Exponent of per unit voltage effecting real power. Default: 0.0
	:qConstantCurrent: Portion of reactive power load modeled as constant current. Default: 0.0
	:qConstantImpedance: Portion of reactive power load modeled as constant impedance. Default: 0.0
	:qConstantPower: Portion of reactive power load modeled as constant power. Default: 0.0
	:qFrequencyExponent: Exponent of per unit frequency effecting reactive power. Default: 0.0
	:qVoltageExponent: Exponent of per unit voltage effecting reactive power. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, EnergyConsumer = "many", exponentModel = False, pConstantCurrent = 0.0, pConstantImpedance = 0.0, pConstantPower = 0.0, pFrequencyExponent = 0.0, pVoltageExponent = 0.0, qConstantCurrent = 0.0, qConstantImpedance = 0.0, qConstantPower = 0.0, qFrequencyExponent = 0.0, qVoltageExponent = 0.0,  *args, **kw_args):
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
