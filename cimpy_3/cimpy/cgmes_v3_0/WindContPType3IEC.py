from .IdentifiedObject import IdentifiedObject


class WindContPType3IEC(IdentifiedObject):
    """
    P control model type 3. Reference: IEC 61400-27-1:2015, 5.6.5.4.

    :dpmax: Maximum wind turbine power ramp rate (<i>dp</i><i><sub>max</sub></i>). It is a type-dependent parameter. Default: 0.0
    :dprefmax: Maximum ramp rate of wind turbine reference power (<i>dp</i><i><sub>refmax</sub></i>). It is a project-dependent parameter. Default: 0.0
    :dprefmin: Minimum ramp rate of wind turbine reference power (<i>dp</i><i><sub>refmin</sub></i>). It is a project-dependent parameter. Default: 0.0
    :dthetamax: Ramp limitation of torque, required in some grid codes (<i>dt</i><i><sub>max</sub></i>). It is a project-dependent parameter. Default: 0.0
    :dthetamaxuvrt: Limitation of torque rise rate during UVRT (<i>dtheta</i><i><sub>maxUVRT</sub></i>). It is a project-dependent parameter. Default: 0.0
    :kdtd: Gain for active drive train damping (<i>K</i><i><sub>DTD</sub></i>). It is a type-dependent parameter. Default: 0.0
    :kip: PI controller integration parameter (<i>K</i><sub>Ip</sub>). It is a type-dependent parameter. Default: 0.0
    :kpp: PI controller proportional gain (<i>K</i><sub>Pp</sub>). It is a type-dependent parameter. Default: 0.0
    :mpuvrt: Enable UVRT power control mode (<i>M</i><i><sub>pUVRT</sub></i><sub>)</sub>.  It is a project-dependent parameter. true = voltage control (1 in the IEC model) false = reactive power control (0 in the IEC model). Default: False
    :omegaoffset: Offset to reference value that limits controller action during rotor speed changes (<i>omega</i><i><sub>offset</sub></i>). It is a case-dependent parameter. Default: 0.0
    :pdtdmax: Maximum active drive train damping power (<i>p</i><sub>DTDmax</sub>). It is a type-dependent parameter. Default: 0.0
    :tdvs: Time<sub> </sub>delay after deep voltage sags (<i>T</i><i><sub>DVS</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
    :thetaemin: Minimum electrical generator torque (<i>t</i><sub>emin</sub>). It is a type-dependent parameter. Default: 0.0
    :thetauscale: Voltage scaling factor of reset-torque (<i>t</i><sub>uscale</sub>). It is a project-dependent parameter. Default: 0.0
    :tomegafiltp3: Filter time constant for generator speed measurement (<i>T</i><sub>omegafiltp3</sub>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :tpfiltp3: Filter time constant for power measurement (<i>T</i><sub>pfiltp3</sub>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :tpord: Time constant in power order lag (<i>T</i><sub>pord</sub>). It is a type-dependent parameter. Default: 0.0
    :tufiltp3: Filter time constant for voltage measurement (<i>T</i><sub>ufiltp3</sub>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :tomegaref: Time constant in speed reference filter (<i>T</i><sub>omega,ref</sub>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :udvs: Voltage limit for hold UVRT status after deep voltage sags (<i>u</i><i><sub>DVS</sub></i>). It is a project-dependent parameter. Default: 0.0
    :updip: Voltage dip threshold for P-control (<i>u</i><sub>Pdip</sub>).  Part of turbine control, often different (e.g 0.8) from converter thresholds. It is a project-dependent parameter. Default: 0.0
    :omegadtd: Active drive train damping frequency (<i>omega</i><i><sub>DTD</sub></i>). It can be calculated from two mass model parameters. It is a type-dependent parameter. Default: 0.0
    :zeta: Coefficient for active drive train damping (<i>zeta</i>). It is a type-dependent parameter. Default: 0.0
    :WindTurbineType3IEC: Wind turbine type 3 model with which this wind control P type 3 model is associated. Default: None
    :WindDynamicsLookupTable: The wind dynamics lookup table associated with this P control type 3 model. Default: "list"
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "dpmax": [
            cgmesProfile.DY.value,
        ],
        "dprefmax": [
            cgmesProfile.DY.value,
        ],
        "dprefmin": [
            cgmesProfile.DY.value,
        ],
        "dthetamax": [
            cgmesProfile.DY.value,
        ],
        "dthetamaxuvrt": [
            cgmesProfile.DY.value,
        ],
        "kdtd": [
            cgmesProfile.DY.value,
        ],
        "kip": [
            cgmesProfile.DY.value,
        ],
        "kpp": [
            cgmesProfile.DY.value,
        ],
        "mpuvrt": [
            cgmesProfile.DY.value,
        ],
        "omegaoffset": [
            cgmesProfile.DY.value,
        ],
        "pdtdmax": [
            cgmesProfile.DY.value,
        ],
        "tdvs": [
            cgmesProfile.DY.value,
        ],
        "thetaemin": [
            cgmesProfile.DY.value,
        ],
        "thetauscale": [
            cgmesProfile.DY.value,
        ],
        "tomegafiltp3": [
            cgmesProfile.DY.value,
        ],
        "tpfiltp3": [
            cgmesProfile.DY.value,
        ],
        "tpord": [
            cgmesProfile.DY.value,
        ],
        "tufiltp3": [
            cgmesProfile.DY.value,
        ],
        "tomegaref": [
            cgmesProfile.DY.value,
        ],
        "udvs": [
            cgmesProfile.DY.value,
        ],
        "updip": [
            cgmesProfile.DY.value,
        ],
        "omegadtd": [
            cgmesProfile.DY.value,
        ],
        "zeta": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType3IEC": [
            cgmesProfile.DY.value,
        ],
        "WindDynamicsLookupTable": [
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
        dpmax=0.0,
        dprefmax=0.0,
        dprefmin=0.0,
        dthetamax=0.0,
        dthetamaxuvrt=0.0,
        kdtd=0.0,
        kip=0.0,
        kpp=0.0,
        mpuvrt=False,
        omegaoffset=0.0,
        pdtdmax=0.0,
        tdvs=0,
        thetaemin=0.0,
        thetauscale=0.0,
        tomegafiltp3=0,
        tpfiltp3=0,
        tpord=0.0,
        tufiltp3=0,
        tomegaref=0,
        udvs=0.0,
        updip=0.0,
        omegadtd=0.0,
        zeta=0.0,
        WindTurbineType3IEC=None,
        WindDynamicsLookupTable="list",
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.dpmax = dpmax
        self.dprefmax = dprefmax
        self.dprefmin = dprefmin
        self.dthetamax = dthetamax
        self.dthetamaxuvrt = dthetamaxuvrt
        self.kdtd = kdtd
        self.kip = kip
        self.kpp = kpp
        self.mpuvrt = mpuvrt
        self.omegaoffset = omegaoffset
        self.pdtdmax = pdtdmax
        self.tdvs = tdvs
        self.thetaemin = thetaemin
        self.thetauscale = thetauscale
        self.tomegafiltp3 = tomegafiltp3
        self.tpfiltp3 = tpfiltp3
        self.tpord = tpord
        self.tufiltp3 = tufiltp3
        self.tomegaref = tomegaref
        self.udvs = udvs
        self.updip = updip
        self.omegadtd = omegadtd
        self.zeta = zeta
        self.WindTurbineType3IEC = WindTurbineType3IEC
        self.WindDynamicsLookupTable = WindDynamicsLookupTable

    def __str__(self):
        str = "class=WindContPType3IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
