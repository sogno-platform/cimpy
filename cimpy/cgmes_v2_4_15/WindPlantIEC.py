from .WindPlantDynamics import WindPlantDynamics
from .CGMESProfile import Profile


class WindPlantIEC(WindPlantDynamics):
    """
    Simplified IEC type plant level model.   Reference: IEC 61400-27-1, AnnexE.

    :WindPlantFreqPcontrolIEC: Wind plant frequency and active power control model associated with this wind plant. Default: None
    :WindPlantReactiveControlIEC: Wind plant reactive control model associated with this wind plant. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindPlantFreqPcontrolIEC": [Profile.DY.value, ],
        "WindPlantReactiveControlIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindPlantDynamics:\n" + WindPlantDynamics.__doc__

    def __init__(self, WindPlantFreqPcontrolIEC = None, WindPlantReactiveControlIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindPlantFreqPcontrolIEC = WindPlantFreqPcontrolIEC
        self.WindPlantReactiveControlIEC = WindPlantReactiveControlIEC

    def __str__(self):
        str = "class=WindPlantIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
