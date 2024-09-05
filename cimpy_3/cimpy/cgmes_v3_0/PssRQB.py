from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssRQB(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer type RQB. This power system stabilizer is intended to be used together with excitation system type ExcRQB, which is primarily used in nuclear or thermal generating units.

    :ki2: Speed input gain (<i>Ki2</i>). Typical value = 3,43. Default: 0.0
    :ki3: Electrical power input gain (<i>Ki3</i>). Typical value = -11,45. Default: 0.0
    :ki4: Mechanical power input gain (<i>Ki4</i>). Typical value = 11,86. Default: 0.0
    :t4m: Input time constant (<i>T4M</i>) (&gt;= 0). Typical value = 5. Default: 0
    :tomd: Speed delay (<i>TOMD</i>) (&gt;= 0). Typical value = 0,02. Default: 0
    :tomsl: Speed time constant (<i>TOMSL</i>) (&gt;= 0). Typical value = 0,04. Default: 0
    :t4mom: Speed time constant (<i>T4MOM</i>) (&gt;= 0). Typical value = 1,27. Default: 0
    :sibv: Speed deadband (<i>SIBV</i>). Typical value = 0,006. Default: 0.0
    :kdpm: Lead lag gain (<i>KDPM</i>). Typical value = 0,185. Default: 0.0
    :t4f: Lead lag time constant (<i>T4F</i>) (&gt;= 0). Typical value = 0,045. Default: 0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ki2": [
            cgmesProfile.DY.value,
        ],
        "ki3": [
            cgmesProfile.DY.value,
        ],
        "ki4": [
            cgmesProfile.DY.value,
        ],
        "t4m": [
            cgmesProfile.DY.value,
        ],
        "tomd": [
            cgmesProfile.DY.value,
        ],
        "tomsl": [
            cgmesProfile.DY.value,
        ],
        "t4mom": [
            cgmesProfile.DY.value,
        ],
        "sibv": [
            cgmesProfile.DY.value,
        ],
        "kdpm": [
            cgmesProfile.DY.value,
        ],
        "t4f": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemStabilizerDynamics: \n"
        + PowerSystemStabilizerDynamics.__doc__
    )

    def __init__(
        self,
        ki2=0.0,
        ki3=0.0,
        ki4=0.0,
        t4m=0,
        tomd=0,
        tomsl=0,
        t4mom=0,
        sibv=0.0,
        kdpm=0.0,
        t4f=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.ki2 = ki2
        self.ki3 = ki3
        self.ki4 = ki4
        self.t4m = t4m
        self.tomd = tomd
        self.tomsl = tomsl
        self.t4mom = t4mom
        self.sibv = sibv
        self.kdpm = kdpm
        self.t4f = t4f

    def __str__(self):
        str = "class=PssRQB\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
