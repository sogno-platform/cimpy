from .DCEquipmentContainer import DCEquipmentContainer
from .CGMESProfile import Profile


class DCConverterUnit(DCEquipmentContainer):
    """
    Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the point of common coupling - DC side, essentially one or more converters, together with one or more converter transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any, used for conversion.

    :Substation:  Default: None
    :operationMode:  Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Substation": [Profile.EQ.value, ],
        "operationMode": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class DCEquipmentContainer:\n" + DCEquipmentContainer.__doc__

    def __init__(self, Substation = None, operationMode = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Substation = Substation
        self.operationMode = operationMode

    def __str__(self):
        str = "class=DCConverterUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
