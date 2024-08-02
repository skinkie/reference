from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VerificationStatusEnumeration(Enum):
    UNKNOWN = "unknown"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    VERIFIED_AS_DUPLICATE = "verifiedAsDuplicate"
    UNDEFINED = "undefined"
