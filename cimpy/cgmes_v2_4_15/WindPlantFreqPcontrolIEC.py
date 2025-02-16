from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """
    Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.

    :WindDynamicsLookupTable: The frequency and active power wind plant control model with which this wind dynamics lookup table is associated. Default: "list"
    :WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated. Default: None
    :dprefmax: Maximum ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0
    :dprefmin: Minimum (negative) ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0
    :kiwpp: Plant P controller integral gain (). It is type dependent parameter. Default: 0.0
    :kpwpp: Plant P controller proportional gain (). It is type dependent parameter. Default: 0.0
    :prefmax: Maximum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0
    :prefmin: Minimum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0
    :tpft: Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 0.0
    :tpfv: Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 0.0
    :twpffilt: Filter time constant for frequency measurement (). It is type dependent parameter. Default: 0.0
    :twppfilt: Filter time constant for active power measurement (). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindDynamicsLookupTable": [Profile.DY.value, ],
        "WindPlantIEC": [Profile.DY.value, ],
        "dprefmax": [Profile.DY.value, ],
        "dprefmin": [Profile.DY.value, ],
        "kiwpp": [Profile.DY.value, ],
        "kpwpp": [Profile.DY.value, ],
        "prefmax": [Profile.DY.value, ],
        "prefmin": [Profile.DY.value, ],
        "tpft": [Profile.DY.value, ],
        "tpfv": [Profile.DY.value, ],
        "twpffilt": [Profile.DY.value, ],
        "twppfilt": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindDynamicsLookupTable = "list", WindPlantIEC = None, dprefmax = 0.0, dprefmin = 0.0, kiwpp = 0.0, kpwpp = 0.0, prefmax = 0.0, prefmin = 0.0, tpft = 0.0, tpfv = 0.0, twpffilt = 0.0, twppfilt = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.WindPlantIEC = WindPlantIEC
        self.dprefmax = dprefmax
        self.dprefmin = dprefmin
        self.kiwpp = kiwpp
        self.kpwpp = kpwpp
        self.prefmax = prefmax
        self.prefmin = prefmin
        self.tpft = tpft
        self.tpfv = tpfv
        self.twpffilt = twpffilt
        self.twppfilt = twppfilt

    def __str__(self):
        str = "class=WindPlantFreqPcontrolIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
