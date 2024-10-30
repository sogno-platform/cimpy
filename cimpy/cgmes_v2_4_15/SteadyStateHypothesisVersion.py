from .Base import Base
from .CGMESProfile import Profile


class SteadyStateHypothesisVersion(Base):
    """
    Version details.

    :baseUML: Base UML provided by CIM model manager. Default: ''
    :baseURI: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
    :date: Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: ''
    :differenceModelURI: Difference model URI defined by IEC 61970-552. Default: ''
    :entsoeUML: UML provided by ENTSO-E. Default: ''
    :entsoeURI: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/SteadyStateHypothesis/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
    :modelDescriptionURI: Model Description URI defined by IEC 61970-552. Default: ''
    :namespaceRDF: RDF namespace. Default: ''
    :namespaceUML: CIM UML namespace. Default: ''
    :shortName: The short name of the profile used in profile documentation. Default: ''
    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
        "baseUML": [Profile.SSH.value, ],
        "baseURI": [Profile.SSH.value, ],
        "date": [Profile.SSH.value, ],
        "differenceModelURI": [Profile.SSH.value, ],
        "entsoeUML": [Profile.SSH.value, ],
        "entsoeURI": [Profile.SSH.value, ],
        "modelDescriptionURI": [Profile.SSH.value, ],
        "namespaceRDF": [Profile.SSH.value, ],
        "namespaceUML": [Profile.SSH.value, ],
        "shortName": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SSH.value


    def __init__(self, baseUML = '', baseURI = '', date = '', differenceModelURI = '', entsoeUML = '', entsoeURI = '', modelDescriptionURI = '', namespaceRDF = '', namespaceUML = '', shortName = ''):

        self.baseUML = baseUML
        self.baseURI = baseURI
        self.date = date
        self.differenceModelURI = differenceModelURI
        self.entsoeUML = entsoeUML
        self.entsoeURI = entsoeURI
        self.modelDescriptionURI = modelDescriptionURI
        self.namespaceRDF = namespaceRDF
        self.namespaceUML = namespaceUML
        self.shortName = shortName

    def __str__(self):
        str = "class=SteadyStateHypothesisVersion\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str