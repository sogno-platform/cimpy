from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """
    Describes the tap model for an asymmetrical phase shifting transformer in which the difference voltage vector adds to the in-phase winding. The out-of-phase winding is the transformer end where the tap changer is located.  The angle between the in-phase and out-of-phase windings is named the winding connection angle. The phase shift depends on both the difference voltage magnitude and the winding connection angle.

    :windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift. The out-of-phase winding produces what is known as the difference voltage.  Setting this angle to 90 degrees is not the same as a symmetrical transformer. The attribute can only be multiples of 30 degrees.  The allowed range is -150 degrees to 150 degrees excluding 0. Default: 0.0
    """

    cgmesProfile = PhaseTapChangerNonLinear.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "windingConnectionAngle": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PhaseTapChangerNonLinear: \n"
        + PhaseTapChangerNonLinear.__doc__
    )

    def __init__(self, windingConnectionAngle=0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.windingConnectionAngle = windingConnectionAngle

    def __str__(self):
        str = "class=PhaseTapChangerAsymmetrical\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
