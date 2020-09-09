from .IdentifiedObject import IdentifiedObject


class Control(IdentifiedObject):
	'''
	Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.

	:controlType: Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. Default: ''
	:operationInProgress: Indicates that a client is currently sending control commands that has not completed. Default: False
	:timeStamp: The last time a control output was sent. Default: ''
	:unitMultiplier: The unit multiplier of the controlled quantity. Default: None
	:unitSymbol: The unit of measure of the controlled quantity. Default: None
	:PowerSystemResource: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'controlType': [cgmesProfile.EQ.value, ],
						'operationInProgress': [cgmesProfile.EQ.value, ],
						'timeStamp': [cgmesProfile.EQ.value, ],
						'unitMultiplier': [cgmesProfile.EQ.value, ],
						'unitSymbol': [cgmesProfile.EQ.value, ],
						'PowerSystemResource': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, controlType = '', operationInProgress = False, timeStamp = '', unitMultiplier = None, unitSymbol = None, PowerSystemResource = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.controlType = controlType
		self.operationInProgress = operationInProgress
		self.timeStamp = timeStamp
		self.unitMultiplier = unitMultiplier
		self.unitSymbol = unitSymbol
		self.PowerSystemResource = PowerSystemResource
		
	def __str__(self):
		str = 'class=Control\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
