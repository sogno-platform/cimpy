from .IdentifiedObject import IdentifiedObject


class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model. Reference: IEC 61400-27-1:2015, 5.6.5.2.

    :dthetamax: Maximum pitch positive ramp rate (<i>dtheta</i><i><sub>max</sub></i>) (&gt; WindContPitchAngleIEC.dthetamin). It is a type-dependent parameter. Unit = degrees / s. Default: 0.0
    :dthetamin: Maximum pitch negative ramp rate (<i>dtheta</i><i><sub>min</sub></i><i>)</i> (&lt; WindContPitchAngleIEC.dthetamax). It is a type-dependent parameter. Unit = degrees / s. Default: 0.0
    :kic: Power PI controller integration gain (<i>K</i><i><sub>Ic</sub></i>). It is a type-dependent parameter. Default: 0.0
    :kiomega: Speed PI controller integration gain (<i>K</i><i><sub>Iomega</sub></i>). It is a type-dependent parameter. Default: 0.0
    :kpc: Power PI controller proportional gain (<i>K</i><i><sub>Pc</sub></i>). It is a type-dependent parameter. Default: 0.0
    :kpomega: Speed PI controller proportional gain (<i>K</i><i><sub>Pomega</sub></i>). It is a type-dependent parameter. Default: 0.0
    :kpx: Pitch cross coupling gain (<i>K</i><i><sub>PX</sub></i>). It is a type-dependent parameter. Default: 0.0
    :thetamax: Maximum pitch angle (<i>theta</i><i><sub>max</sub></i>) (&gt; WindContPitchAngleIEC.thetamin). It is a type-dependent parameter. Default: 0.0
    :thetamin: Minimum pitch angle (<i>theta</i><i><sub>min</sub></i>) (&lt; WindContPitchAngleIEC.thetamax). It is a type-dependent parameter. Default: 0.0
    :ttheta: Pitch time constant (<i>ttheta</i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :WindTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "dthetamax": [
            cgmesProfile.DY.value,
        ],
        "dthetamin": [
            cgmesProfile.DY.value,
        ],
        "kic": [
            cgmesProfile.DY.value,
        ],
        "kiomega": [
            cgmesProfile.DY.value,
        ],
        "kpc": [
            cgmesProfile.DY.value,
        ],
        "kpomega": [
            cgmesProfile.DY.value,
        ],
        "kpx": [
            cgmesProfile.DY.value,
        ],
        "thetamax": [
            cgmesProfile.DY.value,
        ],
        "thetamin": [
            cgmesProfile.DY.value,
        ],
        "ttheta": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType3IEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        dthetamax=0.0,
        dthetamin=0.0,
        kic=0.0,
        kiomega=0.0,
        kpc=0.0,
        kpomega=0.0,
        kpx=0.0,
        thetamax=0.0,
        thetamin=0.0,
        ttheta=0,
        WindTurbineType3IEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

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
        self.WindTurbineType3IEC = WindTurbineType3IEC

    def __str__(self):
        str = "class=WindContPitchAngleIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
