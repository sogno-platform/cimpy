from .Base import Base


class TownDetail(Base):
    """
    Town details, in the context of address.

    :code: Town code. Default: ''
    :section: Town section. For example, it is common for there to be 36 sections per township. Default: ''
    :name: Town name. Default: ''
    :stateOrProvince: Name of the state or province. Default: ''
    :country: Name of the country. Default: ''
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.GL.value,
        ],
        "code": [
            cgmesProfile.GL.value,
        ],
        "section": [
            cgmesProfile.GL.value,
        ],
        "name": [
            cgmesProfile.GL.value,
        ],
        "stateOrProvince": [
            cgmesProfile.GL.value,
        ],
        "country": [
            cgmesProfile.GL.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        code="",
        section="",
        name="",
        stateOrProvince="",
        country="",
    ):

        self.code = code
        self.section = section
        self.name = name
        self.stateOrProvince = stateOrProvince
        self.country = country

    def __str__(self):
        str = "class=TownDetail\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
