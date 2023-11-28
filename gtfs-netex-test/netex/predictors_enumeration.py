from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictorsEnumeration(Enum):
    """
    Allowed values for predictors.
    """
    AVMS_ONLY = "avmsOnly"
    ANYONE = "anyone"
