from .OperationalLimit import OperationalLimit


class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage. The use of operational VoltageLimit is preferred instead of limits defined at VoltageLevel. The operational VoltageLimits are used, if present.

    :value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. The attribute shall be a positive value or zero. Default: 0.0
    :normalValue: The normal limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. The attribute shall be a positive value or zero. Default: 0.0
    """

    cgmesProfile = OperationalLimit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "value": [
            cgmesProfile.SSH.value,
        ],
        "normalValue": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class OperationalLimit: \n"
        + OperationalLimit.__doc__
    )

    def __init__(self, value=0.0, normalValue=0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.value = value
        self.normalValue = normalValue

    def __str__(self):
        str = "class=VoltageLimit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
