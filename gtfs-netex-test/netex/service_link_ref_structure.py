from dataclasses import dataclass
from netex.timing_link_ref_structure import TimingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkRefStructure(TimingLinkRefStructure):
    """
    Type for a reference to a SERVICE LINK.
    """
