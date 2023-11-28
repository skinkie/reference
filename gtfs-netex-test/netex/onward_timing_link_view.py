from dataclasses import dataclass
from netex.onward_timing_link_derived_view_structure import OnwardTimingLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnwardTimingLinkView(OnwardTimingLinkDerivedViewStructure):
    """
    Information about onwards TIMING LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
