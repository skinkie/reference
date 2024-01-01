from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransferConstraintTypeEnumeration(Enum):
    CAN_TRANSFER = "canTransfer"
    CANNOT_TRANSFER = "cannotTransfer"
    OTHER = "other"
