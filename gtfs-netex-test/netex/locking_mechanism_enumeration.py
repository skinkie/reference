from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingMechanismEnumeration(Enum):
    """
    Allowed value for LOCKING MECHANISM.
    """
    NONE = "none"
    DOCK = "dock"
    IMMOBILISING_LOCK = "immobilisingLock"
    SEPARATE_LOCKING_DEVICE = "separateLockingDevice"
    OTHER = "other"
