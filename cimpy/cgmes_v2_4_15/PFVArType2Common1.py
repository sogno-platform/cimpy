from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from .CGMESProfile import Profile


class PFVArType2Common1(PFVArControllerType2Dynamics):
    """
    Power factor / Reactive power regulator. This model represents the power factor or reactive power controller such as the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and compares it with the operator's set point.

    :j: Selector (J). true = control mode for reactive power false = control mode for power factor. Default: False
    :ki: Reset gain (Ki). Default: 0.0
    :kp: Proportional gain (Kp). Default: 0.0
    :max: Output limit (max). Default: 0.0
    :ref: Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This initialisation may override the value exchanged by this attribute to represent a plant operator`s change of the reference setting. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "j": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "max": [Profile.DY.value, ],
        "ref": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PFVArControllerType2Dynamics:\n" + PFVArControllerType2Dynamics.__doc__

    def __init__(self, j = False, ki = 0.0, kp = 0.0, max = 0.0, ref = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.j = j
        self.ki = ki
        self.kp = kp
        self.max = max
        self.ref = ref

    def __str__(self):
        str = "class=PFVArType2Common1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
