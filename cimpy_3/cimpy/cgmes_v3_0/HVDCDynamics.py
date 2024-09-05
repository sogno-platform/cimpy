from .DynamicsFunctionBlock import DynamicsFunctionBlock


class HVDCDynamics(DynamicsFunctionBlock):
    """
    HVDC whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

    """

    cgmesProfile = DynamicsFunctionBlock.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DynamicsFunctionBlock: \n"
        + DynamicsFunctionBlock.__doc__
    )

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=HVDCDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
