from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindAeroLinearIEC(IdentifiedObject):
    """
    The linearised aerodynamic model.    Reference: IEC Standard 614000-27-1 Section 6.6.1.2.

    :WindGenTurbineType3IEC: Wind generator type 3 model with which this wind aerodynamic model is associated. Default: None
    :dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (). It is case dependent parameter. Default: 0.0
    :dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (). It is case dependent parameter. Default: 0.0
    :omegazero: Rotor speed if the wind turbine is not derated (). It is case dependent parameter. Default: 0.0
    :pavail: Available aerodynamic power (). It is case dependent parameter. Default: 0.0
    :thetazero: Pitch angle if the wind turbine is not derated (). It is case dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindGenTurbineType3IEC": [Profile.DY.value, ],
        "dpomega": [Profile.DY.value, ],
        "dptheta": [Profile.DY.value, ],
        "omegazero": [Profile.DY.value, ],
        "pavail": [Profile.DY.value, ],
        "thetazero": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindGenTurbineType3IEC = None, dpomega = 0.0, dptheta = 0.0, omegazero = 0.0, pavail = 0.0, thetazero = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindGenTurbineType3IEC = WindGenTurbineType3IEC
        self.dpomega = dpomega
        self.dptheta = dptheta
        self.omegazero = omegazero
        self.pavail = pavail
        self.thetazero = thetazero

    def __str__(self):
        str = "class=WindAeroLinearIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
