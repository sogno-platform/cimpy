from .Base import Base
from .CGMESProfile import Profile


class MonthDay(Base):
    """
    MonthDay format as "--mm-dd", which conforms with XSD data type gMonthDay.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=MonthDay\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
