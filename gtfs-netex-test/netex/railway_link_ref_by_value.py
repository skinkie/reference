from dataclasses import dataclass
from netex.railway_link_ref_by_value_structure import RailwayLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayLinkRefByValue(RailwayLinkRefByValueStructure):
    """
    Reference to a RAILWAY LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
