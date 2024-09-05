from .Switch import Switch


class Jumper(Switch):
    """
    A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can potentially be modelled by other equipment types.

    """

    cgmesProfile = Switch.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Switch: \n" + Switch.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=Jumper\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
