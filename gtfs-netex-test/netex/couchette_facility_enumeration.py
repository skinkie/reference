from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CouchetteFacilityEnumeration(Enum):
    """Allowed values  for Couchette Facility: UIc.

    :cvar UNKNOWN:
    :cvar T2:
    :cvar T3:
    :cvar C1:
    :cvar C2:
    :cvar C4:
    :cvar C5: pti23_4_1
    :cvar C6:
    :cvar WHEELCHAIR:
    :cvar OTHER:
    """
    UNKNOWN = "unknown"
    T2 = "T2"
    T3 = "T3"
    C1 = "C1"
    C2 = "C2"
    C4 = "C4"
    C5 = "C5"
    C6 = "C6"
    WHEELCHAIR = "wheelchair"
    OTHER = "other"
