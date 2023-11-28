from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class InterchangeWeightingEnumeration(Enum):
    """
    Allowed values for INTERCHANGE Weighting.
    """
    NO_INTERCHANGE = "noInterchange"
    INTERCHANGE_ALLOWED = "interchangeAllowed"
    RECOMMENDED_INTERCHANGE = "recommendedInterchange"
    PREFERRED_INTERCHANGE = "preferredInterchange"
