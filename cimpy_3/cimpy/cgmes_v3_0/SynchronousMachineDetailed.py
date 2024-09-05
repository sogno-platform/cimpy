from .SynchronousMachineDynamics import SynchronousMachineDynamics


class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The several variations differ in the following ways: - the number of  equivalent windings that are included; - the way in which saturation is incorporated into the model; - whether or not "subtransient saliency" (<i>X''q</i> not = <i>X''d</i>) is represented. It is not necessary for each simulation tool to have separate models for each of the model types.  The same model can often be used for several types by alternative logic within the model.  Also, differences in saturation representation might not result in significant model performance differences so model substitutions are often acceptable.

    :saturationFactorQAxis: Quadrature-axis saturation factor at rated terminal voltage (<i>S1q</i>) (&gt;= 0). Typical value = 0,02. Default: 0.0
    :saturationFactor120QAxis: Quadrature-axis saturation factor at 120% of rated terminal voltage (<i>S12q</i>) (&gt;= SynchonousMachineDetailed.saturationFactorQAxis).  Typical value = 0,12. Default: 0.0
    :efdBaseRatio: Ratio (exciter voltage/generator voltage) of <i>Efd</i> bases of exciter and generator models (&gt; 0). Typical value = 1. Default: 0.0
    :ifdBaseType: Excitation base system mode. It should be equal to the value of <i>WLMDV</i> given by the user. <i>WLMDV</i> is the PU ratio between the field voltage and the excitation current: <i>Efd</i> = <i>WLMDV</i> x <i>Ifd</i>. Typical value = ifag. Default: None
    """

    cgmesProfile = SynchronousMachineDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "saturationFactorQAxis": [
            cgmesProfile.DY.value,
        ],
        "saturationFactor120QAxis": [
            cgmesProfile.DY.value,
        ],
        "efdBaseRatio": [
            cgmesProfile.DY.value,
        ],
        "ifdBaseType": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class SynchronousMachineDynamics: \n"
        + SynchronousMachineDynamics.__doc__
    )

    def __init__(
        self,
        saturationFactorQAxis=0.0,
        saturationFactor120QAxis=0.0,
        efdBaseRatio=0.0,
        ifdBaseType=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.saturationFactorQAxis = saturationFactorQAxis
        self.saturationFactor120QAxis = saturationFactor120QAxis
        self.efdBaseRatio = efdBaseRatio
        self.ifdBaseType = ifdBaseType

    def __str__(self):
        str = "class=SynchronousMachineDetailed\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
