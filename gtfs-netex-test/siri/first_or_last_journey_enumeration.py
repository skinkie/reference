from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FirstOrLastJourneyEnumeration(Enum):
    FIRST_SERVICE_OF_DAY = "firstServiceOfDay"
    OTHER_SERVICE = "otherService"
    LAST_SERVICE_OF_DAY = "lastServiceOfDay"
    UNSPECIFIED = "unspecified"
