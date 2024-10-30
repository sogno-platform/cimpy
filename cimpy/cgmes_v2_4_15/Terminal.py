from .ACDCTerminal import ACDCTerminal
from .CGMESProfile import Profile


class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

    :ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: None
    :ConnectivityNode: Terminals interconnected with zero impedance at a this connectivity node. Default: None
    :ConverterDCSides: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer. Default: "list"
    :HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch. Default: "list"
    :HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch. Default: "list"
    :RegulatingControl: The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node (bus in bus-branch model) or a connectivity node (detailed switch model).  Sometimes it is useful to model regulation at a terminal of a bus bar object since the bus bar can be present in both a bus-branch model or a model with switch detail. Default: None
    :RemoteInputSignal: Input signal coming from this terminal. Default: "list"
    :SvPowerFlow: The power flow state variable associated with the terminal. Default: None
    :TieFlow: The control area tie flows to which this terminal associates. Default: "list"
    :TopologicalNode: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: None
    :TransformerEnd: All transformer ends connected at this terminal. Default: "list"
    :phases: Represents the normal network phasing condition. If the attribute is missing three phases (ABC or ABCN) shall be assumed. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, Profile.TP.value, ],
        "ConductingEquipment": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, ],
        "ConnectivityNode": [Profile.EQ.value, ],
        "ConverterDCSides": [Profile.EQ.value, ],
        "HasFirstMutualCoupling": [Profile.EQ.value, ],
        "HasSecondMutualCoupling": [Profile.EQ.value, ],
        "RegulatingControl": [Profile.EQ.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
        "SvPowerFlow": [Profile.SV.value, ],
        "TieFlow": [Profile.EQ.value, ],
        "TopologicalNode": [Profile.TP.value, ],
        "TransformerEnd": [Profile.EQ.value, ],
        "phases": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ACDCTerminal:\n" + ACDCTerminal.__doc__

    def __init__(self, ConductingEquipment = None, ConnectivityNode = None, ConverterDCSides = "list", HasFirstMutualCoupling = "list", HasSecondMutualCoupling = "list", RegulatingControl = None, RemoteInputSignal = "list", SvPowerFlow = None, TieFlow = "list", TopologicalNode = None, TransformerEnd = "list", phases = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ConductingEquipment = ConductingEquipment
        self.ConnectivityNode = ConnectivityNode
        self.ConverterDCSides = ConverterDCSides
        self.HasFirstMutualCoupling = HasFirstMutualCoupling
        self.HasSecondMutualCoupling = HasSecondMutualCoupling
        self.RegulatingControl = RegulatingControl
        self.RemoteInputSignal = RemoteInputSignal
        self.SvPowerFlow = SvPowerFlow
        self.TieFlow = TieFlow
        self.TopologicalNode = TopologicalNode
        self.TransformerEnd = TransformerEnd
        self.phases = phases

    def __str__(self):
        str = "class=Terminal\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
