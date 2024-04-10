from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TactileGuidingStripStatusEnumeration(Enum):
    GOOD_AND_CONTRASTED = "goodAndContrasted"
    PRIMITIVE = "primitive"
    INCORRECT = "incorrect"
    BAD = "bad"
