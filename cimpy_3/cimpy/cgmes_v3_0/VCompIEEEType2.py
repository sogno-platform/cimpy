from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    <font color="#0f0f0f">Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover the following types of compensation: </font> <ul> 	<li><font color="#0f0f0f">reactive droop;</font></li> 	<li><font color="#0f0f0f">transformer-drop or line-drop compensation;</font></li> 	<li><font color="#0f0f0f">reactive differential compensation known also as cross-current compensation.</font></li> </ul> <font color="#0f0f0f">Reference: IEEE 421.5-2005, 4.</font>

    :tr: <font color=`#0f0f0f`>Time constant which is used for the combined voltage sensing and compensation signal (<i>Tr</i>) (&gt;= 0).</font> Default: 0
    :GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another generator. Default: "list"
    """

    cgmesProfile = VoltageCompensatorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "GenICompensationForGenJ": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class VoltageCompensatorDynamics: \n"
        + VoltageCompensatorDynamics.__doc__
    )

    def __init__(self, tr=0, GenICompensationForGenJ="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.tr = tr
        self.GenICompensationForGenJ = GenICompensationForGenJ

    def __str__(self):
        str = "class=VCompIEEEType2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
