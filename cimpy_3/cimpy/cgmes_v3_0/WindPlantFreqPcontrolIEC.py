from .IdentifiedObject import IdentifiedObject


class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """
    Frequency and active power controller model. Reference: IEC 61400-27-1:2015, Annex D.

    :WindDynamicsLookupTable: The wind dynamics lookup table associated with this frequency and active power wind plant model. Default: "list"
    :dprefmax: Maximum ramp rate of <i>p</i><i><sub>WTref</sub></i> request from the plant controller to the wind turbines (<i>dp</i><i><sub>refmax</sub></i>) (&gt; WindPlantFreqPcontrolIEC.dprefmin). It is a case-dependent parameter. Default: 0.0
    :dprefmin: Minimum (negative) ramp rate of <i>p</i><i><sub>WTref</sub></i> request from the plant controller to the wind turbines (<i>dp</i><i><sub>refmin</sub></i>) (&lt; WindPlantFreqPcontrolIEC.dprefmax). It is a project-dependent parameter. Default: 0.0
    :dpwprefmax: Maximum positive ramp rate for wind plant power reference (<i>dp</i><i><sub>WPrefmax</sub></i>) (&gt; WindPlantFreqPcontrolIEC.dpwprefmin). It is a project-dependent parameter. Default: 0.0
    :dpwprefmin: Maximum negative ramp rate for wind plant power reference (<i>dp</i><i><sub>WPrefmin</sub></i>) (&lt; WindPlantFreqPcontrolIEC.dpwprefmax). It is a project-dependent parameter. Default: 0.0
    :prefmax: Maximum <i>p</i><i><sub>WTref</sub></i> request from the plant controller to the wind turbines (<i>p</i><i><sub>refmax</sub></i>) (&gt; WindPlantFreqPcontrolIEC.prefmin). It is a project-dependent parameter. Default: 0.0
    :prefmin: Minimum <i>p</i><i><sub>WTref</sub></i> request from the plant controller to the wind turbines (<i>p</i><i><sub>refmin</sub></i>) (&lt; WindPlantFreqPcontrolIEC.prefmax). It is a project-dependent parameter. Default: 0.0
    :kiwpp: Plant P controller integral gain (<i>K</i><i><sub>IWPp</sub></i>). It is a project-dependent parameter. Default: 0.0
    :kiwppmax: Maximum PI integrator term (<i>K</i><i><sub>IWPpmax</sub></i>) (&gt; WindPlantFreqPcontrolIEC.kiwppmin). It is a project-dependent parameter. Default: 0.0
    :kiwppmin: Minimum PI integrator term (<i>K</i><i><sub>IWPpmin</sub></i>) (&lt; WindPlantFreqPcontrolIEC.kiwppmax). It is a project-dependent parameter. Default: 0.0
    :kpwpp: Plant P controller proportional gain (<i>K</i><i><sub>PWPp</sub></i>). It is a project-dependent parameter. Default: 0.0
    :kwppref: Power reference gain (<i>K</i><i><sub>WPpref</sub></i>). It is a project-dependent parameter. Default: 0.0
    :tpft: Lead time constant in reference value transfer function (<i>T</i><i><sub>pft</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
    :tpfv: Lag time constant in reference value transfer function (<i>T</i><i><sub>pfv</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
    :twpffiltp: Filter time constant for frequency measurement (<i>T</i><i><sub>WPffiltp</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
    :twppfiltp: Filter time constant for active power measurement (<i>T</i><i><sub>WPpfiltp</sub></i>) (&gt;= 0). It is a project-dependent parameter. Default: 0
    :WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindDynamicsLookupTable": [
            cgmesProfile.DY.value,
        ],
        "dprefmax": [
            cgmesProfile.DY.value,
        ],
        "dprefmin": [
            cgmesProfile.DY.value,
        ],
        "dpwprefmax": [
            cgmesProfile.DY.value,
        ],
        "dpwprefmin": [
            cgmesProfile.DY.value,
        ],
        "prefmax": [
            cgmesProfile.DY.value,
        ],
        "prefmin": [
            cgmesProfile.DY.value,
        ],
        "kiwpp": [
            cgmesProfile.DY.value,
        ],
        "kiwppmax": [
            cgmesProfile.DY.value,
        ],
        "kiwppmin": [
            cgmesProfile.DY.value,
        ],
        "kpwpp": [
            cgmesProfile.DY.value,
        ],
        "kwppref": [
            cgmesProfile.DY.value,
        ],
        "tpft": [
            cgmesProfile.DY.value,
        ],
        "tpfv": [
            cgmesProfile.DY.value,
        ],
        "twpffiltp": [
            cgmesProfile.DY.value,
        ],
        "twppfiltp": [
            cgmesProfile.DY.value,
        ],
        "WindPlantIEC": [
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
        dprefmax=0.0,
        dprefmin=0.0,
        dpwprefmax=0.0,
        dpwprefmin=0.0,
        prefmax=0.0,
        prefmin=0.0,
        kiwpp=0.0,
        kiwppmax=0.0,
        kiwppmin=0.0,
        kpwpp=0.0,
        kwppref=0.0,
        tpft=0,
        tpfv=0,
        twpffiltp=0,
        twppfiltp=0,
        WindPlantIEC=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.dprefmax = dprefmax
        self.dprefmin = dprefmin
        self.dpwprefmax = dpwprefmax
        self.dpwprefmin = dpwprefmin
        self.prefmax = prefmax
        self.prefmin = prefmin
        self.kiwpp = kiwpp
        self.kiwppmax = kiwppmax
        self.kiwppmin = kiwppmin
        self.kpwpp = kpwpp
        self.kwppref = kwppref
        self.tpft = tpft
        self.tpfv = tpfv
        self.twpffiltp = twpffiltp
        self.twppfiltp = twppfiltp
        self.WindPlantIEC = WindPlantIEC

    def __str__(self):
        str = "class=WindPlantFreqPcontrolIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
