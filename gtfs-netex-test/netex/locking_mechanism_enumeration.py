from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingMechanismEnumeration(Enum):
    NONE = "none"
    DOCK = "dock"
    IMMOBILISING_LOCK = "immobilisingLock"
    SEPARATE_LOCKING_DEVICE = "separateLockingDevice"
    OTHER = "other"
