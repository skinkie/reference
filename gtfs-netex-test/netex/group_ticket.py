from dataclasses import dataclass

from .group_ticket_version_structure import GroupTicketVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupTicket(GroupTicketVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
