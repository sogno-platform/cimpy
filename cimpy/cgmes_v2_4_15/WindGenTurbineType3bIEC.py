from .WindGenTurbineType3IEC import WindGenTurbineType3IEC
from .CGMESProfile import Profile


class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
    """
    IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

    :fducw: Crowbar duration versus voltage variation look-up table (f()). It is case dependent parameter. Default: 0.0
    :mwtcwp: Crowbar control mode ().   The parameter is case dependent parameter. Default: False
    :tg: Current generation Time constant (). It is type dependent parameter. Default: 0.0
    :two: Time constant for crowbar washout filter (). It is case dependent parameter. Default: 0.0
    :xs: Electromagnetic transient reactance (x). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "fducw": [Profile.DY.value, ],
        "mwtcwp": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "two": [Profile.DY.value, ],
        "xs": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class WindGenTurbineType3IEC:\n" + WindGenTurbineType3IEC.__doc__

    def __init__(self, fducw = 0.0, mwtcwp = False, tg = 0.0, two = 0.0, xs = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.fducw = fducw
        self.mwtcwp = mwtcwp
        self.tg = tg
        self.two = two
        self.xs = xs

    def __str__(self):
        str = "class=WindGenTurbineType3bIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
