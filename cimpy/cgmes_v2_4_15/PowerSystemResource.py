from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class PowerSystemResource(IdentifiedObject):
    """
    A power system resource can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

    :Controls: Regulating device governed by this control output. Default: "list"
    :Location: Location of this power system resource. Default: None
    :Measurements: The power system resource that contains the measurement. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.GL.value, Profile.SSH.value, ],
        "Controls": [Profile.EQ.value, ],
        "Location": [Profile.GL.value, ],
        "Measurements": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, Controls = "list", Location = None, Measurements = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Controls = Controls
        self.Location = Location
        self.Measurements = Measurements

    def __str__(self):
        str = "class=PowerSystemResource\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
