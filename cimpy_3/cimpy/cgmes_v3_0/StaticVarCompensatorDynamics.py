from .DynamicsFunctionBlock import DynamicsFunctionBlock


class StaticVarCompensatorDynamics(DynamicsFunctionBlock):
    """
    Static var compensator whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

    :StaticVarCompensator: Static Var Compensator to which Static Var Compensator dynamics model applies. Default: None
    """

    cgmesProfile = DynamicsFunctionBlock.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "StaticVarCompensator": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DynamicsFunctionBlock: \n"
        + DynamicsFunctionBlock.__doc__
    )

    def __init__(self, StaticVarCompensator=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.StaticVarCompensator = StaticVarCompensator

    def __str__(self):
        str = "class=StaticVarCompensatorDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
