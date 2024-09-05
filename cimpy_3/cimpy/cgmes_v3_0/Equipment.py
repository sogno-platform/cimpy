from .PowerSystemResource import PowerSystemResource


class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    :inService: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. Default: False
    :aggregate: The aggregate flag provides an alternative way of representing an aggregated (equivalent) element. It is applicable in cases when the dedicated classes for equivalent equipment do not have all of the attributes necessary to represent the required level of detail.  In case the flag is set to `true` the single instance of equipment represents multiple pieces of equipment that have been modelled together as an aggregate equivalent obtained by a network reduction procedure. Examples would be power transformers or synchronous machines operating in parallel modelled as a single aggregate power transformer or aggregate synchronous machine.   The attribute is not used for EquivalentBranch, EquivalentShunt and EquivalentInjection. Default: False
    :normallyInService: Specifies the availability of the equipment under normal operating conditions. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. Default: False
    :EquipmentContainer: Container of this equipment. Default: None
    :OperationalLimitSet: The operational limit sets associated with this equipment. Default: "list"
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
            cgmesProfile.SC.value,
        ],
        "inService": [
            cgmesProfile.SSH.value,
        ],
        "aggregate": [
            cgmesProfile.EQ.value,
        ],
        "normallyInService": [
            cgmesProfile.EQ.value,
        ],
        "EquipmentContainer": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        # 						'OperationalLimitSet': [cgmesProfile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self,
        inService=False,
        aggregate=False,
        normallyInService=False,
        EquipmentContainer=None,
        OperationalLimitSet="list",
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.inService = inService
        self.aggregate = aggregate
        self.normallyInService = normallyInService
        self.EquipmentContainer = EquipmentContainer
        self.OperationalLimitSet = OperationalLimitSet

    def __str__(self):
        str = "class=Equipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
