from dataclasses import dataclass
from netex.group_ticket_ref_structure import GroupTicketRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupTicketRef(GroupTicketRefStructure):
    """
    Reference to a GROUP TICKET usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
