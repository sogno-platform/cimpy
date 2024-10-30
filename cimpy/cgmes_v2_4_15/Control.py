from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class Control(IdentifiedObject):
    """
    Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.

    :PowerSystemResource: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator. Default: None
    :controlType: Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. Default: ''
    :operationInProgress: Indicates that a client is currently sending control commands that has not completed. Default: False
    :timeStamp: The last time a control output was sent. Default: ''
    :unitMultiplier: The unit multiplier of the controlled quantity. Default: None
    :unitSymbol: The unit of measure of the controlled quantity. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "PowerSystemResource": [Profile.EQ.value, ],
        "controlType": [Profile.EQ.value, ],
        "operationInProgress": [Profile.EQ.value, ],
        "timeStamp": [Profile.EQ.value, ],
        "unitMultiplier": [Profile.EQ.value, ],
        "unitSymbol": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, PowerSystemResource = None, controlType = '', operationInProgress = False, timeStamp = '', unitMultiplier = None, unitSymbol = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.PowerSystemResource = PowerSystemResource
        self.controlType = controlType
        self.operationInProgress = operationInProgress
        self.timeStamp = timeStamp
        self.unitMultiplier = unitMultiplier
        self.unitSymbol = unitSymbol

    def __str__(self):
        str = "class=Control\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
