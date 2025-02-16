from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.8.

    :WindGenTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated. Default: None
    :dthetamax: Maximum pitch positive ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 0.0
    :dthetamin: Maximum pitch negative ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 0.0
    :kic: Power PI controller integration gain (). It is type dependent parameter. Default: 0.0
    :kiomega: Speed PI controller integration gain (). It is type dependent parameter. Default: 0.0
    :kpc: Power PI controller proportional gain (). It is type dependent parameter. Default: 0.0
    :kpomega: Speed PI controller proportional gain (). It is type dependent parameter. Default: 0.0
    :kpx: Pitch cross coupling gain (K). It is type dependent parameter. Default: 0.0
    :thetamax: Maximum pitch angle (). It is type dependent parameter. Default: 0.0
    :thetamin: Minimum pitch angle (). It is type dependent parameter. Default: 0.0
    :ttheta: Pitch time constant (t). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindGenTurbineType3IEC": [Profile.DY.value, ],
        "dthetamax": [Profile.DY.value, ],
        "dthetamin": [Profile.DY.value, ],
        "kic": [Profile.DY.value, ],
        "kiomega": [Profile.DY.value, ],
        "kpc": [Profile.DY.value, ],
        "kpomega": [Profile.DY.value, ],
        "kpx": [Profile.DY.value, ],
        "thetamax": [Profile.DY.value, ],
        "thetamin": [Profile.DY.value, ],
        "ttheta": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindGenTurbineType3IEC = None, dthetamax = 0.0, dthetamin = 0.0, kic = 0.0, kiomega = 0.0, kpc = 0.0, kpomega = 0.0, kpx = 0.0, thetamax = 0.0, thetamin = 0.0, ttheta = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
        self.dthetamax = dthetamax
        self.dthetamin = dthetamin
        self.kic = kic
        self.kiomega = kiomega
        self.kpc = kpc
        self.kpomega = kpomega
        self.kpx = kpx
        self.thetamax = thetamax
        self.thetamin = thetamin
        self.ttheta = ttheta

    def __str__(self):
        str = "class=WindContPitchAngleIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
