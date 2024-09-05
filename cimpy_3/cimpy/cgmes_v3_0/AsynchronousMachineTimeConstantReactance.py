from .AsynchronousMachineDynamics import AsynchronousMachineDynamics


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """
    Parameter details: <ol> 	<li>If <i>X'' </i>=<i> X'</i>, a single cage (one equivalent rotor winding per axis) is modelled.</li> 	<li>The "<i>p</i>" in the attribute names is a substitution for a "prime" in the usual parameter notation, e.g. <i>tpo</i> refers to <i>T'o</i>.</li> </ol> The parameters used for models expressed in time constant reactance form include: - RotatingMachine.ratedS (<i>MVAbase</i>); - RotatingMachineDynamics.damping (<i>D</i>); - RotatingMachineDynamics.inertia (<i>H</i>); - RotatingMachineDynamics.saturationFactor (<i>S1</i>); - RotatingMachineDynamics.saturationFactor120 (<i>S12</i>); - RotatingMachineDynamics.statorLeakageReactance (<i>Xl</i>); - RotatingMachineDynamics.statorResistance (<i>Rs</i>); - .xs (<i>Xs</i>); - .xp (<i>X'</i>); - .xpp (<i>X''</i>); - .tpo (<i>T'o</i>); - .tppo (<i>T''o</i>).

    :xs: Synchronous reactance (<i>Xs</i>) (&gt;= AsynchronousMachineTimeConstantReactance.xp).  Typical value = 1,8. Default: 0.0
    :xp: Transient reactance (unsaturated) (<i>X`</i>) (&gt;= AsynchronousMachineTimeConstantReactance.xpp).  Typical value = 0,5. Default: 0.0
    :xpp: Subtransient reactance (unsaturated) (<i>X``</i>) (&gt; RotatingMachineDynamics.statorLeakageReactance).  Typical value = 0,2. Default: 0.0
    :tpo: Transient rotor time constant (<i>T`o</i>) (&gt; AsynchronousMachineTimeConstantReactance.tppo).  Typical value = 5. Default: 0
    :tppo: Subtransient rotor time constant (<i>T``o</i>) (&gt; 0).  Typical value = 0,03. Default: 0
    """

    cgmesProfile = AsynchronousMachineDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "xs": [
            cgmesProfile.DY.value,
        ],
        "xp": [
            cgmesProfile.DY.value,
        ],
        "xpp": [
            cgmesProfile.DY.value,
        ],
        "tpo": [
            cgmesProfile.DY.value,
        ],
        "tppo": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class AsynchronousMachineDynamics: \n"
        + AsynchronousMachineDynamics.__doc__
    )

    def __init__(self, xs=0.0, xp=0.0, xpp=0.0, tpo=0, tppo=0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.xs = xs
        self.xp = xp
        self.xpp = xpp
        self.tpo = tpo
        self.tppo = tppo

    def __str__(self):
        str = "class=AsynchronousMachineTimeConstantReactance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
