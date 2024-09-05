from .PowerSystemResource import PowerSystemResource


class BoundaryPoint(PowerSystemResource):
    """
    Designates a connection point at which one or more model authority sets shall connect to. The location of the connection point as well as other properties are agreed between organisations responsible for the interconnection, hence all attributes of the class represent this agreement.  It is primarily used in a boundary model authority set which can contain one or many BoundaryPoint-s among other Equipment-s and their connections.

    :fromEndIsoCode: The ISO code of the region which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes). The length of the string is 2 characters maximum. Default: ''
    :fromEndName: A human readable name with length of the string 64 characters maximum. It covers the following two cases: -if the Boundary point is placed on a tie-line, it is the name (IdentifiedObject.name) of the substation at which the `From` side of the tie-line is connected to. -if the Boundary point is placed in a substation, it is the name (IdentifiedObject.name) of the element (e.g. PowerTransformer, ACLineSegment, Switch, etc.) at which the `From` side of the Boundary point is connected to. Default: ''
    :fromEndNameTso: Identifies the name of the transmission system operator, distribution system operator or other entity at which the `From` side of the interconnection is connected to. The length of the string is 64 characters maximum. Default: ''
    :toEndIsoCode: The ISO code of the region which the `To` side of the Boundary point belongs to or is connected to. The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes). The length of the string is 2 characters maximum. Default: ''
    :toEndName: A human readable name with length of the string 64 characters maximum. It covers the following two cases: -if the Boundary point is placed on a tie-line, it is the name (IdentifiedObject.name) of the substation at which the `To` side of the tie-line is connected to. -if the Boundary point is placed in a substation, it is the name (IdentifiedObject.name) of the element (e.g. PowerTransformer, ACLineSegment, Switch, etc.) at which the `To` side of the Boundary point is connected to. Default: ''
    :toEndNameTso: Identifies the name of the transmission system operator, distribution system operator or other entity at which the `To` side of the interconnection is connected to. The length of the string is 64 characters maximum. Default: ''
    :isDirectCurrent: If true, this boundary point is a point of common coupling (PCC) of a direct current (DC) interconnection, otherwise the interconnection is AC (default). Default: False
    :isExcludedFromAreaInterchange: If true, this boundary point is on the interconnection that is excluded from control area interchange calculation and consequently has no related tie flows. Otherwise, the interconnection is included in control area interchange and a TieFlow is required at all sides of the boundary point (default). Default: False
    :ConnectivityNode: The connectivity node that is designated as a boundary point. Default: None
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "fromEndIsoCode": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "fromEndName": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "fromEndNameTso": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "toEndIsoCode": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "toEndName": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "toEndNameTso": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "isDirectCurrent": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "isExcludedFromAreaInterchange": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "ConnectivityNode": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self,
        fromEndIsoCode="",
        fromEndName="",
        fromEndNameTso="",
        toEndIsoCode="",
        toEndName="",
        toEndNameTso="",
        isDirectCurrent=False,
        isExcludedFromAreaInterchange=False,
        ConnectivityNode=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.fromEndIsoCode = fromEndIsoCode
        self.fromEndName = fromEndName
        self.fromEndNameTso = fromEndNameTso
        self.toEndIsoCode = toEndIsoCode
        self.toEndName = toEndName
        self.toEndNameTso = toEndNameTso
        self.isDirectCurrent = isDirectCurrent
        self.isExcludedFromAreaInterchange = isExcludedFromAreaInterchange
        self.ConnectivityNode = ConnectivityNode

    def __str__(self):
        str = "class=BoundaryPoint\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
