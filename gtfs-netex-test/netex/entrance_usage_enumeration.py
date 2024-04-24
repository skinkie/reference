from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceUsageEnumeration(Enum):
    ENTRY_AND_EXIT = "entryAndExit"
    ENTRY = "entry"
    EXIT = "exit"
    EMERGENCY_EXIT = "emergencyExit"
