from .IOPoint import IOPoint


class Control(IOPoint):
	'''
	Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.

	:controlType: Specifies the type of Control. For example, this specifies if the Control represents BreakerOpen, BreakerClose, GeneratorVoltageSetPoint, GeneratorRaise, GeneratorLower, etc. Default: ''
	:operationInProgress: Indicates that a client is currently sending control commands that has not completed. Default: False
	:timeStamp: The last time a control output was sent. Default: ''
	:unitMultiplier: The unit multiplier of the controlled quantity. Default: None
	:unitSymbol: The unit of measure of the controlled quantity. Default: None
	:PowerSystemResource: Regulating device governed by this control output. Default: None
		'''

	cgmesProfile = IOPoint.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'controlType': [cgmesProfile.OP.value, ],
						'operationInProgress': [cgmesProfile.OP.value, ],
						'timeStamp': [cgmesProfile.OP.value, ],
						'unitMultiplier': [cgmesProfile.OP.value, ],
						'unitSymbol': [cgmesProfile.OP.value, ],
						'PowerSystemResource': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IOPoint: \n' + IOPoint.__doc__ 

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
