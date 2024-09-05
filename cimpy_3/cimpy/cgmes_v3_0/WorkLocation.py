from .Location import Location


class WorkLocation(Location):
    """
    Information about a particular location for various forms of work.

    """

    cgmesProfile = Location.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.GL.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Location: \n" + Location.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=WorkLocation\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
