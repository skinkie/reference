from dataclasses import dataclass, field
from netex.group_of_lines_version_structure import GroupOfLinesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfLines(GroupOfLinesVersionStructure):
    """
    A grouping of LINEs which will be commonly referenced for a specific purpose.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
