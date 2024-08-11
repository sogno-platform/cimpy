from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindDynamicsLookupTable(IdentifiedObject):
    """
    The class models a look up table for the purpose of wind standard models.

    :WindContCurrLimIEC: The wind dynamics lookup table associated with this current control limitation model. Default: None
    :WindContPType3IEC: The wind dynamics lookup table associated with this P control type 3 model. Default: None
    :WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated. Default: None
    :WindPlantFreqPcontrolIEC: The wind dynamics lookup table associated with this frequency and active power wind plant model. Default: None
    :input: Input value (x) for the lookup table function. Default: 0.0
    :lookupTableFunctionType: Type of the lookup table function. Default: None
    :output: Output value (y) for the lookup table function. Default: 0.0
    :sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindContCurrLimIEC": [Profile.DY.value, ],
        "WindContPType3IEC": [Profile.DY.value, ],
        "WindContRotorRIEC": [Profile.DY.value, ],
        "WindPlantFreqPcontrolIEC": [Profile.DY.value, ],
        "input": [Profile.DY.value, ],
        "lookupTableFunctionType": [Profile.DY.value, ],
        "output": [Profile.DY.value, ],
        "sequence": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindContCurrLimIEC = None, WindContPType3IEC = None, WindContRotorRIEC = None, WindPlantFreqPcontrolIEC = None, input = 0.0, lookupTableFunctionType = None, output = 0.0, sequence = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindContCurrLimIEC = WindContCurrLimIEC
        self.WindContPType3IEC = WindContPType3IEC
        self.WindContRotorRIEC = WindContRotorRIEC
        self.WindPlantFreqPcontrolIEC = WindPlantFreqPcontrolIEC
        self.input = input
        self.lookupTableFunctionType = lookupTableFunctionType
        self.output = output
        self.sequence = sequence

    def __str__(self):
        str = "class=WindDynamicsLookupTable\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
