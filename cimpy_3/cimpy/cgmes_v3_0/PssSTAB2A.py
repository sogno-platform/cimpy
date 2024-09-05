from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSTAB2A(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer part of an ABB excitation system. [Footnote: ABB excitation systems are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

    :k2: Gain (<i>K2</i>).  Typical value = 1,0. Default: 0.0
    :k3: Gain (<i>K3</i>).  Typical value = 0,25. Default: 0.0
    :k4: Gain (<i>K4</i>).  Typical value = 0,075. Default: 0.0
    :k5: Gain (<i>K5</i>).  Typical value = 2,5. Default: 0.0
    :t2: Time constant (<i>T2</i>).  Typical value = 4,0. Default: 0
    :t3: Time constant (<i>T3</i>).  Typical value = 2,0. Default: 0
    :t5: Time constant (<i>T5</i>).  Typical value = 4,5. Default: 0
    :hlim: Stabilizer output limiter (<i>H</i><i><sub>LIM</sub></i>).  Typical value = 0,5. Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "k4": [
            cgmesProfile.DY.value,
        ],
        "k5": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "hlim": [
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
        k2=0.0,
        k3=0.0,
        k4=0.0,
        k5=0.0,
        t2=0,
        t3=0,
        t5=0,
        hlim=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.t2 = t2
        self.t3 = t3
        self.t5 = t5
        self.hlim = hlim

    def __str__(self):
        str = "class=PssSTAB2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
