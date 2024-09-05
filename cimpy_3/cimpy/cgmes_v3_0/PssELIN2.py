from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssELIN2(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

    :ts1: Time constant (<i>Ts1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :ts2: Time constant (<i>Ts2</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :ts3: Time constant (<i>Ts3</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :ts4: Time constant (<i>Ts4</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :ts5: Time constant (<i>Ts5</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :ts6: Time constant (<i>Ts6</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :ks1: Gain (<i>Ks1</i>).  Typical value = 1. Default: 0.0
    :ks2: Gain (<i>Ks2</i>).  Typical value = 0,1. Default: 0.0
    :ppss: Coefficient (<i>p_PSS</i>) (&gt;= 0 and &lt;= 4).  Typical value = 0,1. Default: 0.0
    :apss: Coefficient (<i>a_PSS</i>).  Typical value = 0,1. Default: 0.0
    :psslim: PSS limiter (<i>psslim</i>).  Typical value = 0,1. Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ts1": [
            cgmesProfile.DY.value,
        ],
        "ts2": [
            cgmesProfile.DY.value,
        ],
        "ts3": [
            cgmesProfile.DY.value,
        ],
        "ts4": [
            cgmesProfile.DY.value,
        ],
        "ts5": [
            cgmesProfile.DY.value,
        ],
        "ts6": [
            cgmesProfile.DY.value,
        ],
        "ks1": [
            cgmesProfile.DY.value,
        ],
        "ks2": [
            cgmesProfile.DY.value,
        ],
        "ppss": [
            cgmesProfile.DY.value,
        ],
        "apss": [
            cgmesProfile.DY.value,
        ],
        "psslim": [
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
        ts1=0,
        ts2=0,
        ts3=0,
        ts4=0,
        ts5=0,
        ts6=0,
        ks1=0.0,
        ks2=0.0,
        ppss=0.0,
        apss=0.0,
        psslim=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.ts1 = ts1
        self.ts2 = ts2
        self.ts3 = ts3
        self.ts4 = ts4
        self.ts5 = ts5
        self.ts6 = ts6
        self.ks1 = ks1
        self.ks2 = ks2
        self.ppss = ppss
        self.apss = apss
        self.psslim = psslim

    def __str__(self):
        str = "class=PssELIN2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
