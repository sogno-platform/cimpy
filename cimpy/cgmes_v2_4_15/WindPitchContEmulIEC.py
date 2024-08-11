from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindPitchContEmulIEC(IdentifiedObject):
    """
    Pitch control emulator model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.1.

    :WindGenTurbineType2IEC: Wind turbine type 2 model with which this Pitch control emulator model is associated. Default: None
    :kdroop: Power error gain (). It is case dependent parameter. Default: 0.0
    :kipce: Pitch control emulator integral constant (). It is type dependent parameter. Default: 0.0
    :komegaaero: Aerodynamic power change vs. omegachange (). It is case dependent parameter. Default: 0.0
    :kppce: Pitch control emulator proportional constant (). It is type dependent parameter. Default: 0.0
    :omegaref: Rotor speed in initial steady state (omega). It is case dependent parameter. Default: 0.0
    :pimax: Maximum steady state power (). It is case dependent parameter. Default: 0.0
    :pimin: Minimum steady state power (). It is case dependent parameter. Default: 0.0
    :t1: First time constant in pitch control lag (). It is type dependent parameter. Default: 0.0
    :t2: Second time constant in pitch control lag (). It is type dependent parameter. Default: 0.0
    :tpe: Time constant in generator air gap power lag (). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindGenTurbineType2IEC": [Profile.DY.value, ],
        "kdroop": [Profile.DY.value, ],
        "kipce": [Profile.DY.value, ],
        "komegaaero": [Profile.DY.value, ],
        "kppce": [Profile.DY.value, ],
        "omegaref": [Profile.DY.value, ],
        "pimax": [Profile.DY.value, ],
        "pimin": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "tpe": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindGenTurbineType2IEC = None, kdroop = 0.0, kipce = 0.0, komegaaero = 0.0, kppce = 0.0, omegaref = 0.0, pimax = 0.0, pimin = 0.0, t1 = 0.0, t2 = 0.0, tpe = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
        self.kdroop = kdroop
        self.kipce = kipce
        self.komegaaero = komegaaero
        self.kppce = kppce
        self.omegaref = omegaref
        self.pimax = pimax
        self.pimin = pimin
        self.t1 = t1
        self.t2 = t2
        self.tpe = tpe

    def __str__(self):
        str = "class=WindPitchContEmulIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
