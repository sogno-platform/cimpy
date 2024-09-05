from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """
    IEEE VAR controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005, 11.3.

    :tvarc: Var controller time delay (<i>T</i><i><sub>VARC</sub></i>) (&gt;= 0).  Typical value = 5. Default: 0
    :vvar: Synchronous machine power factor (<i>V</i><i><sub>VAR</sub></i>). Default: 0.0
    :vvarcbw: Var controller deadband (<i>V</i><i><sub>VARC_BW</sub></i>).  Typical value = 0,02. Default: 0.0
    :vvarref: Var controller reference (<i>V</i><i><sub>VARREF</sub></i>). Default: 0.0
    :vvtmax: Maximum machine terminal voltage needed for pf/VAr controller to be enabled (<i>V</i><i><sub>VTMAX</sub></i>) (&gt; PVFArType1IEEEVArController.vvtmin). Default: 0.0
    :vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (<i>V</i><i><sub>VTMIN</sub></i>) (&lt; PVFArType1IEEEVArController.vvtmax). Default: 0.0
    """

    cgmesProfile = PFVArControllerType1Dynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "tvarc": [
            cgmesProfile.DY.value,
        ],
        "vvar": [
            cgmesProfile.DY.value,
        ],
        "vvarcbw": [
            cgmesProfile.DY.value,
        ],
        "vvarref": [
            cgmesProfile.DY.value,
        ],
        "vvtmax": [
            cgmesProfile.DY.value,
        ],
        "vvtmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PFVArControllerType1Dynamics: \n"
        + PFVArControllerType1Dynamics.__doc__
    )

    def __init__(
        self,
        tvarc=0,
        vvar=0.0,
        vvarcbw=0.0,
        vvarref=0.0,
        vvtmax=0.0,
        vvtmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.tvarc = tvarc
        self.vvar = vvar
        self.vvarcbw = vvarcbw
        self.vvarref = vvarref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin

    def __str__(self):
        str = "class=PFVArType1IEEEVArController\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
