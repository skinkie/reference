from dataclasses import dataclass, field
from netex.group_of_link_sequences_version_structure import GroupOfLinkSequencesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfLinkSequences(GroupOfLinkSequencesVersionStructure):
    """
    A grouping of LINK SEQUENCEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
