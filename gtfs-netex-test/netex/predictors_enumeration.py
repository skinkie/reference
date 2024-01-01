from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictorsEnumeration(Enum):
    AVMS_ONLY = "avmsOnly"
    ANYONE = "anyone"
