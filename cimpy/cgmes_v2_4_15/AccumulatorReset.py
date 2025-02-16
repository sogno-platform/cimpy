from .Control import Control
from .CGMESProfile import Profile


class AccumulatorReset(Control):
    """
    This command reset the counter value to zero.

    :AccumulatorValue: The accumulator value that is reset by the command. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "AccumulatorValue": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Control:\n" + Control.__doc__

    def __init__(self, AccumulatorValue = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AccumulatorValue = AccumulatorValue

    def __str__(self):
        str = "class=AccumulatorReset\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
