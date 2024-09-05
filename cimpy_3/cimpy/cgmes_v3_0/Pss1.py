from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS with three inputs (speed, frequency, power).

    :komega: Shaft speed power input gain (<i>K</i><i><sub>omega</sub></i>).  Typical value = 0. Default: 0.0
    :kf: Frequency power input gain (<i>K</i><i><sub>F</sub></i>).  Typical value = 5. Default: 0.0
    :kpe: Electric power input gain (<i>K</i><i><sub>PE</sub></i>).  Typical value = 0,3. Default: 0.0
    :pmin: Minimum power PSS enabling (<i>Pmin</i>).  Typical value = 0,25. Default: 0.0
    :ks: PSS gain (<i>Ks</i>).  Typical value = 1. Default: 0.0
    :vsmn: Stabilizer output maximum limit (<i>V</i><i><sub>SMN</sub></i>).  Typical value = -0,06. Default: 0.0
    :vsmx: Stabilizer output minimum limit (<i>V</i><i><sub>SMX</sub></i>).  Typical value = 0,06. Default: 0.0
    :tpe: Electric power filter time constant (<i>T</i><i><sub>PE</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
    :t5: Washout (<i>T</i><i><sub>5</sub></i>) (&gt;= 0).  Typical value = 3,5. Default: 0
    :t6: Filter time constant (<i>T</i><i><sub>6</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :t7: Lead/lag time constant (<i>T</i><i><sub>7</sub></i>) (&gt;= 0). If = 0, both blocks are bypassed.  Typical value = 0. Default: 0
    :t8: Lead/lag time constant (<i>T</i><i><sub>8</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :t9: Lead/lag time constant (<i>T</i><i><sub>9</sub></i>) (&gt;= 0).  If = 0, both blocks are bypassed.  Typical value = 0. Default: 0
    :t10: Lead/lag time constant (<i>T</i><i><sub>10</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vadat: <font color=`#0f0f0f`>Signal selector (<i>V</i><i><sub>ADAT</sub></i>).</font> <font color=`#0f0f0f`>true = closed (generator power is greater than <i>Pmin</i>)</font> <font color=`#0f0f0f`>false = open (<i>Pe</i> is smaller than <i>Pmin</i>).</font> <font color=`#0f0f0f`>Typical value = true.</font> Default: False
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "komega": [
            cgmesProfile.DY.value,
        ],
        "kf": [
            cgmesProfile.DY.value,
        ],
        "kpe": [
            cgmesProfile.DY.value,
        ],
        "pmin": [
            cgmesProfile.DY.value,
        ],
        "ks": [
            cgmesProfile.DY.value,
        ],
        "vsmn": [
            cgmesProfile.DY.value,
        ],
        "vsmx": [
            cgmesProfile.DY.value,
        ],
        "tpe": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "t7": [
            cgmesProfile.DY.value,
        ],
        "t8": [
            cgmesProfile.DY.value,
        ],
        "t9": [
            cgmesProfile.DY.value,
        ],
        "t10": [
            cgmesProfile.DY.value,
        ],
        "vadat": [
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
        komega=0.0,
        kf=0.0,
        kpe=0.0,
        pmin=0.0,
        ks=0.0,
        vsmn=0.0,
        vsmx=0.0,
        tpe=0,
        t5=0,
        t6=0,
        t7=0,
        t8=0,
        t9=0,
        t10=0,
        vadat=False,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.komega = komega
        self.kf = kf
        self.kpe = kpe
        self.pmin = pmin
        self.ks = ks
        self.vsmn = vsmn
        self.vsmx = vsmx
        self.tpe = tpe
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.t10 = t10
        self.vadat = vadat

    def __str__(self):
        str = "class=Pss1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
