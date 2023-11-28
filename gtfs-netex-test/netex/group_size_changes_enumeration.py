from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupSizeChangesEnumeration(Enum):
    """Allowed values for GROUP SIZE CHANGE.

    +v1.1

    :cvar NO_CHANGES: Group size cannot be changed..
    :cvar FREE: No charge to change group size.
    :cvar CHARGE: Group size can be changed for a fee (as specified by a
        EXCHANGING usage parameter).
    :cvar PURCHASE_WINDOW_STEPPED_CHARGE: Group size can be changed,
        charges are according to a sliding scale according to  the
        length of time before travel (as specified by several
        EXCHANGING parameters).
    :cvar NUMBER_OF_PASSENGERS_STEPPED_CHARGE: Group size can be
        changed, charges are according to a sliding scale according to
        the number of passengers changed.
    """
    NO_CHANGES = "noChanges"
    FREE = "free"
    CHARGE = "charge"
    PURCHASE_WINDOW_STEPPED_CHARGE = "purchaseWindowSteppedCharge"
    NUMBER_OF_PASSENGERS_STEPPED_CHARGE = "numberOfPassengersSteppedCharge"
