from .DynamicsFunctionBlock import DynamicsFunctionBlock


class CrossCompoundTurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor cross-compound function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

    :HighPressureSynchronousMachineDynamics: High-pressure synchronous machine with which this cross-compound turbine governor is associated. Default: None
    :LowPressureSynchronousMachineDynamics: Low-pressure synchronous machine with which this cross-compound turbine governor is associated. Default: None
    """

    cgmesProfile = DynamicsFunctionBlock.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "HighPressureSynchronousMachineDynamics": [
            cgmesProfile.DY.value,
        ],
        "LowPressureSynchronousMachineDynamics": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DynamicsFunctionBlock: \n"
        + DynamicsFunctionBlock.__doc__
    )

    def __init__(
        self,
        HighPressureSynchronousMachineDynamics=None,
        LowPressureSynchronousMachineDynamics=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.HighPressureSynchronousMachineDynamics = (
            HighPressureSynchronousMachineDynamics
        )
        self.LowPressureSynchronousMachineDynamics = (
            LowPressureSynchronousMachineDynamics
        )

    def __str__(self):
        str = "class=CrossCompoundTurbineGovernorDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
