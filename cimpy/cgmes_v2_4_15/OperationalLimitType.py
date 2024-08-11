from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.

    :OperationalLimit: The operational limits associated with this type of limit. Default: "list"
    :acceptableDuration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. Default: 0.0
    :direction: The direction of the limit. Default: None
    :limitType: Types of limits defined in the ENTSO-E Operational Handbook Policy 3. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "OperationalLimit": [Profile.EQ.value, ],
        "acceptableDuration": [Profile.EQ.value, ],
        "direction": [Profile.EQ.value, ],
        "limitType": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, OperationalLimit = "list", acceptableDuration = 0.0, direction = None, limitType = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.OperationalLimit = OperationalLimit
        self.acceptableDuration = acceptableDuration
        self.direction = direction
        self.limitType = limitType

    def __str__(self):
        str = "class=OperationalLimitType\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
