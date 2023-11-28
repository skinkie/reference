from dataclasses import dataclass
from netex.group_of_timing_links_ref_structure import GroupOfTimingLinksRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimingLinksRef(GroupOfTimingLinksRefStructure):
    """
    Reference to a GROUP OF TIMING LINKs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
