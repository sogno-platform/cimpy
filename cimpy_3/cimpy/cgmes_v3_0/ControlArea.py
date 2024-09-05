from .PowerSystemResource import PowerSystemResource


class ControlArea(PowerSystemResource):
    """
    A control area is a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be used for a variety of purposes including automatic generation control, power flow solution area interchange control specification, and input to load forecasting. All generation and load within the area defined by the terminals on the border are considered in the area interchange control. Note that any number of overlapping control area specifications can be superimposed on the physical model. The following general principles apply to ControlArea: 1.  The control area orientation for net interchange is positive for an import, negative for an export. 2.  The control area net interchange is determined by summing flows in Terminals. The Terminals are identified by creating a set of TieFlow objects associated with a ControlArea object. Each TieFlow object identifies one Terminal. 3.  In a single network model, a tie between two control areas must be modelled in both control area specifications, such that the two representations of the tie flow sum to zero. 4.  The normal orientation of Terminal flow is positive for flow into the conducting equipment that owns the Terminal. (i.e. flow from a bus into a device is positive.) However, the orientation of each flow in the control area specification must align with the control area convention, i.e. import is positive. If the orientation of the Terminal flow referenced by a TieFlow is positive into the control area, then this is confirmed by setting TieFlow.positiveFlowIn flag TRUE. If not, the orientation must be reversed by setting the TieFlow.positiveFlowIn flag FALSE.

    :netInterchange: The specified positive net interchange into the control area, i.e. positive sign means flow into the area. Default: 0.0
    :pTolerance: Active power net interchange tolerance. The attribute shall be a positive value or zero. Default: 0.0
    :type: The primary type of control area definition used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.   A control area specified with primary type of automatic generation control could still be forecast and used as an interchange area in power flow analysis. Default: None
    :TieFlow: The tie flows associated with the control area. Default: "list"
    :ControlAreaGeneratingUnit: The generating unit specifications for the control area. Default: "list"
    :EnergyArea: The energy area that is forecast from this control area specification. Default: None
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "netInterchange": [
            cgmesProfile.SSH.value,
        ],
        "pTolerance": [
            cgmesProfile.SSH.value,
        ],
        "type": [
            cgmesProfile.EQ.value,
        ],
        "TieFlow": [
            cgmesProfile.EQ.value,
        ],
        "ControlAreaGeneratingUnit": [
            cgmesProfile.EQ.value,
        ],
        "EnergyArea": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self,
        netInterchange=0.0,
        pTolerance=0.0,
        type=None,
        TieFlow="list",
        ControlAreaGeneratingUnit="list",
        EnergyArea=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.netInterchange = netInterchange
        self.pTolerance = pTolerance
        self.type = type
        self.TieFlow = TieFlow
        self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit
        self.EnergyArea = EnergyArea

    def __str__(self):
        str = "class=ControlArea\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
