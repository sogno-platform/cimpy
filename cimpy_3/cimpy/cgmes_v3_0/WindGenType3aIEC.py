from .WindGenType3IEC import WindGenType3IEC


class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC type 3A generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.2.

    :kpc: Current PI controller proportional gain (<i>K</i><i><sub>Pc</sub></i>). It is a type-dependent parameter. Default: 0.0
    :tic: Current PI controller integration time constant (<i>T</i><i><sub>Ic</sub></i>) (&gt;= 0). It is a type-dependent parameter. Default: 0
    :WindTurbineType4IEC: Wind turbine type 4 model with which this wind generator type 3A model is associated. Default: None
    """

    cgmesProfile = WindGenType3IEC.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "kpc": [
            cgmesProfile.DY.value,
        ],
        "tic": [
            cgmesProfile.DY.value,
        ],
        "WindTurbineType4IEC": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class WindGenType3IEC: \n" + WindGenType3IEC.__doc__
    )

    def __init__(self, kpc=0.0, tic=0, WindTurbineType4IEC=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kpc = kpc
        self.tic = tic
        self.WindTurbineType4IEC = WindTurbineType4IEC

    def __str__(self):
        str = "class=WindGenType3aIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
