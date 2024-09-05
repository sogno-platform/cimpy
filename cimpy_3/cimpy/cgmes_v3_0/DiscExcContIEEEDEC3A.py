from .DiscontinuousExcitationControlDynamics import (
    DiscontinuousExcitationControlDynamics,
)


class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing. Reference: IEEE 421.5-2005 12.4.

    :vtmin: Terminal undervoltage comparison level (<i>V</i><i><sub>TMIN</sub></i>). Default: 0.0
    :tdr: Reset time delay (<i>T</i><i><sub>DR</sub></i>) (&gt;= 0). Default: 0
    """

    cgmesProfile = DiscontinuousExcitationControlDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "vtmin": [
            cgmesProfile.DY.value,
        ],
        "tdr": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class DiscontinuousExcitationControlDynamics: \n"
        + DiscontinuousExcitationControlDynamics.__doc__
    )

    def __init__(self, vtmin=0.0, tdr=0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.vtmin = vtmin
        self.tdr = tdr

    def __str__(self):
        str = "class=DiscExcContIEEEDEC3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
