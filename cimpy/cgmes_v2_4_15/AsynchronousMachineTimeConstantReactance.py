from .AsynchronousMachineDynamics import AsynchronousMachineDynamics
from .CGMESProfile import Profile


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """
    The parameters used for models expressed in time constant reactance form include:

    :tpo: Transient rotor time constant (T`o) (> T``o).  Typical Value = 5. Default: 0.0
    :tppo: Subtransient rotor time constant (T``o) (> 0).  Typical Value = 0.03. Default: 0.0
    :xp: Transient reactance (unsaturated) (X`) (>=X``).  Typical Value = 0.5. Default: 0.0
    :xpp: Subtransient reactance (unsaturated) (X``) (> Xl).  Typical Value = 0.2. Default: 0.0
    :xs: Synchronous reactance (Xs) (>= X`).  Typical Value = 1.8. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "tpo": [Profile.DY.value, ],
        "tppo": [Profile.DY.value, ],
        "xp": [Profile.DY.value, ],
        "xpp": [Profile.DY.value, ],
        "xs": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class AsynchronousMachineDynamics:\n" + AsynchronousMachineDynamics.__doc__

    def __init__(self, tpo = 0.0, tppo = 0.0, xp = 0.0, xpp = 0.0, xs = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.tpo = tpo
        self.tppo = tppo
        self.xp = xp
        self.xpp = xpp
        self.xs = xs

    def __str__(self):
        str = "class=AsynchronousMachineTimeConstantReactance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
