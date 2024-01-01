from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ActivationMeansEnumeration(Enum):
    NONE_REQUIRED = "noneRequired"
    CHECK_IN = "checkIn"
    USE_OF_VALIDATOR = "useOfValidator"
    USE_OF_MOBILE_DEVICE = "useOfMobileDevice"
    AUTOMATIC_BY_TIME = "automaticByTime"
    AUTOMATIC_BY_PROXIMITY = "automaticByProximity"
    ACCESS_CODE = "accessCode"
    OTHER = "other"
