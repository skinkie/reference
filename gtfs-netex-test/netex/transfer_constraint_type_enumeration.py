from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransferConstraintTypeEnumeration(Enum):
    """
    Allowed values for Transfer Constraint.
    """
    CAN_TRANSFER = "canTransfer"
    CANNOT_TRANSFER = "cannotTransfer"
    OTHER = "other"
