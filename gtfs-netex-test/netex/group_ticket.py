from dataclasses import dataclass, field
from netex.group_ticket_version_structure import GroupTicketVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupTicket(GroupTicketVersionStructure):
    """
    The number and characteristics of persons entitled to travel in addition to the
    holder of an access right.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
