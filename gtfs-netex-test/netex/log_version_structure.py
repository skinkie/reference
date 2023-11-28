from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.log_entries_rel_structure import LogEntriesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LogVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for  LOG.

    :ivar log_entries: LOG ENTRies using LOG.
    :ivar name_of_log_entry_class: Name of LogEntry Cass of  LOG
    """
    class Meta:
        name = "Log_VersionStructure"

    log_entries: Optional[LogEntriesRelStructure] = field(
        default=None,
        metadata={
            "name": "logEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_log_entry_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfLogEntryClass",
            "type": "Attribute",
        }
    )
