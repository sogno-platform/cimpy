from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    <font color="#0f0f0f">Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is common to all excitation system models described in the IEEE Standard. </font> <font color="#0f0f0f">Parameter details:</font> <ol> 	<li><font color="#0f0f0f">If <i>Rc</i> and <i>Xc</i> are set to zero, the l</font>oad compensation is not employed and the behaviour is as a simple sensing circuit.</li> </ol> <ol> 	<li>If all parameters (<i>Rc</i>, <i>Xc</i> and <i>Tr</i>) are set to zero, the standard model VCompIEEEType1 is bypassed.</li> </ol> Reference: IEEE 421.5-2005 4.

    :rc: <font color=`#0f0f0f`>Resistive component of compensation of a generator (<i>Rc</i>) (&gt;= 0).</font> Default: 0.0
    :xc: <font color=`#0f0f0f`>Reactive component of compensation of a generator (<i>Xc</i>) (&gt;= 0).</font> Default: 0.0
    :tr: <font color=`#0f0f0f`>Time constant which is used for the combined voltage sensing and compensation signal (<i>Tr</i>) (&gt;= 0).</font> Default: 0
    """

    cgmesProfile = VoltageCompensatorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "rc": [
            cgmesProfile.DY.value,
        ],
        "xc": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class VoltageCompensatorDynamics: \n"
        + VoltageCompensatorDynamics.__doc__
    )

    def __init__(self, rc=0.0, xc=0.0, tr=0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.rc = rc
        self.xc = xc
        self.tr = tr

    def __str__(self):
        str = "class=VCompIEEEType1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
