from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelativeOperatorEnumeration(Enum):
    """
    Allowed values for Comparison operations.

    :cvar EQ: Parameter value must have same identity, or have value
        equal  to a quantitative value associated with specified item.
    :cvar NE: Parameter value must not have same identity, or have value
        different from  a quantitative value associated with specified
        item.
    :cvar GE: Parameter value must be greater  than  or equal to a
        quantitative value associated with specified item.
    :cvar GT: Parameter value must be greater than a quantitative value
        associated with specified item.
    :cvar LE: Parameter value must be less  than  or equal to a
        quantitative value associated with specified item.
    :cvar LT: Parameter value must be less  than a quantitative value
        associated with specified item.
    """
    EQ = "EQ"
    NE = "NE"
    GE = "GE"
    GT = "GT"
    LE = "LE"
    LT = "LT"
