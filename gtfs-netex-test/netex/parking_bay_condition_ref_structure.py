from dataclasses import dataclass
from .log_entry_ref_structure import LogEntryRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayConditionRefStructure(LogEntryRefStructure):
    value: RestrictedVar
