from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    :ConductingEquipment: Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: "list"
    :TopologicalNode: The topological nodes at the base voltage. Default: "list"
    :TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation. Default: "list"
    :VoltageLevel: The voltage levels having this base voltage. Default: "list"
    :nominalVoltage: The power system resource`s base voltage. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, Profile.TP_BD.value, Profile.TP.value, ],
        "ConductingEquipment": [Profile.EQ.value, ],
        "TopologicalNode": [Profile.TP_BD.value, Profile.TP.value, ],
        "TransformerEnds": [Profile.EQ.value, ],
        "VoltageLevel": [Profile.EQ.value, ],
        "nominalVoltage": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ConductingEquipment = "list", TopologicalNode = "list", TransformerEnds = "list", VoltageLevel = "list", nominalVoltage = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ConductingEquipment = ConductingEquipment
        self.TopologicalNode = TopologicalNode
        self.TransformerEnds = TransformerEnds
        self.VoltageLevel = VoltageLevel
        self.nominalVoltage = nominalVoltage

    def __str__(self):
        str = "class=BaseVoltage\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
