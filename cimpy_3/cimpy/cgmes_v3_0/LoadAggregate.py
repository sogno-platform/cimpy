from .LoadDynamics import LoadDynamics


class LoadAggregate(LoadDynamics):
    """
    Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static (power flow) data. This load is usually the aggregation of many individual load devices and the load model is an approximate representation of the aggregate response of the load devices to system disturbances. Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can be used to represent the aggregate response of the motor components of the load.

    :LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load. Default: None
    :LoadStatic: Aggregate static load associated with this aggregate load. Default: None
    """

    cgmesProfile = LoadDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "LoadMotor": [
            cgmesProfile.DY.value,
        ],
        "LoadStatic": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class LoadDynamics: \n" + LoadDynamics.__doc__
    )

    def __init__(self, LoadMotor=None, LoadStatic=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadMotor = LoadMotor
        self.LoadStatic = LoadStatic

    def __str__(self):
        str = "class=LoadAggregate\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
