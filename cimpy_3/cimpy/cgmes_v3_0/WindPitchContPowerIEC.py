from .IdentifiedObject import IdentifiedObject


class WindPitchContPowerIEC(IdentifiedObject):
    """
    Pitch control power model. Reference: IEC 61400-27-1:2015, 5.6.5.1.

    :WindDynamicsLookupTable: The wind dynamics lookup table associated with this pitch control power model. Default: "list"
    :WindGenTurbineType1bIEC: Wind turbine type 1B model with which this pitch control power model is associated. Default: None
    :WindGenTurbineType2IEC: Wind turbine type 2 model with which this pitch control power model is associated. Default: None
    :dpmax: Rate limit for increasing power (<i>dp</i><i><sub>max</sub></i>) (&gt; WindPitchContPowerIEC.dpmin). It is a type-dependent parameter. Default: 0.0
    :dpmin: Rate limit for decreasing power (<i>dp</i><i><sub>min</sub></i>) (&lt; WindPitchContPowerIEC.dpmax). It is a type-dependent parameter. Default: 0.0
    :pmin: Minimum power setting (<i>p</i><i><sub>min</sub></i>). It is a type-dependent parameter. Default: 0.0
    :pset: If <i>p</i><i><sub>init</sub></i><sub> </sub>&lt; <i>p</i><i><sub>set</sub></i><sub> </sub>then power will be ramped down to <i>p</i><i><sub>min</sub></i>. It is (<i>p</i><i><sub>set</sub></i>) in the IEC 61400-27-1:2015. It is a type-dependent parameter. Default: 0.0
    :t1: Lag time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :tr: Voltage measurement time constant (<i>T</i><i><sub>r</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :uuvrt: Dip detection threshold (<i>u</i><i><sub>UVRT</sub></i>). It is a type-dependent parameter. Default: 0.0
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindDynamicsLookupTable": [
            cgmesProfile.DY.value,
        ],
        "WindGenTurbineType1bIEC": [
            cgmesProfile.DY.value,
        ],
        "WindGenTurbineType2IEC": [
            cgmesProfile.DY.value,
        ],
        "dpmax": [
            cgmesProfile.DY.value,
        ],
        "dpmin": [
            cgmesProfile.DY.value,
        ],
        "pmin": [
            cgmesProfile.DY.value,
        ],
        "pset": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "uuvrt": [
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
        WindDynamicsLookupTable="list",
        WindGenTurbineType1bIEC=None,
        WindGenTurbineType2IEC=None,
        dpmax=0.0,
        dpmin=0.0,
        pmin=0.0,
        pset=0.0,
        t1=0,
        tr=0,
        uuvrt=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.WindGenTurbineType1bIEC = WindGenTurbineType1bIEC
        self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
        self.dpmax = dpmax
        self.dpmin = dpmin
        self.pmin = pmin
        self.pset = pset
        self.t1 = t1
        self.tr = tr
        self.uuvrt = uuvrt

    def __str__(self):
        str = "class=WindPitchContPowerIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
