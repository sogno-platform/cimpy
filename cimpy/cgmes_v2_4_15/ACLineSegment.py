from .Conductor import Conductor
from .CGMESProfile import Profile


class ACLineSegment(Conductor):
    """
    A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use  attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances. The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines  may have slightly different BaseVoltage.nominalVoltages and  variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

    :b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 0.0
    :bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. Default: 0.0
    :g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    :gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    :r: Positive sequence series resistance of the entire line section. Default: 0.0
    :r0: Zero sequence series resistance of the entire line section. Default: 0.0
    :shortCircuitEndTemperature: Maximum permitted temperature at the end of SC for the calculation of minimum short-circuit currents. Used for short circuit data exchange according to IEC 60909 Default: 0.0
    :x: Positive sequence series reactance of the entire line section. Default: 0.0
    :x0: Zero sequence series reactance of the entire line section. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "b0ch": [Profile.EQ.value, ],
        "bch": [Profile.EQ.value, ],
        "g0ch": [Profile.EQ.value, ],
        "gch": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
        "r0": [Profile.EQ.value, ],
        "shortCircuitEndTemperature": [Profile.EQ.value, ],
        "x": [Profile.EQ.value, ],
        "x0": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Conductor:\n" + Conductor.__doc__

    def __init__(self, b0ch = 0.0, bch = 0.0, g0ch = 0.0, gch = 0.0, r = 0.0, r0 = 0.0, shortCircuitEndTemperature = 0.0, x = 0.0, x0 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.b0ch = b0ch
        self.bch = bch
        self.g0ch = g0ch
        self.gch = gch
        self.r = r
        self.r0 = r0
        self.shortCircuitEndTemperature = shortCircuitEndTemperature
        self.x = x
        self.x0 = x0

    def __str__(self):
        str = "class=ACLineSegment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
