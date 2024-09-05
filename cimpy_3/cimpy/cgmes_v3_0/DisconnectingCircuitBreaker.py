from .Breaker import Breaker


class DisconnectingCircuitBreaker(Breaker):
    """
    A circuit breaking device including disconnecting function, eliminating the need for separate disconnectors.

    """

    cgmesProfile = Breaker.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Breaker: \n" + Breaker.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=DisconnectingCircuitBreaker\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
