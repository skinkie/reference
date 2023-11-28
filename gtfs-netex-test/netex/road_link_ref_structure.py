from dataclasses import dataclass
from netex.infrastructure_link_ref_structure import InfrastructureLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadLinkRefStructure(InfrastructureLinkRefStructure):
    """
    Type for Reference to a ROAD LINK.
    """
