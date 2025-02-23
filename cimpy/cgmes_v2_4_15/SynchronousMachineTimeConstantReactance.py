from .SynchronousMachineDetailed import SynchronousMachineDetailed
from .CGMESProfile import Profile


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    """
    Synchronous machine detailed modelling types are defined by the combination of the attributes SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.     The parameters used for models expressed in time constant reactance form include:

    :ks: Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.  Typical Value = 0. Default: 0.0
    :modelType: Type of synchronous machine model used in Dynamic simulation applications. Default: None
    :rotorType: Type of rotor on physical machine. Default: None
    :tc: Damping time constant for `Canay` reactance.  Typical Value = 0. Default: 0.0
    :tpdo: Direct-axis transient rotor time constant (T`do) (> T``do).  Typical Value = 5. Default: 0.0
    :tppdo: Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical Value = 0.03. Default: 0.0
    :tppqo: Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical Value = 0.03. Default: 0.0
    :tpqo: Quadrature-axis transient rotor time constant (T`qo) (> T``qo). Typical Value = 0.5. Default: 0.0
    :xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X``d) (> Xl).  Typical Value = 0.2. Default: 0.0
    :xDirectSync: Direct-axis synchronous reactance (Xd) (>= X`d). The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. Typical Value = 1.8. Default: 0.0
    :xDirectTrans: Direct-axis transient reactance (unsaturated) (X`d) (> =X``d).  Typical Value = 0.5. Default: 0.0
    :xQuadSubtrans: Quadrature-axis subtransient reactance (X``q) (> Xl).  Typical Value = 0.2. Default: 0.0
    :xQuadSync: Quadrature-axis synchronous reactance (Xq) (> =X`q). The ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.  Typical Value = 1.6. Default: 0.0
    :xQuadTrans: Quadrature-axis transient reactance (X`q) (> =X``q).  Typical Value = 0.3. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "modelType": [Profile.DY.value, ],
        "rotorType": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "tpdo": [Profile.DY.value, ],
        "tppdo": [Profile.DY.value, ],
        "tppqo": [Profile.DY.value, ],
        "tpqo": [Profile.DY.value, ],
        "xDirectSubtrans": [Profile.DY.value, ],
        "xDirectSync": [Profile.DY.value, ],
        "xDirectTrans": [Profile.DY.value, ],
        "xQuadSubtrans": [Profile.DY.value, ],
        "xQuadSync": [Profile.DY.value, ],
        "xQuadTrans": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class SynchronousMachineDetailed:\n" + SynchronousMachineDetailed.__doc__

    def __init__(self, ks = 0.0, modelType = None, rotorType = None, tc = 0.0, tpdo = 0.0, tppdo = 0.0, tppqo = 0.0, tpqo = 0.0, xDirectSubtrans = 0.0, xDirectSync = 0.0, xDirectTrans = 0.0, xQuadSubtrans = 0.0, xQuadSync = 0.0, xQuadTrans = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ks = ks
        self.modelType = modelType
        self.rotorType = rotorType
        self.tc = tc
        self.tpdo = tpdo
        self.tppdo = tppdo
        self.tppqo = tppqo
        self.tpqo = tpqo
        self.xDirectSubtrans = xDirectSubtrans
        self.xDirectSync = xDirectSync
        self.xDirectTrans = xDirectTrans
        self.xQuadSubtrans = xQuadSubtrans
        self.xQuadSync = xQuadSync
        self.xQuadTrans = xQuadTrans

    def __str__(self):
        str = "class=SynchronousMachineTimeConstantReactance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
