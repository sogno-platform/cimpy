from .ShuntCompensator import ShuntCompensator
from .CGMESProfile import Profile


class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that differs.

    :NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "NonlinearShuntCompensatorPoints": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ShuntCompensator:\n" + ShuntCompensator.__doc__

    def __init__(self, NonlinearShuntCompensatorPoints = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.NonlinearShuntCompensatorPoints = NonlinearShuntCompensatorPoints

    def __str__(self):
        str = "class=NonlinearShuntCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
