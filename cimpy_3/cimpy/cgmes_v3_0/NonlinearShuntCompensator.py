from .ShuntCompensator import ShuntCompensator


class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber.

    :NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator. Default: "list"
    """

    cgmesProfile = ShuntCompensator.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "NonlinearShuntCompensatorPoints": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ShuntCompensator: \n"
        + ShuntCompensator.__doc__
    )

    def __init__(self, NonlinearShuntCompensatorPoints="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.NonlinearShuntCompensatorPoints = NonlinearShuntCompensatorPoints

    def __str__(self):
        str = "class=NonlinearShuntCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
