from dataclasses import dataclass
from netex.log_entry_ref_structure import LogEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayConditionRefStructure(LogEntryRefStructure):
    """
    Type for a reference to a PPARKING BAY CONDITION.
    """
