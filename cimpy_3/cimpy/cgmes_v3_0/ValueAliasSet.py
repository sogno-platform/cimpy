from .IdentifiedObject import IdentifiedObject


class ValueAliasSet(IdentifiedObject):
    """
    Describes the translation of a set of values into a name and is intendend to facilitate custom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0-&gt;"Invalid", 1-&gt;"Open", 2-&gt;"Closed", 3-&gt;"Intermediate". Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.

    :Commands: The Commands using the set for translation. Default: "list"
    :Discretes: The Measurements using the set for translation. Default: "list"
    :RaiseLowerCommands: The Commands using the set for translation. Default: "list"
    :Values: The ValueToAlias mappings included in the set. Default: "list"
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
        ],
        "Commands": [
            cgmesProfile.OP.value,
        ],
        "Discretes": [
            cgmesProfile.OP.value,
        ],
        "RaiseLowerCommands": [
            cgmesProfile.OP.value,
        ],
        "Values": [
            cgmesProfile.OP.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        Commands="list",
        Discretes="list",
        RaiseLowerCommands="list",
        Values="list",
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.Commands = Commands
        self.Discretes = Discretes
        self.RaiseLowerCommands = RaiseLowerCommands
        self.Values = Values

    def __str__(self):
        str = "class=ValueAliasSet\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
