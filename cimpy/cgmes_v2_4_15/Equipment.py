from .PowerSystemResource import PowerSystemResource
from .CGMESProfile import Profile


class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    :EquipmentContainer: Container of this equipment. Default: None
    :OperationalLimitSet: The operational limit sets associated with this equipment. Default: "list"
    :aggregate: The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be power transformers or synchronous machines operating in parallel modeled as a single aggregate power transformer or aggregate synchronous machine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.SSH.value, ],
        "EquipmentContainer": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "OperationalLimitSet": [Profile.EQ.value, ],
        "aggregate": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemResource:\n" + PowerSystemResource.__doc__

    def __init__(self, EquipmentContainer = None, OperationalLimitSet = "list", aggregate = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EquipmentContainer = EquipmentContainer
        self.OperationalLimitSet = OperationalLimitSet
        self.aggregate = aggregate

    def __str__(self):
        str = "class=Equipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
