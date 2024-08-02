from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class QualityIndexEnumeration(Enum):
    CERTAIN = "certain"
    VERY_RELIABLE = "veryReliable"
    RELIABLE = "reliable"
    PROBABLY_RELIABLE = "probablyReliable"
    UNCONFIRMED = "unconfirmed"
