from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RelatedToEnumeration(Enum):
    CAUSE = "cause"
    EFFECT = "effect"
    CORRECTION_TO = "correctionTo"
    UPDATE = "update"
    SUPERCEDES = "supercedes"
    SUPERCEDED_BY = "supercededBy"
    ASSOCIATED = "associated"
