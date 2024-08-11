from .SynchronousMachineDynamics import SynchronousMachineDynamics
from .CGMESProfile import Profile


class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The several variations differ in the following ways:   It is not necessary for each simulation tool to have separate models for each of the model types.  The same model can often be used for several types by alternative logic within the model.  Also, differences in saturation representation may not result in significant model performance differences so model substitutions are often acceptable.

    :efdBaseRatio: Ratio of Efd bases of exciter and generator models.  Typical Value = 1. Default: 0.0
    :ifdBaseType: Excitation base system mode.  Typical Value = ifag. Default: None
    :ifdBaseValue: Ifd base current if .ifdBaseType = other. Not needed if .ifdBaseType not = other.   Unit = A.  Typical Value = 0. Default: 0.0
    :saturationFactor120QAxis: Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).  Typical Value = 0.12. Default: 0.0
    :saturationFactorQAxis: Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value = 0.02. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdBaseRatio": [Profile.DY.value, ],
        "ifdBaseType": [Profile.DY.value, ],
        "ifdBaseValue": [Profile.DY.value, ],
        "saturationFactor120QAxis": [Profile.DY.value, ],
        "saturationFactorQAxis": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class SynchronousMachineDynamics:\n" + SynchronousMachineDynamics.__doc__

    def __init__(self, efdBaseRatio = 0.0, ifdBaseType = None, ifdBaseValue = 0.0, saturationFactor120QAxis = 0.0, saturationFactorQAxis = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdBaseRatio = efdBaseRatio
        self.ifdBaseType = ifdBaseType
        self.ifdBaseValue = ifdBaseValue
        self.saturationFactor120QAxis = saturationFactor120QAxis
        self.saturationFactorQAxis = saturationFactorQAxis

    def __str__(self):
        str = "class=SynchronousMachineDetailed\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
