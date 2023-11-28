from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageStartConstraintTypeEnumeration(Enum):
    """
    Allowed values for Usage Validity Period Start constraint.

    :cvar VARIABLE: Validity start date can be chosen by user.
    :cvar FIXED: Validity start date is constrained. For a pass to
        certain days of week, month or year. For a trip to a specific
        train.
    :cvar FIXED_WINDOW: Validity start date for a trip  is constrained
        relative to  start of booked service, eg may catch previous
        train as well.
    """
    VARIABLE = "variable"
    FIXED = "fixed"
    FIXED_WINDOW = "fixedWindow"
