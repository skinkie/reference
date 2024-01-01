from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupSizeChangesEnumeration(Enum):
    NO_CHANGES = "noChanges"
    FREE = "free"
    CHARGE = "charge"
    PURCHASE_WINDOW_STEPPED_CHARGE = "purchaseWindowSteppedCharge"
    NUMBER_OF_PASSENGERS_STEPPED_CHARGE = "numberOfPassengersSteppedCharge"
