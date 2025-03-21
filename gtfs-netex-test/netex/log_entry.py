from dataclasses import dataclass

from .log_entry_version_structure import LogEntryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LogEntry(LogEntryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
