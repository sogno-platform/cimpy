from .ACDCConverter import ACDCConverter
from .CGMESProfile import Profile


class CsConverter(ACDCConverter):
    """
    DC side of the current source converter (CSC).

    :alpha: Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC state variable, result from power flow. Default: 0.0
    :gamma: Extinction angle. CSC state variable, result from power flow. Default: 0.0
    :maxAlpha: Maximum firing angle. CSC configuration data used in power flow. Default: 0.0
    :maxGamma: Maximum extinction angle. CSC configuration data used in power flow. Default: 0.0
    :maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. Converter configuration data use in power flow. Default: 0.0
    :minAlpha: Minimum firing angle. CSC configuration data used in power flow. Default: 0.0
    :minGamma: Minimum extinction angle. CSC configuration data used in power flow. Default: 0.0
    :minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. CSC configuration data used in power flow. Default: 0.0
    :operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. CSC control variable used in power flow. Default: None
    :pPccControl:  Default: None
    :ratedIdc: Rated converter DC current, also called IdN. Converter configuration data used in power flow. Default: 0.0
    :targetAlpha: Target firing angle. CSC control variable used in power flow. Default: 0.0
    :targetGamma: Target extinction angle. CSC  control variable used in power flow. Default: 0.0
    :targetIdc: DC current target value. CSC control variable used in power flow. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "alpha": [Profile.SV.value, ],
        "gamma": [Profile.SV.value, ],
        "maxAlpha": [Profile.EQ.value, ],
        "maxGamma": [Profile.EQ.value, ],
        "maxIdc": [Profile.EQ.value, ],
        "minAlpha": [Profile.EQ.value, ],
        "minGamma": [Profile.EQ.value, ],
        "minIdc": [Profile.EQ.value, ],
        "operatingMode": [Profile.SSH.value, ],
        "pPccControl": [Profile.SSH.value, ],
        "ratedIdc": [Profile.EQ.value, ],
        "targetAlpha": [Profile.SSH.value, ],
        "targetGamma": [Profile.SSH.value, ],
        "targetIdc": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ACDCConverter:\n" + ACDCConverter.__doc__

    def __init__(self, alpha = 0.0, gamma = 0.0, maxAlpha = 0.0, maxGamma = 0.0, maxIdc = 0.0, minAlpha = 0.0, minGamma = 0.0, minIdc = 0.0, operatingMode = None, pPccControl = None, ratedIdc = 0.0, targetAlpha = 0.0, targetGamma = 0.0, targetIdc = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.alpha = alpha
        self.gamma = gamma
        self.maxAlpha = maxAlpha
        self.maxGamma = maxGamma
        self.maxIdc = maxIdc
        self.minAlpha = minAlpha
        self.minGamma = minGamma
        self.minIdc = minIdc
        self.operatingMode = operatingMode
        self.pPccControl = pPccControl
        self.ratedIdc = ratedIdc
        self.targetAlpha = targetAlpha
        self.targetGamma = targetGamma
        self.targetIdc = targetIdc

    def __str__(self):
        str = "class=CsConverter\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
