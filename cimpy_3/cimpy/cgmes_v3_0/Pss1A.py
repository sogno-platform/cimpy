from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss1A(PowerSystemStabilizerDynamics):
    """
    Single input power system stabilizer. It is a modified version in order to allow representation of various vendors' implementations on PSS type 1A.

    :inputSignalType: Type of input signal (rotorAngularFrequencyDeviation, busFrequencyDeviation, generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative). Default: None
    :a1: Notch filter parameter (<i>A</i><i><sub>1</sub></i>). Default: 0.0
    :a2: Notch filter parameter (<i>A</i><i><sub>2</sub></i>). Default: 0.0
    :t1: Lead/lag time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0). Default: 0
    :t2: Lead/lag time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0). Default: 0
    :t3: Lead/lag time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0). Default: 0
    :t4: Lead/lag time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0). Default: 0
    :t5: Washout time constant (<i>T</i><i><sub>5</sub></i>) (&gt;= 0). Default: 0
    :t6: Transducer time constant (<i>T</i><i><sub>6</sub></i>) (&gt;= 0). Default: 0
    :ks: Stabilizer gain (<i>K</i><i><sub>s</sub></i>). Default: 0.0
    :vrmax: Maximum stabilizer output (<i>Vrmax</i>) (&gt; Pss1A.vrmin). Default: 0.0
    :vrmin: Minimum stabilizer output (<i>Vrmin</i>) (&lt; Pss1A.vrmax). Default: 0.0
    :vcu: Stabilizer input cutoff threshold (<i>Vcu</i>). Default: 0.0
    :vcl: Stabilizer input cutoff threshold (<i>Vcl</i>). Default: 0.0
    :a3: Notch filter parameter (<i>A</i><i><sub>3</sub></i>). Default: 0.0
    :a4: Notch filter parameter (<i>A</i><i><sub>4</sub></i>). Default: 0.0
    :a5: Notch filter parameter (<i>A</i><i><sub>5</sub></i>). Default: 0.0
    :a6: Notch filter parameter (<i>A</i><i><sub>6</sub></i>). Default: 0.0
    :a7: Notch filter parameter (<i>A</i><i><sub>7</sub></i>). Default: 0.0
    :a8: Notch filter parameter (<i>A</i><i><sub>8</sub></i>). Default: 0.0
    :kd: Selector (<i>Kd</i>).  true = e<sup>-sTdelay</sup> used false = e<sup>-sTdelay</sup> not used. Default: False
    :tdelay: Time constant (<i>Tdelay</i>) (&gt;= 0). Default: 0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "inputSignalType": [
            cgmesProfile.DY.value,
        ],
        "a1": [
            cgmesProfile.DY.value,
        ],
        "a2": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "t5": [
            cgmesProfile.DY.value,
        ],
        "t6": [
            cgmesProfile.DY.value,
        ],
        "ks": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "vcu": [
            cgmesProfile.DY.value,
        ],
        "vcl": [
            cgmesProfile.DY.value,
        ],
        "a3": [
            cgmesProfile.DY.value,
        ],
        "a4": [
            cgmesProfile.DY.value,
        ],
        "a5": [
            cgmesProfile.DY.value,
        ],
        "a6": [
            cgmesProfile.DY.value,
        ],
        "a7": [
            cgmesProfile.DY.value,
        ],
        "a8": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "tdelay": [
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
        inputSignalType=None,
        a1=0.0,
        a2=0.0,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        t5=0,
        t6=0,
        ks=0.0,
        vrmax=0.0,
        vrmin=0.0,
        vcu=0.0,
        vcl=0.0,
        a3=0.0,
        a4=0.0,
        a5=0.0,
        a6=0.0,
        a7=0.0,
        a8=0.0,
        kd=False,
        tdelay=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.inputSignalType = inputSignalType
        self.a1 = a1
        self.a2 = a2
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.ks = ks
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.vcu = vcu
        self.vcl = vcl
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.kd = kd
        self.tdelay = tdelay

    def __str__(self):
        str = "class=Pss1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
