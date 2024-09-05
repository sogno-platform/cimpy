from .Base import Base


class StreetDetail(Base):
    """
    Street details, in the context of address.

    :number: Designator of the specific location on the street. Default: ''
    :name: Name of the street. Default: ''
    :suffix: Suffix to the street name. For example: North, South, East, West. Default: ''
    :prefix: Prefix to the street name. For example: North, South, East, West. Default: ''
    :type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. Default: ''
    :code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner`s department or surveyor general`s mapping system, that allocate global reference codes to streets. Default: ''
    :buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. Default: ''
    :suiteNumber: Number of the apartment or suite. Default: ''
    :addressGeneral: First line of a free form address or some additional address information (for example a mail stop). Default: ''
    :addressGeneral2: (if applicable) Second line of a free form address. Default: ''
    :addressGeneral3: (if applicable) Third line of a free form address. Default: ''
    :withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default). Default: False
    :floorIdentification: The identification by name or number, expressed as text, of the floor in the building as part of this address. Default: ''
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.GL.value,
        ],
        "number": [
            cgmesProfile.GL.value,
        ],
        "name": [
            cgmesProfile.GL.value,
        ],
        "suffix": [
            cgmesProfile.GL.value,
        ],
        "prefix": [
            cgmesProfile.GL.value,
        ],
        "type": [
            cgmesProfile.GL.value,
        ],
        "code": [
            cgmesProfile.GL.value,
        ],
        "buildingName": [
            cgmesProfile.GL.value,
        ],
        "suiteNumber": [
            cgmesProfile.GL.value,
        ],
        "addressGeneral": [
            cgmesProfile.GL.value,
        ],
        "addressGeneral2": [
            cgmesProfile.GL.value,
        ],
        "addressGeneral3": [
            cgmesProfile.GL.value,
        ],
        "withinTownLimits": [
            cgmesProfile.GL.value,
        ],
        "floorIdentification": [
            cgmesProfile.GL.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        number="",
        name="",
        suffix="",
        prefix="",
        type="",
        code="",
        buildingName="",
        suiteNumber="",
        addressGeneral="",
        addressGeneral2="",
        addressGeneral3="",
        withinTownLimits=False,
        floorIdentification="",
    ):

        self.number = number
        self.name = name
        self.suffix = suffix
        self.prefix = prefix
        self.type = type
        self.code = code
        self.buildingName = buildingName
        self.suiteNumber = suiteNumber
        self.addressGeneral = addressGeneral
        self.addressGeneral2 = addressGeneral2
        self.addressGeneral3 = addressGeneral3
        self.withinTownLimits = withinTownLimits
        self.floorIdentification = floorIdentification

    def __str__(self):
        str = "class=StreetDetail\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
