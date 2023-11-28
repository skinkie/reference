from dataclasses import dataclass, field
from netex.group_of_timing_links_rel_structure import GroupOfTimingLinksRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimingLinks(GroupOfTimingLinksRelStructure):
    """A set of TIMING LINKs grouped together according to the similarity of TIME
    BANDs which are relevant to them.

    There may be a GROUP OF TIMING LINKS which covers all TIMING LINKs,
    for use when different GROUPs OF TIMING LINKS are not needed.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
