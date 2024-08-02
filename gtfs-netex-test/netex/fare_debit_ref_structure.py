from dataclasses import dataclass

from .log_entry_ref_structure import LogEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDebitRefStructure(LogEntryRefStructure):
    pass
