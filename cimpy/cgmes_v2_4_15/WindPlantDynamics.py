from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class WindPlantDynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant IEC and user defined wind plants including their control models.

    :RemoteInputSignal: The wind plant using the remote signal. Default: None
    :WindTurbineType3or4Dynamics: The wind turbine type 3 or 4 associated with this wind plant. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
        "WindTurbineType3or4Dynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, RemoteInputSignal = None, WindTurbineType3or4Dynamics = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RemoteInputSignal = RemoteInputSignal
        self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics

    def __str__(self):
        str = "class=WindPlantDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
