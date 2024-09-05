from .WindGenType3IEC import WindGenType3IEC


class WindGenType3bIEC(WindGenType3IEC):
    """
    IEC type 3B generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.3.

    :WindDynamicsLookupTable: The wind dynamics lookup table associated with this generator type 3B model. Default: "list"
    :mwtcwp: Crowbar control mode (<i>M</i><i><sub>WTcwp</sub></i>). It is a case-dependent parameter. true = 1 in the IEC model false = 0 in the IEC model. Default: False
    :tg: Current generation time constant (<i>T</i><i><sub>g</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :two: Time constant for crowbar washout filter (<i>T</i><i><sub>wo</sub></i>) (&gt;= 0). It is a case-dependent parameter. Default: 0
    """

    cgmesProfile = WindGenType3IEC.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "WindDynamicsLookupTable": [
            cgmesProfile.DY.value,
        ],
        "mwtcwp": [
            cgmesProfile.DY.value,
        ],
        "tg": [
            cgmesProfile.DY.value,
        ],
        "two": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindGenType3IEC: \n" + WindGenType3IEC.__doc__
    )

    def __init__(
        self,
        WindDynamicsLookupTable="list",
        mwtcwp=False,
        tg=0,
        two=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.mwtcwp = mwtcwp
        self.tg = tg
        self.two = two

    def __str__(self):
        str = "class=WindGenType3bIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
