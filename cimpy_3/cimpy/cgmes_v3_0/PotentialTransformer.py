from .Sensor import Sensor


class PotentialTransformer(Sensor):
    """
    Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.

    """

    cgmesProfile = Sensor.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Sensor: \n" + Sensor.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=PotentialTransformer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
