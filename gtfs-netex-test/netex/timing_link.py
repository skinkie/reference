from dataclasses import dataclass, field
from netex.timing_link_version_structure import TimingLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingLink(TimingLinkVersionStructure):
    """An ordered pair of TIMING POINTs for which run times may be recorded.

    Timing links are directional - there will be separate links for each direction of a route.

    :ivar id: Identifier of TIMING LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
