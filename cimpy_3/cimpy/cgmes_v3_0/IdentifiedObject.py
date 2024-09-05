from .Base import Base


class IdentifiedObject(Base):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.

    :mRID: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. Default: ''
    :name: The name is any free human readable and possibly non unique text naming the object. Default: ''
    :description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. Default: ''
    :DiagramObjects: The diagram objects that are associated with the domain object. Default: "list"
    :energyIdentCodeEic: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. Default: ''
    :shortName: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. Default: ''
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.GL.value,
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.TP.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "mRID": [
            cgmesProfile.GL.value,
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.TP.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "name": [
            cgmesProfile.GL.value,
            cgmesProfile.DY.value,
            cgmesProfile.DL.value,
            cgmesProfile.TP.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
            cgmesProfile.SV.value,
        ],
        "description": [
            cgmesProfile.DY.value,
            cgmesProfile.DL.value,
            cgmesProfile.TP.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "DiagramObjects": [
            cgmesProfile.DL.value,
        ],
        "energyIdentCodeEic": [
            cgmesProfile.TP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "shortName": [
            cgmesProfile.TP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        mRID="",
        name="",
        description="",
        DiagramObjects="list",
        energyIdentCodeEic="",
        shortName="",
    ):

        self.mRID = mRID
        self.name = name
        self.description = description
        self.DiagramObjects = DiagramObjects
        self.energyIdentCodeEic = energyIdentCodeEic
        self.shortName = shortName

    def __str__(self):
        str = "class=IdentifiedObject\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
