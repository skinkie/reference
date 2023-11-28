from dataclasses import dataclass, field
from netex.group_of_timebands_versioned_child_structure import GroupOfTimebandsVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimebands(GroupOfTimebandsVersionedChildStructure):
    """
    A period in a day, significant for some aspect of public transport, e.g.
    similar traffic conditions or fare category.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
