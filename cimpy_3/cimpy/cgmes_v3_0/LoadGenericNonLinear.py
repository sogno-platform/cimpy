from .LoadDynamics import LoadDynamics


class LoadGenericNonLinear(LoadDynamics):
    """
    Generic non-linear dynamic (GNLD) load. This model can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as it can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

    :genericNonLinearLoadModelType: Type of generic non-linear load model. Default: None
    :tp: Time constant of lag function of active power (<i>T</i><i><sub>P</sub></i>) (&gt; 0). Default: 0
    :tq: Time constant of lag function of reactive power (<i>T</i><i><sub>Q</sub></i>) (&gt; 0). Default: 0
    :ls: Steady state voltage index for active power (<i>LS</i>). Default: 0.0
    :lt: Transient voltage index for active power (<i>LT</i>). Default: 0.0
    :bs: Steady state voltage index for reactive power (<i>BS</i>). Default: 0.0
    :bt: Transient voltage index for reactive power (<i>BT</i>). Default: 0.0
    """

    cgmesProfile = LoadDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "genericNonLinearLoadModelType": [
            cgmesProfile.DY.value,
        ],
        "tp": [
            cgmesProfile.DY.value,
        ],
        "tq": [
            cgmesProfile.DY.value,
        ],
        "ls": [
            cgmesProfile.DY.value,
        ],
        "lt": [
            cgmesProfile.DY.value,
        ],
        "bs": [
            cgmesProfile.DY.value,
        ],
        "bt": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class LoadDynamics: \n" + LoadDynamics.__doc__
    )

    def __init__(
        self,
        genericNonLinearLoadModelType=None,
        tp=0,
        tq=0,
        ls=0.0,
        lt=0.0,
        bs=0.0,
        bt=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.genericNonLinearLoadModelType = genericNonLinearLoadModelType
        self.tp = tp
        self.tq = tq
        self.ls = ls
        self.lt = lt
        self.bs = bs
        self.bt = bt

    def __str__(self):
        str = "class=LoadGenericNonLinear\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
