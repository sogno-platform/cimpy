from .LoadDynamics import LoadDynamics
from .CGMESProfile import Profile


class LoadAggregate(LoadDynamics):
    """
    Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.

    :LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load. Default: None
    :LoadStatic: Aggregate static load associated with this aggregate load. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "LoadMotor": [Profile.DY.value, ],
        "LoadStatic": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class LoadDynamics:\n" + LoadDynamics.__doc__

    def __init__(self, LoadMotor = None, LoadStatic = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadMotor = LoadMotor
        self.LoadStatic = LoadStatic

    def __str__(self):
        str = "class=LoadAggregate\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
