from dataclasses import dataclass, field
from netex.group_of_links_version_structure import GroupOfLinksVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfLinks(GroupOfLinksVersionStructure):
    """
    A grouping of LINKs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
